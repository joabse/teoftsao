# -*- coding: utf-8 -*-
"""Reparo 2 do 05 — formatos reais pós-strip (\\n simples, notas no meio)."""
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

# fn1 reposicionada + join do parágrafo
rep("um assunto\n\nUma abreviatura da palavra alemã Quelle, que quer dizer “fonte”.\n\nconhecido como",
    "um assunto conhecido como\n\n1 Uma abreviatura da palavra alemã Quelle, "
    "que quer dizer “fonte”.", "fn1+j0")

# join quebra de página com \\n simples
rep("listados de Mateus\ne Lucas para notar", "listados de Mateus e Lucas para notar", "j2")
rep("observe como começa\na história:", "observe como começa a história:", "j5")
rep("conhece uma\nnarrativa da história das últimas", "conhece uma narrativa da história das últimas", "j6")
rep("no rolo de Qumran\n11QMelquisedeque,", "no rolo de Qumran 11QMelquisedeque,", "j11")

# fn8
rep("traz juntas as parábolas\n\n* Estou sugerindo que, talvez antes da composição de Q, o qual também\n"
    "da ovelha perdida e da dracma perdida, segundo a semelhança de suas temáticas. uma coletânea de "
    "parábolas agrupadas\n\npoderia ter existido",
    "8 Estou sugerindo que, talvez antes da composição de Q, o qual também traz "
    "juntas as parábolas da ovelha perdida e da dracma perdida, segundo a "
    "semelhança de suas temáticas, poderia ter existido uma coletânea de "
    "parábolas agrupadas.", "fn8")

# fn9-10 + reanexa o parágrafo interrompido
rep("?V. o levantamento feito por J. B. GREEN no verbete “Passion Narrative”. In: The Dictionary of Jesus\n"
    "and the Gospels, editado por Joel B. Green e Scot McKnight p. 601-4. 'o Essa última hipótese é "
    "defendida na obra magistral de R. Brown, Grove, The Death of the Messiah, 2 vols. Ill.: "
    "InterVarsity, 1992),\n(New York:\n\n(Downers\n\nDoubleday, 1994).",
    "9 V. o levantamento feito por J. B. GREEN no verbete “Passion Narrative”. "
    "In: The Dictionary of Jesus and the Gospels, editado por Joel B. Green e "
    "Scot McKnight (Downers Grove, Ill.: InterVarsity, 1992), p. 601-4.\n\n"
    "10 Essa última hipótese é defendida na obra magistral de R. Brown, The "
    "Death of the Messiah, 2 vols. (New York: Doubleday, 1994).", "fn9-10")
rep("da Paixão que\n\nnão podem ser explicados", "da Paixão que não podem ser explicados", "j4")

# fn11 reposicionada + junção
rep("a execução\n\n11 V., de GREEN, “Passion Narrative”, p. 602-3.\n\npor crucificação e o sepultamento.",
    "a execução por crucificação e o sepultamento.\n\n11 V., de GREEN, "
    "“Passion Narrative”, p. 602-3.", "fn11+j7")

# fn7 reposicionada + junção
rep("não era necessário que esse\n\n“On the Christology of Q”, p. 41.\n\nsumário da história",
    "não era necessário que esse sumário da história", "fn7a")
rep("em todas as fontes e documentos cristãos.\n\nVamos examinar",
    "em todas as fontes e documentos cristãos.\n\n“On the Christology of Q”, "
    "p. 41.\n\nVamos examinar", "fn7b")

# legenda da foto (formato real)
rep("As s atuais at ruínas d da sinagoga goga de de Caf. Cafarnaum datam datam do do t terceiro século\n"
    "parecem ser da época da sinagoga do primeiro século, onde as palavras de Jesus foram ouvidas.\n\n"
    "éculo d de nossa era, mas suas fundaç fundações",
    "*As atuais ruínas da sinagoga de Cafarnaum datam do terceiro século de "
    "nossa era, mas suas fundações parecem ser da época da sinagoga do "
    "primeiro século, onde as palavras de Jesus foram ouvidas.*", "legenda")

# tabela de Q
rep("1. O precursor e o anúncio da vinda do sábio (por Joao) — Lc 3.2-9/Mt\n"
    "3.1-10; Le 3.15-17/Mt 3.11-12",
    "1. O precursor e o anúncio da vinda do sábio (por João) — Lc 3.2-9/Mt "
    "3.1-10; Lc 3.15-17/Mt 3.11-12", "Q1")
rep("30. Oriente e ocidente/Primeiro e ultimo — Lc 13.28-30/Mt 8.11, 12;\n20.16",
    "30. Oriente e ocidente/Primeiro e último — Lc 13.28-30/Mt 8.11, 12; 20.16", "Q30")
rep("41. Contra falsas esperanças — Lc 17.22, 23/Mt\n"
    "42. Como um relâmpago — Lc 17.24/Mt\n"
    "43. Como aburres — Lc 17.37/Mt 24.28\n\n24.26\n24.27",
    "41. Contra falsas esperanças — Lc 17.22, 23/Mt 24.26\n"
    "42. Como um relâmpago — Lc 17.24/Mt 24.27\n"
    "43. Como abutres — Lc 17.37/Mt 24.28", "Q41-43")

# separa frases "A parte N termina" coladas aos itens
for n, meio in [("cinco", "35. A dracma perdida — Lc 15.8-10 A parte cinco termina"),
                ("três", "15. Os ais de sabedoria — Lc 11.42-52/Mt 23 (porções) A parte três termina"),
                ("quatro", "27. A sabedoria lamenta por Jerusalém — Lc 13.34, 35/Mt 23.37-39 A parte quatro termina"),
                ("seis", "40. Fé como a semente de mostarda — Lc 17.5, 6/Mt 17.20 A parte seis termina"),
                ("sete", "49. Lugares à mesa e em tronos no reino — Lc 22.28-30/Mt 19.28 A parte sete é um discurso escatológico")]:
    antigo = meio
    novo = re.sub(r" A parte (cinco|três|quatro|seis|sete) termina", r"\n\nA parte \1 termina", meio, count=1)
    if n == "sete":
        novo = re.sub(r" A parte (sete) é um discurso", r"\n\nA parte \1 é um discurso", antigo, count=1)
    rep(antigo, novo, f"parte-{n}")

# marcadores
rep("tenha ocorrido? ou, pelo menos", "tenha ocorrido⁹ ou, pelo menos", "mk9")
rep("o primeiro evangelho.” De fato", "o primeiro evangelho.¹⁰ De fato", "mk10")

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
heads = [ln for ln in txt.split("\n") if ln.startswith("#")]
print("headings:", len(heads))
for h in heads:
    print(" ", h)
print("pipes:", sum(1 for ln in txt.split("\n") if ln.startswith("|")))
print(f"{len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes")
