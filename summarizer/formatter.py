# summarizer/formatter.py
import json
from fpdf import FPDF
from jinja2 import Template

def save_markdown(content, output_path="outputs/summary.md"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

import json

def save_json(content, output_path="outputs/summary.json"):
    data = {"summary": content}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def save_pdf(text: str, output_path: str):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    x = 1 * inch
    y = height - 1 * inch
    line_height = 14

    lines = text.split("\n")
    for line in lines:
        wrapped = []
        while len(line) > 100:
            split_at = line.rfind(" ", 0, 100)
            if split_at == -1:
                split_at = 100
            wrapped.append(line[:split_at])
            line = line[split_at:].lstrip()
        wrapped.append(line)

        for part in wrapped:
            if y < 1 * inch:
                c.showPage()
                y = height - 1 * inch
            c.drawString(x, y, part)
            y -= line_height

    c.save()


def render_newsletter(summary, template_path="templates/newsletter_template.jinja2"):
    with open(template_path) as file:
        template = Template(file.read())
    return template.render(content=summary)
