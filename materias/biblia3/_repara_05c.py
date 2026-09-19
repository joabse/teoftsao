# -*- coding: utf-8 -*-
"""Reparo 4 do 05 — microajustes finais."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\05-Witherington_Sinoticos.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, 1)

rep("que quer dizer “fonte”. “problema sinótico”.",
    "que quer dizer “fonte”.\n\n“problema sinótico”.", "F1")
rep("sabedoria de Deus.’ Aliás", "sabedoria de Deus.² Aliás", "F2")
rep("A. À história do sábio", "A. A história do sábio", "F3")
rep("ais do sabio/sabedoria", "ais do sábio/sabedoria", "F4")
rep("Lc 12.8-12/Mc 10.19, 32, 33", "Lc 12.8-12/Mt 10.32, 33", "F6")
rep("agia c falava", "agia e falava", "F7")
rep("À resposta dada por Jesus", "A resposta dada por Jesus", "F8")
rep("p. 602-3. Se havia uma parte", "p. 602-3.\n\nSe havia uma parte", "F9")
rep("O que é Qe por que", "O que é Q e por que", "F10")

lines = [ln for ln in txt.split("\n") if ln.strip() != "85"]
txt = "\n".join(lines)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")
print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print(f"{len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes")
