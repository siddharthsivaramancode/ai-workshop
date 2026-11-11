"""Sanity-check a generated deck without opening PowerPoint.

    uv run --with python-pptx python curriculum/decks/check_deck.py slideshows/*.pptx

Checks: animation targets exist, shapes stay on the slide, transition/timing
XML order, and a rough text-fit estimate (flags text likely to overflow its box).
The fit check is an estimate: always click through the deck in PowerPoint once.
"""
import math
import sys
from pptx import Presentation
from pptx.util import Emu

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
# average glyph width as a fraction of font size (bold-ish text)
WIDTH = {"Arial Black": 0.66, "Courier New": 0.60, "Arial": 0.55}


def est_lines(text, font, size_pt, box_w_in):
    cw = WIDTH.get(font, 0.55) * size_pt / 72  # inches per char
    per_line = max(1, int(box_w_in / cw))
    return sum(max(1, math.ceil(len(seg) / per_line)) for seg in text.split("\n"))


def check(path):
    prs = Presentation(path)
    sw, sh = prs.slide_width, prs.slide_height
    problems = []
    for n, slide in enumerate(prs.slides, 1):
        ids = {sp.shape_id for sp in slide.shapes}
        for t in slide._element.iter(f"{P}spTgt"):
            if int(t.get("spid")) not in ids:
                problems.append(f"slide {n}: animation targets missing shape {t.get('spid')}")
        kids = [c.tag.replace(P, "") for c in slide._element]
        if "timing" in kids and "transition" in kids and kids.index("timing") < kids.index("transition"):
            problems.append(f"slide {n}: timing before transition (PowerPoint will repair)")
        for sp in slide.shapes:
            if sp.width == 0:
                continue
            if sp.left < 0 or sp.top < 0 or sp.left + sp.width > sw + Emu(5000) or sp.top + sp.height > sh + Emu(5000):
                problems.append(f"slide {n}: shape {sp.shape_id} goes off the slide")
            if not sp.has_text_frame or not sp.text_frame.text.strip():
                continue
            w_in = sp.width / 914400 - 0.16
            h_in = sp.height / 914400 - 0.16
            need = 0.0
            for p in sp.text_frame.paragraphs:
                runs = p.runs
                size = max((r.font.size.pt for r in runs if r.font.size), default=18)
                font = next((r.font.name for r in runs if r.font.name), "Arial")
                txt = "".join(r.text for r in runs) or " "
                lines = est_lines(txt, font, size, w_in)
                need += lines * size * 1.2 / 72 * (p.line_spacing or 1.0)
            if need > h_in * 1.15 and need - h_in > 0.25:
                problems.append(f"slide {n}: text may overflow ({need:.1f}in needed, {h_in:.1f}in box): "
                                f"{sp.text_frame.text[:50]!r}")
    print(f"{path}: {len(prs.slides)} slides, {len(problems)} possible problems")
    for p in problems:
        print("  -", p)
    return problems


if __name__ == "__main__":
    bad = sum(len(check(p)) for p in sys.argv[1:])
    sys.exit(1 if bad else 0)
