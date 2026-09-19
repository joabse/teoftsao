# -*- coding: utf-8 -*-
"""Fix-up 07c: varredura com padrão correto (HOM[EI]?LIAS) + 4 junções exatas."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\07-Witherington_Cartas.md")
txt = P.read_text(encoding="utf-8")

def is_header(t):
    t = t.strip()
    if t.startswith("#"):
        return False
    if len(t) < 100 and re.search(r"HOM[EIÍ]?LIAS\s+PARA\s+OS\s+CONVER", t, re.I):
        return True
    if len(t) < 100 and re.search(r"CA\s+HOM[EIÍ]?LIAS\s+PARA\s+OS\s+CONVERTIDOS", t, re.I):
        return True
    if len(t) < 80 and re.search(r"HIST[OÓ]RIA\s+DO\s+NOVO\s+[FT]ESTAMENTO", t, re.I):
        return True
    return False

linhas = txt.split("\n")
removidas = [l for l in linhas if is_header(l)]
txt = "\n".join(l for l in linhas if not is_header(l))
txt = re.sub(r"\n{3,}", "\n\n", txt)
print("CABEÇALHOS REMOVIDOS NESTA PASSAGEM:", len(removidas))
for l in removidas:
    print("   -", l.strip()[:70])

def rep(old, new, tag):
    global txt
    if old not in txt:
        print("[NAO ENCONTRADO]", tag)
        return False
    txt = txt.replace(old, new, 1)
    return True

rep("Isso vale até para um documento\n\ncomo Filemom.",
    "Isso vale até para um documento como Filemom.", "join-doc")
rep("coisas do\n\ngênero. Em particular",
    "coisas do gênero. Em particular", "join-genero")
rep("Paulo escreve motivado\n\npor essa série de acontecimentos",
    "Paulo escreve motivado por essa série de acontecimentos", "join-motivado")
rep("bem-estar dos convertidos dessas\n\ncongregações. Aparentemente",
    "bem-estar dos convertidos dessas congregações. Aparentemente", "join-congreg")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

resid = [l for l in txt.split("\n") if not l.startswith("#") and (
    re.search(r"HOM[EIÍ]?LIAS PARA OS CONVER", l, re.I)
    or re.search(r"HIST[OÓ]RIA DO NOVO", l, re.I)
    or (l.isupper() and len(l.strip()) > 3))]
print("RESÍDUOS EM MAIÚSCULAS:", len(resid))
for r2 in resid[:8]:
    print("   ?", r2[:80])
print("U+FFFD:", txt.count("\ufffd"))
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
