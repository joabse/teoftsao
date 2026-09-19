# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md").read_text(encoding="utf-8")
lines = t.replace("\r\n", "\n").split("\n")
print("linhas:", len(lines), "| bytes:", len(t.encode("utf-8")), "| U+FFFD:", t.count("\ufffd"))
print("--- HEADINGS ---")
for i, ln in enumerate(lines, 1):
    if ln.startswith("#"):
        print(f"{i:5d} {ln[:120]}")
print("--- pipes ---")
print(sum(1 for ln in lines if ln.startswith("|")))
print("--- primeiras 30 linhas ---")
for ln in lines[:30]:
    print(" ", ln[:120])
