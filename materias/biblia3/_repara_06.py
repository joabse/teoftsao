# -*- coding: utf-8 -*-
"""Reparo do 06 — regex tolerante a \\n+ para os 5 pontos falhos."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rx(pattern, new, tag):
    global txt
    t2, n = re.subn(pattern, new, txt, count=1, flags=re.S)
    if n == 0:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = t2

# junta a frase que a nota 6/7 interrompia
rx(r"precisou depender tanto\n+@@FN67@@\n+de um evangelho",
   "precisou depender tanto de um evangelho", "j6")

# reinseri as notas 6-7 apos o paragrafo
FN6 = ("6 Leon L. Morris, especialista em NT, considera a data de 68 d.C. para "
       "a composição do evangelho de Marcos muito tardia (Lucas: introdução e "
       "comentário [São Paulo: Vida Nova, 1983; reimp. 1996]). Aceitando-se a "
       "hipótese de Marcos ter sido o primeiro evangelho e de ter sido usado "
       "como fonte por Mateus e Lucas, a aceitação dessa data tardia "
       "estenderia para depois do ano 70 a composição desses dois evangelhos, "
       "o que inviabilizaria o caráter profético dos discursos de Jesus sobre "
       "a destruição de Jerusalém (v. Mt 24; Lc 21), ocorrida em 70 d.C. "
       "Portanto, se Mateus e Lucas contêm discursos genuinamente proféticos, "
       "isso quer dizer que foram escritos antes de 70, o que retrocederia a "
       "datação de Marcos para o início da década de 60. (N. do E.)")
rx(r"em todos os quatro evangelhos, inclusive no primeiro\.\n+Em todo caso,",
   "em todos os quatro evangelhos, inclusive no primeiro.\n\n" + FN6 +
   "\n\n7 V. meu livro Gospel of Mark, p. 1-62.\n\nEm todo caso,", "fn6-7 insere")

# nota 10 (chars reais)
rx(r"\d{0,2}[°º'’o]{0,2}V[.,] minha discussão em The Acts of the Apostles",
   "10 V. minha discussão em The Acts of the Apostles", "fn10")

# nota 11: extrai do meio da frase
rx(r"como a obra de\n+UV\. p\. 19-22\.\n+Lucas, ao enfatizar",
   "como a obra de Lucas, ao enfatizar", "j11")
rx(r"suas implicações políticas\.\n+## João",
   "suas implicações políticas.\n\n11 V. p. 19-22.\n\n## João", "fn11 insere")

# join0 com \n simples
rx(r"obras históricas ou biográficas\n+da época, com a diferença",
   "obras históricas ou biográficas da época, com a diferença", "join0")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
assert "@@" not in txt, "placeholder sobrando!"
P.write_text(txt, encoding="utf-8")
print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print(f"{len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes")
print("FN6 presente:", "6 Leon L. Morris" in txt, "| fn10:", "10 V. minha" in txt,
      "| fn11:", "11 V. p. 19-22." in txt)
