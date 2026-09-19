# -*- coding: utf-8 -*-
"""Estrutura do 05: headings + início de cada página."""
from pathlib import Path
t = Path(r"01_markdown\adicionais\05-Witherington_Sinoticos.md").read_text(encoding="utf-8")
lines = t.replace("\r\n", "\n").split("\n")
print("linhas:", len(lines), "| bytes:", len(t.encode("utf-8")))
print("--- HEADINGS ---")
for i, ln in enumerate(lines, 1):
    if ln.startswith("#"):
        print(f"{i:5d} {ln[:110]}")
print("--- primeiras 25 linhas ---")
for ln in lines[:25]:
    print(" ", ln[:110])
