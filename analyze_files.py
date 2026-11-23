from pathlib import Path
import pymupdf
from pptx import Presentation
from PIL import Image


def analyze_pdf(path: Path) -> None:
    print(f"=== PDF: {path.name} ===")
    try:
        with pymupdf.open(path) as doc:
            print(f"  Seiten: {len(doc)}")
            for i, page in enumerate(doc):
                text = page.get_text("text").strip()
                images = page.get_images()
                preview = " | ".join(
                    line.strip() for line in text.splitlines() if line.strip()
                )[:300]
                print(f"  [S.{i+1}] (Bilder={len(images)}, Zeichen={len(text)}): {preview}")
    except Exception as e:
        print(f"  FEHLER: {e}")


def analyze_pptx(path: Path) -> None:
    print(f"=== PPTX: {path.name} ===")
    try:
        prs = Presentation(str(path))
        print(f"  Folien: {len(prs.slides)}")
        for i, slide in enumerate(prs.slides):
            texts = []
            pics = 0
            for shape in slide.shapes:
                if shape.has_text_frame:
                    t = shape.text_frame.text.strip()
                    if t:
                        texts.append(" ".join(t.split()))
                if hasattr(shape, "image"):
                    pics += 1
            preview = " | ".join(texts)[:300]
            print(f"  [Folie {i+1}] (Bilder={pics}): {preview}")
    except Exception as e:
        print(f"  FEHLER: {e}")


def analyze_image(path: Path) -> None:
    print(f"=== BILD: {path.name} ===")
    try:
        with Image.open(path) as img:
            print(f"  Format: {img.format}, Auflösung: {img.size[0]}x{img.size[1]}, Modus: {img.mode}")
    except Exception as e:
        print(f"  FEHLER: {e}")


def main() -> None:
    root = Path(".")
    files = sorted(root.iterdir(), key=lambda p: p.name.lower())
    for f in files:
        if f.is_file():
            ext = f.suffix.lower()
            if ext == ".pdf":
                analyze_pdf(f)
            elif ext == ".pptx":
                analyze_pptx(f)
            elif ext in {".png", ".jpg", ".jpeg"}:
                analyze_image(f)


if __name__ == "__main__":
    main()
