#!/usr/bin/env python3
"""
Render a Hormozi Council audit JSON into a PDF using the HTML template + Playwright.

Usage:
    python3 render-audit-pdf.py <audit-json-path> [<output-pdf-path>]

If output path is omitted, derives it from the JSON path by swapping .json -> .pdf.
"""

import asyncio
import json
import sys
from pathlib import Path
from jinja2 import Template
from playwright.async_api import async_playwright

SKILL_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = SKILL_DIR / "audit-pdf-template.html"


async def render(json_path: Path, output_path: Path) -> None:
    data = json.loads(json_path.read_text())
    template = Template(TEMPLATE_PATH.read_text())
    html = template.render(**data)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_content(html, wait_until="networkidle")
        await page.pdf(
            path=str(output_path),
            format="Letter",
            margin={"top": "18mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
            print_background=True,
        )
        await browser.close()


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: render-audit-pdf.py <audit-json-path> [<output-pdf-path>]", file=sys.stderr)
        return 2

    json_path = Path(sys.argv[1]).expanduser().resolve()
    if not json_path.exists():
        print(f"error: {json_path} does not exist", file=sys.stderr)
        return 1

    output_path = (
        Path(sys.argv[2]).expanduser().resolve()
        if len(sys.argv) >= 3
        else json_path.with_suffix(".pdf")
    )

    asyncio.run(render(json_path, output_path))
    print(str(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
