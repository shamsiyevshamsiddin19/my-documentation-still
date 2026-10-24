#!/usr/bin/env python3
"""Shamsiyev uslubidagi bo'sh A4 darslik PDF shablonini yaratadi."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


# Brend matnlari bitta joyda turadi: yangi loyiha uchun shu qiymatlarni almashtirish kifoya.
BRAND_NAME = "shamsiyev"
FOOTER_TEXT = "shamsiyev.uz"

# Darsliklar oilasining asosiy ranglari.
BRAND_RED = HexColor("#B71C1C")
TEXT_DARK = HexColor("#111111")
NEUTRAL_GREY = HexColor("#B0B0B0")


@dataclass(frozen=True)
class Layout:
    """A4 sahifa o'lchamlari va qat'iy joylashuv qoidalari."""

    width: float = A4[0]
    height: float = A4[1]
    left_margin: float = 62.35
    right_margin: float = 61.75
    logo_width: float = 107.25
    logo_height: float = 27.0


LAYOUT = Layout()


def find_font(*names: str) -> Path | None:
    """Ko'p Linux distributivlarida uchraydigan shrift faylini qidiradi."""
    font_directories = (
        Path("/usr/share/fonts/truetype/liberation"),
        Path("/usr/share/fonts/truetype/liberation2"),
        Path("/usr/share/fonts/truetype/dejavu"),
    )

    for directory in font_directories:
        for name in names:
            candidate = directory / name
            if candidate.is_file():
                return candidate
    return None


def register_fonts() -> dict[str, str]:
    """Cyrillic va o'zbekcha matnni qo'llaydigan shriftlarni ro'yxatdan o'tkazadi."""
    serif_regular = find_font("LiberationSerif-Regular.ttf", "DejaVuSerif.ttf")
    serif_bold = find_font("LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf")
    sans_regular = find_font("LiberationSans-Regular.ttf", "DejaVuSans.ttf")
    sans_bold = find_font("LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf")

    required_fonts = (serif_regular, serif_bold, sans_regular, sans_bold)
    if any(font is None for font in required_fonts):
        raise RuntimeError(
            "Liberation yoki DejaVu shriftlari topilmadi. "
            "Tizimga Unicode TrueType shriftlarini o'rnating."
        )

    font_files = {
        "TemplateSerif": serif_regular,
        "TemplateSerifBold": serif_bold,
        "TemplateSans": sans_regular,
        "TemplateSansBold": sans_bold,
    }
    for font_name, font_path in font_files.items():
        pdfmetrics.registerFont(TTFont(font_name, str(font_path)))

    return {name: name for name in font_files}


def draw_header(canvas: Canvas, title: str, page_number: int, fonts: dict[str, str]) -> None:
    """Har bir sahifadagi brend, mavzu va sahifa raqamini chizadi."""
    logo_x = LAYOUT.left_margin
    logo_y = LAYOUT.height - 78.0

    canvas.setFillColor(BRAND_RED)
    canvas.rect(logo_x, logo_y, LAYOUT.logo_width, LAYOUT.logo_height, stroke=0, fill=1)
    canvas.setFillColor(white)
    canvas.setFont(fonts["TemplateSansBold"], 15.5)
    canvas.drawString(logo_x + 10.5, logo_y + 7.5, BRAND_NAME)

    badge_width, badge_height = 24.0, 13.5
    badge_x = LAYOUT.width - LAYOUT.right_margin - badge_width
    badge_y = logo_y + (LAYOUT.logo_height - badge_height) / 2
    canvas.setFillColor(NEUTRAL_GREY)
    canvas.rect(badge_x, badge_y, badge_width, badge_height, stroke=0, fill=1)
    canvas.setFillColor(white)
    canvas.setFont(fonts["TemplateSansBold"], 10.5)
    canvas.drawCentredString(badge_x + badge_width / 2, badge_y + 3.0, str(page_number))

    canvas.setFillColor(TEXT_DARK)
    canvas.setFont(fonts["TemplateSans"], 11.25)
    canvas.drawRightString(badge_x - 10.0, badge_y + 3.0, title)


def draw_footer(canvas: Canvas, fonts: dict[str, str]) -> None:
    """Footerdagi doimiy brend yozuvini chizadi."""
    canvas.setFillColor(NEUTRAL_GREY)
    canvas.setFont(fonts["TemplateSerif"], 10.5)
    canvas.drawCentredString(LAYOUT.width / 2, 43.9, FOOTER_TEXT)


def create_template(output_path: Path, title: str) -> None:
    """Header va footerli mutlaqo bo'sh bitta A4 darslik qolipini yaratadi."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fonts = register_fonts()
    canvas = Canvas(str(output_path), pagesize=A4)
    canvas.setTitle("Darslik shabloni")
    canvas.setAuthor(BRAND_NAME)

    draw_header(canvas, title, 1, fonts)
    draw_footer(canvas, fonts)
    canvas.save()


def parse_arguments() -> argparse.Namespace:
    """Buyruq satridan mavzu nomi va chiqish PDF manzilini o'qiydi."""
    parser = argparse.ArgumentParser(description="A4 darslik PDF shablonini yaratadi.")
    parser.add_argument(
        "--title",
        default="[Hujjat / Mavzu nomi]",
        help="Headerda ko'rinadigan mavzu yoki hujjat nomi.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("Darslik_shabloni.pdf"),
        help="Yaratiladigan PDF manzili.",
    )
    return parser.parse_args()


def main() -> int:
    """Xatoni tushunarli xabar bilan yakunlaydigan dastur kirish nuqtasi."""
    arguments = parse_arguments()
    try:
        create_template(arguments.output, arguments.title)
    except (OSError, RuntimeError) as error:
        print(f"PDF yaratilmadi: {error}")
        return 1

    print(f"PDF yaratildi: {arguments.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
