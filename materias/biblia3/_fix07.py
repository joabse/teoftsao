# -*- coding: utf-8 -*-
"""Fix-up 07: varredura agressiva de cabeçalhos + drop 'p. Iss.' + joins restantes."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\07-Witherington_Cartas.md")
txt = P.read_text(encoding="utf-8")
erros = []

def is_header(t):
    t = t.strip()
    if t.startswith("#"):
        return False
    if len(t) < 100 and re.search(r"CARTAS\s+[ÉEe]?\s*HOM[EL]LIAS\s+PARA\s+OS\s+CONVER", t, re.I):
        return True
    if len(t) < 100 and re.search(r"CA\s+HOMILIAS\s+PARA\s+OS\s+CONVERTIDOS", t, re.I):
        return True
    if len(t) < 80 and re.search(r"HIST[OÓ]RIA\s+DO\s+NOVO\s+[FT]ESTAMENTO", t, re.I):
        return True
    if re.match(r"^p\. Iss\.$", t):
        return True
    return False

antes = txt.count("\n")
linhas = [l for l in txt.split("\n") if not is_header(l)]
txt = "\n".join(linhas)
txt = re.sub(r"\n{3,}", "\n\n", txt)

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, 1)

rep("Isso vale até para um documento\n\ncomo Filemom.",
    "Isso vale até para um documento como Filemom.", "join-doc")
rep("comerem em templos pagãos e coisas do\n\ngênero. Em particular",
    "comerem em templos pagãos e coisas do gênero. Em particular", "join-genero")
rep("Paulo escreve motivado\n\npor essa série de acontecimentos",
    "Paulo escreve motivado por essa série de acontecimentos", "join-motivado")
rep("bem-estar dos convertidos dessas\n\ncongregações. Aparentemente",
    "bem-estar dos convertidos dessas congregações. Aparentemente", "join-congreg")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
suspeitas = [l for l in txt.split("\n")
             if (re.search(r"HOM[EL]LIAS PARA OS CONVER", l, re.I)
                 or re.search(r"HIST[OÓ]RIA DO NOVO [FT]ESTAMENTO", l, re.I)
                 or "p. Iss." in l) and not l.startswith("#")]
print("SUSPEITAS RESTANTES:", len(suspeitas))
for s in suspeitas[:6]:
    print("   ", s[:90])
print("U+FFFD:", txt.count("\ufffd"))
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
