// pdftoppm-compatible page renderer built on macOS's own PDFKit.
//
// Exists because Claude Code's file reader shells out to poppler's `pdftoppm`
// to turn PDF pages into images, and this machine has no Homebrew and so no
// poppler. Rather than install a package manager to get one binary, this uses
// PDFKit, which ships with macOS.
//
// It implements the subset poppler's pdftoppm exposes that the reader actually
// uses: -png, -r <dpi>, -f <first>, -l <last>, and the trailing
// "input.pdf out-prefix" pair. Unknown flags are ignored rather than fatal —
// a renderer that dies on an option it merely does not care about is worse
// than one that renders the page.
//
// Output naming follows poppler: <prefix>-<n>.png, with n zero-padded to the
// width of the highest page number requested.

import Foundation
import PDFKit
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

func fail(_ msg: String) -> Never {
    FileHandle.standardError.write(("pdftoppm: " + msg + "\n").data(using: .utf8)!)
    exit(1)
}

var args = Array(CommandLine.arguments.dropFirst())
var dpi: Double = 150
var first: Int? = nil
var last: Int? = nil
var positional: [String] = []

// The output format is chosen by flag, and the FILE EXTENSION follows it —
// poppler writes -jpeg as <prefix>-<n>.jpg. Getting that wrong is silent: the
// pages render fine and the caller finds no files, because it is looking for a
// different name. That is exactly how this was first shipped broken.
enum OutFormat { case png, jpeg, tiff }
var format: OutFormat = .png

// Flags that CONSUME the next argument. This has to be a list rather than a
// guess, because getting one wrong is not a cosmetic failure: an unlisted
// value-taking flag leaves its value loose, the loop reads it as a positional,
// and it becomes the input filename. `-aa yes` did exactly that and the
// renderer reported "could not open yes as a PDF" — a confusing message about
// the wrong thing entirely. The selftest covers it.
let takesValue: Set<String> = [
    "-r", "-rx", "-ry", "-f", "-l", "-x", "-y", "-W", "-H",
    "-scale-to", "-scale-to-x", "-scale-to-y",
    "-aa", "-aaVector", "-jpegopt", "-thinlinemode",
    "-sep", "-opw", "-upw", "-o", "-tiffcompression",
]

var i = 0
while i < args.count {
    let a = args[i]
    if takesValue.contains(a) {
        i += 1
        guard i < args.count else { break }
        switch a {
        case "-r", "-rx", "-ry": if let v = Double(args[i]) { dpi = v }
        case "-f": first = Int(args[i])
        case "-l": last = Int(args[i])
        default: break                          // consumed and ignored
        }
    } else if a == "-png" {
        format = .png
    } else if a == "-jpeg" || a == "-jpegcmyk" {
        format = .jpeg
    } else if a == "-tiff" {
        format = .tiff
    } else if a.hasPrefix("-") {
        // Any other switch: ignored rather than fatal. poppler has a long tail
        // of options, and dying on one we merely do not implement would turn a
        // cosmetic gap into a failed read.
    } else {
        positional.append(a)
    }
    i += 1
}

guard positional.count >= 1 else { fail("no input PDF given") }
let inputPath = positional[0]
let prefix = positional.count >= 2 ? positional[1] : String(inputPath.dropLast(4))

guard let doc = PDFDocument(url: URL(fileURLWithPath: inputPath)) else {
    fail("could not open \(inputPath) as a PDF")
}

let pageCount = doc.pageCount
let from = max(1, first ?? 1)
let to = min(pageCount, last ?? pageCount)
guard from <= to else { fail("page range \(from)-\(to) is empty (document has \(pageCount))") }

let width = String(to).count
let scale = dpi / 72.0

// PIXEL BUDGET. The page size comes from the file's MediaBox, and for a mail
// attachment that is the sender's choice: a one-page PDF whose only hostile
// property is a 100,000-point MediaBox, rendered at the reader's fixed 100 dpi,
// ran 104 s at 4.4 GB resident (review CC4). A bitmap is four bytes a pixel, so
// the default budget of 64 million pixels bounds one page at about 256 MB — an
// A0 sheet at 150 dpi (35 million) still fits. A page over budget is refused
// with a named error and a non-zero exit, before anything is allocated.
// CCPDF_MAX_PIXELS overrides it for a machine that wants more or less. The
// sums are done in Double, because converting an infinite or NaN size to Int
// traps.
let defaultMaxPixels: Double = 64_000_000
var maxPixels = defaultMaxPixels
if let raw = ProcessInfo.processInfo.environment["CCPDF_MAX_PIXELS"] {
    guard let v = Double(raw), v >= 1, v.isFinite else {
        fail("CCPDF_MAX_PIXELS must be a number of pixels, 1 or more (got \"\(raw)\")")
    }
    maxPixels = v
}
guard scale.isFinite, scale > 0 else { fail("-r must be a positive resolution (got \(dpi))") }

for n in from...to {
    guard let page = doc.page(at: n - 1) else { continue }
    let box = page.bounds(for: .mediaBox)
    let wantW = (Double(box.width) * scale).rounded()
    let wantH = (Double(box.height) * scale).rounded()
    guard wantW.isFinite, wantH.isFinite else {
        fail("page \(n) has a non-finite size — refusing")
    }
    guard wantW > 0, wantH > 0 else { continue }
    if wantW * wantH > maxPixels {
        fail("page \(n) would be \(Int(min(wantW, 1e9))) x \(Int(min(wantH, 1e9))) px " +
             "(\(Int(min(wantW * wantH / 1_000_000, 1e12))) Mpx), over the \(Int(maxPixels / 1_000_000)) Mpx " +
             "budget — refusing before allocating. Use a lower -r, or raise CCPDF_MAX_PIXELS.")
    }
    let pxW = Int(wantW)
    let pxH = Int(wantH)

    guard let ctx = CGContext(
        data: nil, width: pxW, height: pxH,
        bitsPerComponent: 8, bytesPerRow: 0,
        space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)
    else { fail("could not allocate a \(pxW)x\(pxH) bitmap for page \(n)") }

    // White ground: a PDF page is transparent where nothing is drawn, and a
    // transparent PNG reads as a black page in most viewers.
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: pxW, height: pxH))
    ctx.scaleBy(x: scale, y: scale)
    ctx.translateBy(x: -box.origin.x, y: -box.origin.y)
    page.draw(with: .mediaBox, to: ctx)

    guard let image = ctx.makeImage() else { fail("page \(n) did not render") }
    let ext: String
    let type: UTType
    switch format {
    case .png:  ext = "png"; type = .png
    case .jpeg: ext = "jpg"; type = .jpeg
    case .tiff: ext = "tif"; type = .tiff
    }
    let name = String(format: "%@-%0\(width)d.%@", prefix, n, ext)
    let url = URL(fileURLWithPath: name)
    guard let dest = CGImageDestinationCreateWithURL(
        url as CFURL, type.identifier as CFString, 1, nil)
    else { fail("could not write \(name)") }
    CGImageDestinationAddImage(dest, image, nil)
    if !CGImageDestinationFinalize(dest) { fail("could not finalise \(name)") }
}
