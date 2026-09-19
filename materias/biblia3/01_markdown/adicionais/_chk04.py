# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader
pdf = os.path.join(os.environ["TEMP"], "_tmp_b3_04_ocr.pdf")
r = PdfReader(pdf)
starts = [(p.extract_text() or "")[:60].replace("\n", " ") for p in r.pages]
for i, s in enumerate(starts):
    print(f"p{i+1:02d}: {s}")
dups = [(i+1, j+1) for i in range(len(starts)) for j in range(i+1, len(starts)) if starts[i][:18] == starts[j][:18]]
print("DUP (candidatos):", dups)
