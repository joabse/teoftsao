# -*- coding: utf-8 -*-
"""Reparo final 06 — insere notas 6/7 (espaço simples entre frases)."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md")
txt = P.read_text(encoding="utf-8")

FN67 = ("6 Leon L. Morris, especialista em NT, considera a data de 68 d.C. para "
        "a composição do evangelho de Marcos muito tardia (Lucas: introdução e "
        "comentário [São Paulo: Vida Nova, 1983; reimp. 1996]). Aceitando-se a "
        "hipótese de Marcos ter sido o primeiro evangelho e de ter sido usado "
        "como fonte por Mateus e Lucas, a aceitação dessa data tardia "
        "estenderia para depois do ano 70 a composição desses dois evangelhos, "
        "o que inviabilizaria o caráter profético dos discursos de Jesus sobre "
        "a destruição de Jerusalém (v. Mt 24; Lc 21), ocorrida em 70 d.C. "
        "Portanto, se Mateus e Lucas contêm discursos genuinamente proféticos, "
        "isso quer dizer que foram escritos antes de 70, o que retrocederia a "
        "datação de Marcos para o início da década de 60. (N. do E.)\n\n"
        "7 V. meu livro Gospel of Mark, p. 1-62.")

old = "em todos os quatro evangelhos, inclusive no primeiro. Em todo caso,"
new = ("em todos os quatro evangelhos, inclusive no primeiro.\n\n" + FN67 +
       "\n\nEm todo caso,")
assert old in txt
txt = txt.replace(old, new, 1)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")
ok = all(s in txt for s in ["6 Leon L. Morris", "7 V. meu livro Gospel of Mark",
                            "5 Sobre o assunto", "8 Sobre essa datação",
                            "9 V. meu livro Jesus the Sage", "10 V. minha",
                            "11 V. p. 19-22.", "12 Sobre esse assunto",
                            "13 Também conhecida"])
print("todas as notas 1-13 presentes:", ok)
print(f"{len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes")
