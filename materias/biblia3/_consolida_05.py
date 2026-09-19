# -*- coding: utf-8 -*-
"""Consolida 05-Witherington_Sinoticos.md — cap. 'Pedagogia e Paixão' de
'A História do Novo Testamento' (Ben Witherington III, Ed. Vida Nova, 2005).
OCR local limpo (monocolunar). Ajustes: capa, cabeçalhos correntes, notas,
numeração da tabela de Q, junções de quebra de página."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\05-Witherington_Sinoticos.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rep(old, new, tag, cnt=1):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, cnt)

# ---------- 1) strip de tabelas ----------
lines = txt.replace("\r\n", "\n").split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith("|"):
        while i < len(lines) and lines[i].startswith("|"):
            row = lines[i].strip().strip("|")
            cells = [c.strip() for c in row.split("|")]
            if cells and all(c and set(c) <= set("-:") for c in cells):
                pass
            else:
                joined = " ".join(c for c in cells if c)
                if joined:
                    out.append(joined)
            i += 1
        out.append("")
    else:
        out.append(ln)
        i += 1
txt = "\n".join(out)

# ---------- 2) capa ----------
rep("#### BEN WITHERINGTON HI\n\n### Vabd. Cu\n\nii Ê\n\n# | f et\n\n"
    "#### | e HISÍÓrIAS Go } À NOVOTESTAMENTO\n\n"
    "##### k Lucília Marques Pereira da Silva\n\nt\n\nCopyright O 2004",
    "# A HISTÓRIA DO NOVO TESTAMENTO\n\n*Ben Witherington III*\n\n"
    "Lucília Marques Pereira da Silva\n\nCopyright © 2004", "capa")

rep('##### 1." edição: 2005', "1.a edição: 2005", "edicao")
txt = txt.replace("2.o edição", "2.a edição").replace("1.4 edição", "1.a edição")
txt = txt.replace("REVISAO", "REVISÃO").replace("O 1995", "© 1995")

# ---------- 3) cabeçalhos correntes (linhas exatas) ----------
HEADERS = {
    "A HISTÓRIA DO NOVO TESTAMENTO",
    "PEDAGOG VIXNAOS DITOS DE JESUS E HISTORIAS DA PAIXÃO",
    "“A HISTORIA DO NOVO TESTAMENTO",
    "e PEDAGOGIA E PAIXÃO: DITOS DE JESUS E HISTORIAS DA PAIXÃO & 4]",
    "PEDAGOGIA E PAIXAO: DITOS DE JESUS E HISTÓRIAS DA PAIXÃO +3",
    "A HISTÓRIA DO NOVO FESTAMENTO",
    "PEDAGOGIA É PAIXÃO: DITOS DE JESUS E HISTÓRIAS DA PAIXÃO “É 45",
    "PEDAGOGIA É PAIXAO: OS DE JESUS E HISTÓRIAS DA PAIXÃO",
    "PEDAGOGIA E PAIXÃO: DITOS DE JESUS E HISTÓRIAS DA PAIXÃO *",
    "PEDAGOGIA E PAIXÃO; DITOS DE JESUS E HISTÓRIAS DA PAIXÃO % 51",
    "S2 + A HISTÓRIA DO NOVO TESTAMENTO",
    "PEDAGOGIA E PAIXÃO: DITOS DE JESUS E HISTÓRIAS DA PAIXÃO 4o 53",
}
n0 = len(txt.split("\n"))
txt = "\n".join(l for l in txt.split("\n") if l.strip() not in HEADERS)
print(f"cabeçalhos removidos: {n0 - len(txt.split(chr(10)))}")

# ---------- 4) títulos de seção ----------
rep("#### Pedagogia e Paixão: ditos de Jesus e Histórias da Paixão",
    "## Pedagogia e Paixão: ditos de Jesus e Histórias da Paixão", "titulo cap")
rep("##### VAMOS DIRETO A Q: OS DITOS DE JESUS",
    "## VAMOS DIRETO A Q: OS DITOS DE JESUS", "sec Q")
rep("##### A PAIXÃO E A GLÓRIA", "## A PAIXÃO E A GLÓRIA", "sec paixao")
rep("\nCONCLUSÕES\n", "\n## CONCLUSÕES\n", "sec conclusoes")
rep("##### EXERCÍCIOS E QUESTÕES PARA ESTUDO E REFLEXÃO",
    "## EXERCÍCIOS E QUESTÕES PARA ESTUDO E REFLEXÃO", "sec exerc")
rep("##### c. Autoridade dos missionários",
    "c. Autoridade dos missionários", "item c")

# ---------- 5) notas de rodapé ----------
rep("| Uma abreviatura da palavra alemã Quelle",
    "1 Uma abreviatura da palavra alemã Quelle", "fn1")
rep("2V. p. 44-7. *V. meu livro Jesus the Sage",
    "2 V. p. 44-7.\n\n3 V. meu livro Jesus the Sage", "fn2-3")
rep("' Essa tabela aparece", "4 Essa tabela aparece", "fn4")
rep("* Seguimos a posição convencional", "5 Seguimos a posição convencional", "fn5")
rep("preserva a ordem\nde Q. Também", "preserva a ordem de Q. Também", "fn5 join")
rep("$V., de G. N. STANTON", "6 V., de G. N. STANTON", "fn6")
txt = txt.replace("Linpars", "Lindars")

rep("traz juntas as parábolas\n\n* Estou sugerindo que, talvez antes da "
    "composição de Q, o qual também\nda ovelha perdida e da dracma perdida, "
    "segundo a semelhança de suas temáticas. uma coletânea de parábolas "
    "agrupadas\n\npoderia ter existido",
    "8 Estou sugerindo que, talvez antes da composição de Q, o qual também "
    "traz juntas as parábolas da ovelha perdida e da dracma perdida, segundo "
    "a semelhança de suas temáticas, poderia ter existido uma coletânea de "
    "parábolas agrupadas.", "fn8")

rep("?V. o levantamento feito por J. B. GREEN no verbete “Passion Narrative”. "
    "In: The Dictionary of Jesus\nand the Gospels, editado por Joel B. Green e "
    "Scot McKnight p. 601-4. 'o Essa última hipótese é defendida na obra "
    "magistral de R. Brown, Grove, The Death of the Messiah, 2 vols. Ill.: "
    "InterVarsity, 1992),\n\n(New York:\n\n(Downers\n\nDoubleday, 1994).",
    "9 V. o levantamento feito por J. B. GREEN no verbete “Passion Narrative”. "
    "In: The Dictionary of Jesus and the Gospels, editado por Joel B. Green e "
    "Scot McKnight (Downers Grove, Ill.: InterVarsity, 1992), p. 601-4.\n\n"
    "10 Essa última hipótese é defendida na obra magistral de R. Brown, The "
    "Death of the Messiah, 2 vols. (New York: Doubleday, 1994).", "fn9-10")

rep("##### 1 V., de GREEN, “Passion Narrative”, p. 602-3.",
    "11 V., de GREEN, “Passion Narrative”, p. 602-3.", "fn11")

# marcadores no texto
rep("denominada Q,' precisamos", "denominada Q,¹ precisamos", "mk1")
rep("existência de Q.- A grande", "existência de Q.² A grande", "mk2")
rep("sabedoria de Deus.' Aliás", "sabedoria de Deus.² Aliás", "mk2b")
rep("sabedoria de Deus.” Isso", "sabedoria de Deus.³ Isso", "mk3")
rep("discurso escatológico.” É nesse", "discurso escatológico.⁴ É nesse", "mk4")
rep("do termo”. Q também", "do termo⁷. Q também", "mk7")
rep("tenha ocorrido? ou, pelo menos", "tenha ocorrido⁹ ou, pelo menos", "mk9")
rep("narrativa da Paixão.” De fato", "narrativa da Paixão.¹⁰ De fato", "mk10")

# ---------- 6) legenda da foto ----------
rep("As s atuais at ruínas d da sinagoga goga de de Caf. Cafarnaum datam do do t "
    "terceiro século\nparecem ser da época da sinagoga do primeiro século, onde "
    "as palavras de Jesus foram ouvidas.\n\néculo d de nossa era, mas suas "
    "fundaç fundações",
    "*As atuais ruínas da sinagoga de Cafarnaum datam do terceiro século de "
    "nossa era, mas suas fundações parecem ser da época da sinagoga do "
    "primeiro século, onde as palavras de Jesus foram ouvidas.*", "legenda")

# ---------- 7) tabela de Q: numeração ----------
rep("1. O precursor e o anúncio da vinda do sábio (por Joao) — Lc 3.2-9/Mt\n\n"
    "3.1-10; Le 3.15-17/Mt 3.11-12",
    "1. O precursor e o anúncio da vinda do sábio (por João) — Lc 3.2-9/Mt "
    "3.1-10; Lc 3.15-17/Mt 3.11-12", "Q1")
rep("fo A unção do sábio com o Espírito — Lc 3.21-22/Mt 3.13-16 A tentação do "
    "sábio — Lc 4.1-13/Mt 4.1-11 eSO sermão do sábio — Lc 6.20-49/Mt 5—7 A "
    "maravilhosa operação do sábio — Lc 7.1-10/Mt 8.5-13 O questionamento do "
    "sábio (por João) — Lc 7.18-23/Mt 11.2-6 A resposta do sábio — Lc "
    "7.24-28/Mt 11.7-11 SNe A rejeição ao sábio por “esta geração” — Lc "
    "7.31-35/Mt 11.16-19",
    "2. A unção do sábio com o Espírito — Lc 3.21-22/Mt 3.13-16\n"
    "3. A tentação do sábio — Lc 4.1-13/Mt 4.1-11\n"
    "4. O sermão do sábio — Lc 6.20-49/Mt 5—7\n"
    "5. A maravilhosa operação do sábio — Lc 7.1-10/Mt 8.5-13\n"
    "6. O questionamento do sábio (por João) — Lc 7.18-23/Mt 11.2-6\n"
    "7. A resposta do sábio — Lc 7.24-28/Mt 11.7-11\n"
    "8. A rejeição ao sábio por “esta geração” — Lc 7.31-35/Mt 11.16-19", "Q2-8")
rep("11. A oração do discípulo e uma ilustração sobre a oração — Lc 11.2-4; 5- "
    "13/Mt 6.7-13; 7.7-11 A parte dois termina",
    "11. A oração do discípulo e uma ilustração sobre a oração — Lc 11.2-4; "
    "5-13/Mt 6.7-13; 7.7-11\n\nA parte dois termina", "Q11")
rep("20. Os tesouros da sabedoria — Le 12.32-34/Mt 6.19-21 PAR A preparação "
    "para o banquete da sabedoria — Le 12.35-40/Mt 24.43, 44",
    "20. Os tesouros da sabedoria — Lc 12.32-34/Mt 6.19-21\n21. A preparação "
    "para o banquete da sabedoria — Lc 12.35-40/Mt 24.43, 44", "Q20-21")
rep("23. O segundo batismo da sabedoria — Lc 12.49, 50 24, Divisões por causa "
    "da sabedoria e seu legado — Lc 12.51-53/Mt 10.34-36 ds Sinais de desgraça "
    "(2) — Lc 12.54-56/Mt 16.2, 3",
    "23. O segundo batismo da sabedoria — Lc 12.49, 50\n24. Divisões por causa "
    "da sabedoria e seu legado — Lc 12.51-53/Mt 10.34-36\n25. Sinais de "
    "desgraça (2) — Lc 12.54-56/Mt 16.2, 3", "Q23-25")
rep("28. Semente e fermento — Lc 13.18-21/Mt 13.31-33 2, Porta e caminho — Lc "
    "13.23-27/Mt 7.13, 14, 22, 23",
    "28. Semente e fermento — Lc 13.18-21/Mt 13.31-33\n29. Porta e caminho — "
    "Lc 13.23-27/Mt 7.13, 14, 22, 23", "Q28-29")
rep("30. Oriente e ocidente/Primeiro e ultimo — Lc 13.28-30/Mt 8.11, 12;\n\n"
    "20.16",
    "30. Oriente e ocidente/Primeiro e último — Lc 13.28-30/Mt 8.11, 12; 20.16",
    "Q30")
rep("31. O banquete da sabedoria — Lc 14.15-24/Mt 22.1-10 S23 O preço do "
    "discipulado — Lc 14.25-27/Mt 10.37, 38 Do. Sal insípido — Le 14.34, "
    "35/Mt 5.13",
    "31. O banquete da sabedoria — Lc 14.15-24/Mt 22.1-10\n32. O preço do "
    "discipulado — Lc 14.25-27/Mt 10.37, 38\n33. Sal insípido — Lc 14.34, "
    "35/Mt 5.13", "Q31-33")
rep("41. Contra falsas esperanças — Lc 17.22, 23/Mt\n"
    "42. Como um relâmpago — Lc 17.24/Mt\n"
    "43. Como aburres — Le 17.37/Mt 24.28\n\n24.26\n\n24.27",
    "41. Contra falsas esperanças — Lc 17.22, 23/Mt 24.26\n"
    "42. Como um relâmpago — Lc 17.24/Mt 24.27\n"
    "43. Como abutres — Lc 17.37/Mt 24.28", "Q41-43")

# ---------- 8) colapso e junções de quebra de página ----------
txt = re.sub(r"\n{3,}", "\n\n", txt)
JOINS = [
    ("um assunto\n\nconhecido como “problema sinótico”", "um assunto conhecido como “problema sinótico”"),
    ("contar as\n\nparábolas de Jesus,", "contar as parábolas de Jesus,"),
    ("listados de Mateus\n\ne Lucas para notar", "listados de Mateus e Lucas para notar"),
    ("Esse retrato\n\nparece ser um tanto atenuado", "Esse retrato parece ser um tanto atenuado"),
    ("da Paixão que\n\nnão podem ser explicados", "da Paixão que não podem ser explicados"),
    ("observe como começa\n\na história:", "observe como começa a história:"),
    ("conhece uma\n\nnarrativa da história das últimas", "conhece uma narrativa da história das últimas"),
    ("a execução\n\npor crucificação e o sepultamento.", "a execução por crucificação e o sepultamento."),
    ("Teófilo e,\n\nde fato, provavelmente", "Teófilo e, de fato, provavelmente"),
    ("importância histórica\n\ne é baseado em acontecimentos históricos.", "importância histórica e é baseado em acontecimentos históricos."),
    ("não era necessário que esse\n\nsumário da história", "não era necessário que esse sumário da história"),
    ("no rolo de Qumran\n\n11QMelquisedeque,", "no rolo de Qumran 11QMelquisedeque,"),
]
for j, (o, n) in enumerate(JOINS):
    rep(o, n, f"join{j}")

# ---------- 9) normalizações finais ----------
txt = txt.replace("— Le ", "— Lc ")
txt = txt.replace("(Mr 19.17)", "(Mt 19.17)").replace("Mtr ", "Mt ")
txt = txt.replace("quando cle vier", "quando ele vier")
txt = txt.replace("spsis litteris", "ipsis litteris")
txt = txt.replace(" ¢ ", " e ")
txt = txt.replace("À, C, D e E", "A, C, D e E")
txt = txt.replace("o capítulo anterior, descrevemos", "No capítulo anterior, descrevemos")
txt = txt.replace("E claro que o conteúdo", "É claro que o conteúdo")
txt = txt.replace("E exatamente essa combinação", "É exatamente essa combinação")
txt = txt.replace("À leitura do material de Q", "A leitura do material de Q")
txt = txt.replace("e Pegue duas Bíblias", "Pegue duas Bíblias")
# hifenização de quebra de linha dentro do parágrafo
txt = re.sub(r"(?u)([a-zçá-úâ-ûã-õ])-\s+(?=[a-zçá-úâ-ûã-õ])", r"\1", txt)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print("--- HEADINGS ---")
for h in txt.split("\n"):
    if h.startswith("#"):
        print(" ", h)
resto = [ln for ln in txt.split("\n") if ln.startswith("|")]
print("linhas pipe restantes:", len(resto))
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
