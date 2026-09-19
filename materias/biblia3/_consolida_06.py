# -*- coding: utf-8 -*-
"""Consolida 06-Witherington_Evangelhos.md — cap. 4 'Tudo o que valia a pena
registrar sobre As boas novas' de 'A História do Novo Testamento'."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, 1)

# ---------- capa ----------
rep("#### BEN WITHERINGTON HI\n\n### Vabd. Cu\n\nii Ê\n\n# | f et\n\n"
    "#### | e HISÍÓrIAS Go } À NOVOTESTAMENTO\n\n"
    "##### k Lucília Marques Pereira da Silva\n\nt\n\nCopyright O 2004",
    "# A HISTÓRIA DO NOVO TESTAMENTO\n\n*Ben Witherington III*\n\n"
    "Lucília Marques Pereira da Silva\n\nCopyright © 2004", "capa")
rep('##### 1." edição: 2005', "1.a edição: 2005", "edicao")
txt = txt.replace("2.o edição", "2.a edição").replace("1.4 edição", "1.a edição")
txt = txt.replace("REVISAO", "REVISÃO")
txt = txt.replace("O 1995", "© 1995").replace("O 2005", "© 2005")

# ---------- cabeçalhos correntes ----------
HEADERS = {
    "E, STORIA DO NO TES L\\MEN FO",
    "A HISTÓRIA DO NOVO TESTAMENTO",
    "DO O QUE VALIA A PENA REGIS OBRE AS BOAS NOVA",
    "TUDO O QUE VALIA A PENA REGISTRAR SOBRE AS BOAS NOVAS “:* 8]",
    "PUD O QUE VALIA A PENA REGISTRAR SOBRE AS BOAS NOVAS",
    "“A HISTÓRIA DO NOVO TESTAMENTO",
    "FUDO O QUE VALIA A PENA REGISTRAR SOBRE AS BOAS NOVAS % 85",
}
txt = "\n".join(l for l in txt.split("\n") if l.strip() not in HEADERS)
rep("##### CV p 722\n", "", "mobilia pagina")

# ---------- títulos ----------
rep("#### 4, Tudo o que valia a pena registrar sobre As boas novas",
    "## 4. Tudo o que valia a pena registrar sobre As boas novas", "titulo cap")
rep("\nMARCOS\n", "\n## MARCOS\n", "sec marcos")
rep("##### Lucas— ATOS", "## Lucas—Atos", "sec lucas")
rep("JoÃo", "## João", "sec joao")
rep("MATEUS O evangelho de Mateus é uma combinação",
    "## MATEUS\n\nO evangelho de Mateus é uma combinação", "sec mateus")

# ---------- notas 1-4 ----------
rep("em forma impressa.' Isso levanta", "em forma impressa.¹ Isso levanta", "mk1")
rep("incluindo Q,* mas também", "incluindo Q, mas também", "mk4a")
rep("Mas, o que O Didaquê mostra uma familiaridade especial com Mateus, mas o "
    "autor parece conhecer também outros evangelhos. 2V. p. 37-42. >V. p. 39-48.",
    "Mas, o que⁴\n\n2 V. p. 37-42.\n\n3 V. p. 39-48.\n\n4 O Didaquê mostra uma "
    "familiaridade especial com Mateus, mas o autor parece conhecer também "
    "outros evangelhos.", "fn1-4")

# ---------- nota 5 ----------
rep("de forma seletiva.”", "de forma seletiva.⁵", "mk5")
rep("* Sobre o assunto a seguir, v. meu livro The Gospel of Mark: A "
    "Socio-Rhetorical Commentary\n(Grand Rapids: Ecrdmans, 2001), p. Iss.",
    "5 Sobre o assunto a seguir, v. meu livro The Gospel of Mark: A "
    "Socio-Rhetorical Commentary (Grand Rapids: Eerdmans, 2001), p. 155.", "fn5")

# ---------- notas 6-7 (extrai do meio da frase e reinser depois) ----------
rep("no período de 68-69,o quando", "no período de 68-69,⁶ quando", "mk6")
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
rep("* Leon L. Morris, especialista em NT, considera a data de 68 d.C para a "
    "composição do evangelho\nde Marcos muito tardia (Lucas: introdução e "
    "comentário [São Paulo: Vida Nova, 1983; reimp. 1996]). Aceitando-se a "
    "hipótese de Marcos ter sido o primeiro evangelho e de ter sido usado como "
    "fonte por Mateus e Lucas, a aceitação dessa data tardia estenderia para "
    "depois do ano 70 a composição desses dois evangelhos, o que invibializaria "
    "o caráter profético dos discursos de Jesus sobre a destruição de Jerusálem "
    "(v. Mt 24; Lc 21), ocorrida em 70. d.C. Portanto, se Mateus e Lucas contêm "
    "discursos genuinamente proféticos, isso quer dizer que foram escritos "
    "antes de 70, o que retrocederia a datação de Marcos para o Início da "
    "década de 60. (N. do E.) $V. meu livro Gospel of Mark, p. 1-62.",
    "@@FN67@@", "fn6-7 extrai")
rep("precisou depender tanto\n\n@@FN67@@\n\nde um evangelho",
    "precisou depender tanto de um evangelho", "j6")
rep("em todos os quatro evangelhos, inclusive no primeiro.\n\nEm todo caso,",
    "em todos os quatro evangelhos, inclusive no primeiro.\n\n" + FN6 +
    "\n\n7 V. meu livro Gospel of Mark, p. 1-62.\n\nEm todo caso,", "fn6-7 insere")

# ---------- notas 8-9 ----------
rep("entre as décadas de 70 e 80 do primeiro século.”", 
    "entre as décadas de 70 e 80 do primeiro século.⁸", "mk8")
rep("a própria mente e presença de Deus na terra.”",
    "a própria mente e presença de Deus na terra.⁹", "mk9")
rep("” Sobre essa datação, v. a nota n. 5. o V, meu livro Jesus the Sage: The "
    "Pilgrimage of Wisdom (Minneapolis: Augsburg/Fortress, 1994),\n\np. 348-68, "
    "e The Gospel of Mattew (Macon: Smyth and Helwys, no prelo).",
    "8 Sobre essa datação, v. a nota n. 5.\n\n9 V. meu livro Jesus the Sage: "
    "The Pilgrimage of Wisdom (Minneapolis: Augsburg/Fortress, 1994), "
    "p. 348-68, e The Gospel of Matthew (Macon: Smyth and Helwys, no prelo).",
    "fn8-9")

# ---------- notas 10-11 ----------
rep("região por regiao.'°", "região por região.¹⁰", "mk10")
rep("'°'V. minha discussão em The Acts of the Apostles: A Socio-Rhetorical "
    "Commentary (Grand Rapids: Eerdmans, 1998), p. 1-101.",
    "10 V. minha discussão em The Acts of the Apostles: A Socio-Rhetorical "
    "Commentary (Grand Rapids: Eerdmans, 1998), p. 1-101.", "fn10")
rep("patrono de Lucas.''", "patrono de Lucas.¹¹", "mk11")
rep("como a obra de\n\nUV. p. 19-22.\n\nLucas, ao enfatizar",
    "como a obra de Lucas, ao enfatizar", "j11")
rep("suas implicações políticas.\n\n## João",
    "suas implicações políticas.\n\n11 V. p. 19-22.\n\n## João", "fn11 insere")

# ---------- notas 12-13 ----------
rep("em relação a Jesus e seus ensi- namentos.'?", 
    "em relação a Jesus e seus ensinamentos.¹²", "mk12")
rep("em fontes como a Sabedoria de Salomão. '*",
    "em fontes como a Sabedoria de Salomão.¹³", "mk13")
rep("'2 Sobre esse assunto, v. meu livro Johns Wisdom: A Commentary on the "
    "Fourth Gospel (Louisville: Westminster/John Knox, 1995). “ Também "
    "conhecida por Livro da Sabedoria, essa obra é considerada apocrifa, isto "
    "é, não inspirada, na teologia protestante. A Igreja Católica Romana, em "
    "contrapartida, considera seu conteúdo inspirado por Deus. Para mais "
    "informações, v. o verbete Livros arocriFos do Dicionário Ilustrado da "
    "Biblia (São Paulo: Vida Nova, 2004), p. 868. (N. do E.)",
    "12 Sobre esse assunto, v. meu livro John's Wisdom: A Commentary on the "
    "Fourth Gospel (Louisville: Westminster/John Knox, 1995).\n\n13 Também "
    "conhecida por Livro da Sabedoria, essa obra é considerada apócrifa, isto "
    "é, não inspirada, na teologia protestante. A Igreja Católica Romana, em "
    "contrapartida, considera seu conteúdo inspirado por Deus. Para mais "
    "informações, v. o verbete Livros Apócrifos do Dicionário Ilustrado da "
    "Bíblia (São Paulo: Vida Nova, 2004), p. 868. (N. do E.)", "fn12-13")

# ---------- junções de quebra de página ----------
txt = re.sub(r"\n{3,}", "\n\n", txt)
JOINS = [
    ("biográficas\n\nda época, com a diferença", "biográficas da época, com a diferença"),
    ("chamados evangelhos no Didaqué (8.2; 11.3;\n\n15.3, 4).", "chamados evangelhos no Didaqué (8.2; 11.3; 15.3, 4)."),
    ("o jovem citado\n\nrapidamente na narrativa", "o jovem citado rapidamente na narrativa"),
    ("descrito em Marcos\n\n14.51, 52,", "descrito em Marcos 14.51, 52,"),
    ("Lucas, que tem\n\n19.428 palavras", "Lucas, que tem 19.428 palavras"),
    ("sua obra. Para os antigos", "sua obra. Para os antigos"),
]
for j, (o, n) in enumerate(JOINS):
    rep(o, n, f"join{j}")

# ---------- normalizações ----------
for o, n in [
    ("4. termo “evangelho” vem", "O termo “evangelho” vem"),
    ("significa ( | “novidades”.", "significa “novidades”."),
    ("“ Z que significa “boa nova”", "que significa “boa nova”"),
    ("da era cristá e circulavam", "da era cristã e circulavam"),
    ("O que sao os evangelhos?", "O que são os evangelhos?"),
    ("À tradição romana, que entrou em cena", "A tradição romana, que entrou em cena"),
    ("priincipalmente", "principalmente"),
    ("pouco antes de seu climax", "pouco antes de seu clímax"),
    ("E provável que o evangelho de Mateus", "É provável que o evangelho de Mateus"),
    ("um homem ins- truído.”", "um homem instruído."),
    ("ele agia c falava", "ele agia e falava"),
    ("Isafas", "Isaías"),
]:
    txt = txt.replace(o, n)
# hifenização
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
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
