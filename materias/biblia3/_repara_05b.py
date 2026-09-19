# -*- coding: utf-8 -*-
"""Reparo 3 do 05 — reposiciona notas 9/10 e 7."""
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

FN9_10 = ("9 V. o levantamento feito por J. B. GREEN no verbete “Passion "
          "Narrative”. In: The Dictionary of Jesus and the Gospels, editado "
          "por Joel B. Green e Scot McKnight (Downers Grove, Ill.: "
          "InterVarsity, 1992), p. 601-4.\n\n10 Essa última hipótese é "
          "defendida na obra magistral de R. Brown, The Death of the Messiah, "
          "2 vols. (New York: Doubleday, 1994).")

rep("na narrativa da Paixão que\n\n" + FN9_10 + "\n\nnão podem ser explicados",
    "na narrativa da Paixão que não podem ser explicados", "j4-extrai")
rep('profecia historicizada." Devemos concluir',
    'profecia historicizada."\n\n' + FN9_10 + "\n\nDevemos concluir", "fn9-10-insere")

rep("aparecesse em todas as fontes e documentos cristãos. Vamos examinar",
    "aparecesse em todas as fontes e documentos cristãos.\n\n“On the "
    "Christology of Q”, p. 41.\n\nVamos examinar", "fn7-insere")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")
print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print(f"{len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes")
