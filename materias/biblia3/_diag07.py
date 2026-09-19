# -*- coding: utf-8 -*-
from pypdf import PdfReader
from pathlib import Path

src = Path(r"00_originais")
pdf = next(src.glob("07-Witherington*"))
print("ARQUIVO:", pdf.name, "|", round(pdf.stat().st_size / 1e6, 1), "MB")
r = PdfReader(str(pdf))
print("PÁGINAS:", len(r.pages))
with_text = 0
sample = ""
for p in r.pages:
    t = (p.extract_text() or "").strip()
    if len(t) > 40:
        with_text += 1
        if not sample:
            sample = t[:120].replace("\n", " | ")
print(f"páginas com texto nativo (>40 chars): {with_text}/{len(r.pages)}")
print("amostra:", sample)
