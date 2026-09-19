# -*- coding: utf-8 -*-
"""Extrai o texto OCR de _ocr08.pdf para o md bruto (pré-consolidação)."""
from pypdf import PdfReader
from pathlib import Path

r = PdfReader("_ocr08.pdf")
parts = []
for pg in r.pages:
    parts.append(pg.extract_text() or "")
out = "\n\n".join(p.replace("\r\n", "\n") for p in parts)
Path(r"01_markdown\adicionais\08-Witherington_Joao.md").write_text(out, encoding="utf-8")
print("paginas:", len(r.pages), "| bytes:", len(out.encode("utf-8")), "| linhas:", out.count("\n") + 1)
