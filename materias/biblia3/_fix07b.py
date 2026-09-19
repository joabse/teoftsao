# -*- coding: utf-8 -*-
"""Fix-up 07b: junções com whitespace flexível (linhas do OCR têm espaço à direita)."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\07-Witherington_Cartas.md")
txt = P.read_text(encoding="utf-8")

JOINS = [
    (r"Isso vale até para um documento[ ]*\n\ncomo Filemom\.",
     "Isso vale até para um documento como Filemom."),
    (r"coisas do[ ]*\n\ngênero\. Em particular",
     "coisas do gênero. Em particular"),
    (r"Paulo escreve motivado[ ]*\n\npor essa série",
     "Paulo escreve motivado por essa série"),
    (r"bem-estar dos convertidos dessas[ ]*\n\ncongregações\. Aparentemente",
     "bem-estar dos convertidos dessas congregações. Aparentemente"),
]
falhas = 0
for pat, new in JOINS:
    txt, n = re.subn(pat, new, txt, count=1)
    if n == 0:
        falhas += 1
        print("[NAO ENCONTRADO]", pat[:60])

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")
print("FALHAS:", falhas)
print("U+FFFD:", txt.count("\ufffd"))
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
