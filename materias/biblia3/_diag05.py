# -*- coding: utf-8 -*-
"""Diagnóstico: nº de páginas e presença de camada de texto."""
from pypdf import PdfReader
from pathlib import Path

src = Path(r"00_originais")
pdf = next(src.glob("05-Witherington*"))
print("ARQUIVO:", pdf.name, "|", round(pdf.stat().st_size / 1e6, 1), "MB")
r = PdfReader(str(pdf))
print("PÁGINAS:", len(r.pages))
with_text = 0
sample = ""
for i, p in enumerate(r.pages):
    t = (p.extract_text() or "").strip()
    if len(t) > 40:
        with_text += 1
        if not sample:
            sample = t[:150].replace("\n", " | ")
print(f"páginas com texto nativo (>40 chars): {with_text}/{len(r.pages)}")
print("amostra:", sample[:150])
img_pages = []
for i, p in enumerate(r.pages):
    try:
        n = len(p.images)
    except Exception:
        n = -1
    img_pages.append(n)
print("imagens por página (primeiras 30):", img_pages[:30])
