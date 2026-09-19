# -*- coding: utf-8 -*-
"""Reparo fase C (linhas unidas com \\n simples) + democao dos falsos
titulos ####/##### restantes (bloco 'Jesus, mas Paulo e ainda')."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\04-Alter_NTLiterGrecoRomana.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, 1)

# 1) demove TODOS os falsos titulos com 3+ hashes (nao existem ### reais)
antes = len(re.findall(r"(?m)^#{3,6}\s", txt))
txt = re.sub(r"(?m)^#{3,6}\s", "", txt)
print(f"democoes aplicadas: {antes}")

# 2) une o bloco de fragmentos (ordem do arquivo preservada)
m = re.search(r"(?m)^Jesus, mas Paulo é ainda$", txt)
m2 = re.search(r"(?m)^essa redenção a outros no$", txt)
if m and m2 and m.start() < m2.start():
    seg = txt[m.start():m2.end()]
    joined = " ".join(l.strip() for l in seg.splitlines() if l.strip())
    txt = txt[:m.start()] + joined + txt[m2.end():]
    print("bloco Jesus unido")
else:
    erros.append("[NAO ENCONTRADO] bloco Jesus")

rep("essa redenção a outros no\n\nnovo mundo. organização",
    "essa redenção a outros no novo mundo.\n\norganização", "novo mundo")

# 3) reassemblagens fase C com \\n simples
rep("leitores,\n\nde língua grega, do Império Romano. As expectativas de seus "
    "possíveis leitores,\nque devemos entender",
    "leitores,\n\nque devemos entender", "C0 dedup")

rep("servidores da observação escrever sobre todos os detalhes\n\n"
    "palavra, eu decidi depois de cuidadosa\ndesde o início. (1:1-3 [TA])",
    "servidores da palavra, eu decidi depois de cuidadosa observação escrever "
    "sobre todos os detalhes desde o início. (1:1-3 [TA])", "C1 Lucas 1:1-3")

rep("(Anais 15:\n62-63); Dion de Prusa distorce (Oração 13).\n\n"
    "a história de seu exílio para se assemelhar a Sócrates",
    "(Anais 15:62-63); Dion de Prusa distorce a história de seu exílio para se "
    "assemelhar a Sócrates (Oração 13).", "C2 nota 4")

rep("8 Essa posição University, 1981). é bem delineada em Trembley, J. T, The "
    "Beloved Self (Tese de Doutorado, Princeton\n\n7 Aafirmação definitiva da "
    "concepção de que as novelas são narrativas de culto disfarçadas é Roman",
    "8 Essa posição é bem delineada em Trembley, J. T, The Beloved Self (Tese de "
    "Doutorado, Princeton University, 1981).", "C3 notas 7/8")

rep("10 Ver White, J. L. New Testament Epistolary in the Framework of Ancient "
    "Epistolography,\nund Niedergang Welt II 25.2, Berlin, 1984, p.1730-56, esp. "
    "p.1733-51.\n\nL,terature Aufstieg der Rômischen",
    "10 Ver White, J. L. New Testament Epistolary Literature in the Framework of "
    "Ancient Epistolography, in Aufstieg und Niedergang der Römischen Welt II "
    "25.2, Berlin, 1984, p.1730-56, esp. p.1733-51.", "C4 nota 10")

rep("WHITE, J. L. New Testament Epistolary Litarature in the Framework of Ancient "
    "Epistolography\nin Aufstieg und Niedergang der Rémischen Welt 1 25:2, Berlin, "
    "1984, p.170-56.",
    "WHITE, J. L. New Testament Epistolary Literature in the Framework of Ancient "
    "Epistolography in Aufstieg und Niedergang der Römischen Welt 1 25:2, Berlin, "
    "1984, p.170-56.", "C7 ref White")

rep("(1:98), Ver Pseudo-Aristóteles, De mundo\n\n12 A descrição da cidade se "
    "origina em Heródoto\nimperial.\n\nApuleio traduz De mundo de modo a fazê-lo "
    "refletir a mistificação da burocracia 398a11-b10.",
    "12 A descrição da cidade se origina em Heródoto (1:98), Ver "
    "Pseudo-Aristóteles, De mundo 398a11-b10. Apuleio traduz De mundo de modo a "
    "fazê-lo refletir a mistificação da burocracia imperial.", "C8 nota 12")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print("--- HEADINGS ---")
for h in txt.split("\n"):
    if h.startswith("#"):
        print(" ", h)
print(f"--- {len(txt.splitlines())} linhas ---")
