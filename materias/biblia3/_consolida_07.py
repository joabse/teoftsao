# -*- coding: utf-8 -*-
"""Consolida 07-Witherington_Cartas.md — cap. 5 'Cartas e homilias para os
convertidos' de 'A História do Novo Testamento' (Ben Witherington III)."""
from pathlib import Path
import re

P = Path(r"01_markdown\adicionais\07-Witherington_Cartas.md")
txt = P.read_text(encoding="utf-8")
erros = []

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}")
        return
    txt = txt.replace(old, new, 1)

# ============ 1. REMOÇÃO DE LINHAS-ESTRUTURA ============
Q = r"[“”\"'’‘*°o]"

def is_header(s):
    t = s.strip()
    if t.startswith("#") or t.startswith("|"):
        return False
    if re.match(rf"^.{{0,12}}CARTAS\s+[ÉE]?\s*HOM[EL]LIAS\s+PARA\s+OS\s+CONVER", t):
        return True
    if re.match(r"^CA\s+HOMILIAS\s+PARA\s+OS\s+CONVERTIDOS", t):
        return True
    if re.search(r"HIST[OÓ]RIA\s+DO\s+NOVO\s+[FT]ESTAMENTO", t) and len(t) < 80:
        return True
    return False

DROP = [
    rf"^{Q}\s*Observe como Paulo fala pouco",                                   # 112 (fn7+8)
    rf"^p\. 132-9\.$",                                                          # 114
    rf"^\* Sobre isso, v\. p\. 65-7\.",                                         # 120 (fn9)
    rf"^Society in the Book of Acts,",                                          # 121 (fn10)
    rf"^1996\), p\. 154-84\.$",                                                 # 123
    rf"^{Q}\s*R\.?J\. Bauck",                                                   # 129 (fn11)
    rf"^{Q}V\., p\. ex\., de C\. WANAMAKER",                                    # 154 (fn12)
    rf"^3 V\. minha discussão desses assuntos em Conflict",                     # 167 (fn13)
    rf"^{Q}\s*Existe uma hipótese de que Paulo escreveu essas cartas em Cesaréia",  # 212 (fn15)
    rf"^{Q}\??\s*Estudiosos de renome, como J\. N\. D\. RELLY",                 # 246 (fn19)
    rf"^2001\)\. \[Em português, o leitor pode consultar as seguintes publicações",  # 50 (fn1)
    rf"^do E\.?\)$",                                                            # 63
    rf"^Life\. Oxford:$",                                                       # 73
    rf"^A Commentary on St\. Paul'?s Letter to the$",                           # 100
    rf"^nessa encontrada de Corinto\. o seguinte:$",                            # 163 (box1)
    rf"^foi lá que ele$",                                                       # 173 (box2)
    rf"^conheceu Erasto, que devia estar coletando impostos como tesoureiro da cidade\. É provável que$",  # 179
    rf"^Account \(Grand Rapids:$",                                              # 227 (fn16/17)
    rf"^1983\),$",                                                              # 229
    rf"^L\. T\. Johnson$",                                                      # 256 (fn20)
    rf"^de que 2Timóteo$",                                                      # 262
]

linhas = txt.split("\n")
linhas = [l for l in linhas if not is_header(l)]
linhas = [l for l in linhas if not l.strip().startswith("|")]
linhas = [l for l in linhas if not any(re.match(p, l.strip()) for p in DROP)]
txt = "\n".join(linhas)
txt = re.sub(r"\n{3,}", "\n\n", txt)

# fn18 estava embutida no fim da linha do corpo (p. 71)
txt, n = re.subn(r"\s*.{0,4}V\. meu artigo “The Influence of Galatians on Hebrews”, New Testament Studies 37 \(1991\): 146-52\.", "", txt, count=1)
if n == 0:
    erros.append("[NAO ENCONTRADO] fn18 inline")

# ============ 2. CAPA E TÍTULOS ============
rep("#### BEN WITHERINGTON HI\n\n### Vabd. Cu\n\nii Ê\n\n# | f et\n\n"
    "#### | e HISÍÓrIAS Go } À NOVOTESTAMENTO\n\n##### k Lucília Marques Pereira da Silva\n\nt",
    "# A HISTÓRIA DO NOVO TESTAMENTO\n\n*Ben Witherington III*\n\n"
    "Lucília Marques Pereira da Silva", "capa")
rep("Copyright O 2004 Wm. B. Eerdmans Publishing Co.",
    "Copyright © 2004 Wm. B. Eerdmans Publishing Co.", "copyright")
rep("— 2.o edição — 1995 O 1995 Sociedade Bíblica do Brasil",
    "— 2.a edição — 1995 © 1995 Sociedade Bíblica do Brasil", "edicao-ara")
rep("— 1.4 edição — 2005 O 2005 Sociedade Religiosa",
    "— 1.a edição — 2005 © 2005 Sociedade Religiosa", "edicao-as21")
rep('##### 1." edição: 2005', "1.a edição: 2005", "edicao-2005")
rep("#### Py Cartas e Homilias para * os convertidos",
    "## 5. Cartas e homilias para os convertidos", "titulo cap")
rep("». Ss mais antigos textos canônicos de que dispomos são as cartas de Paulo.' | Elas são anteriores",
    "Os mais antigos textos canônicos de que dispomos são as cartas de Paulo.¹ Elas são anteriores", "abertura")
rep("#### \\ J provavelmente, aos próprios evangelhos",
    "provavelmente, aos próprios evangelhos", "dropcap p2")

# ============ 3. SEÇÕES ============
rep("##### GALATAS — A PRIMEIRA CARTA CRISTÃ EXISTENTE",
    "## Gálatas — a primeira carta cristã existente", "sec galatas")
rep("##### AS CARTAS DE TIAGO", "## As cartas de Tiago", "sec tiago")
rep("JUDAS\n\nO serviço também estava", "## Judas\n\nO serviço também estava", "sec judas")
rep("##### 1 E 2 TESSALONICENSES", "## 1 e 2 Tessalonicenses", "sec tess")
rep("##### 1 E 2CoRÍNTIOS", "## 1 e 2 Coríntios", "sec cor")
rep("ROMANOS\n\nA carta aos cristãos romanos", "## Romanos\n\nA carta aos cristãos romanos", "sec rom")
rep("##### FILIPENSES, FILEMOM, COLOSSENSES, EFESIOS",
    "## Filipenses, Filemom, Colossenses, Efésios", "sec prisao")
rep("##### | PEDRO", "## 1 e 2 Pedro", "sec pedro")
rep("nos gentios. HEBREUS A procedência desse documento é difícil",
    "nos gentios.\n\n## Hebreus\n\nA procedência desse documento é difícil", "sec hebreus")
rep("##### AS EPÍSTOLAS PASTORAIS", "## As epístolas pastorais", "sec pastorais")
rep("CONCLUSÕES\n\nJá deve ter ficado claro", "## Conclusões\n\nJá deve ter ficado claro", "sec conclusao")
rep("##### EXERCICIOS E QUESTÕES PARA ESTUDO E REFLEXÃO",
    "## Exercícios e questões para estudo e reflexão", "sec exercicios")

# ============ 4. NOTAS DE RODAPÉ ============
FN1 = ("1 Existem várias obras, em inglês, que abordam integralmente as questões pertinentes à "
       "introdução ao NT. Três dos melhores trabalhos nessa área são: Introducing the New Testament: "
       "Its Literature and Theology, de P. J. ACHTEMEIER, J. B. GREEN e M. M. THOMPSON (Grand Rapids: "
       "Eerdmans, 2001); The Writings of the New Testament, de L. T. JOHNSON (Minneapolis: Fortress, "
       "1999); e An Introduction to the New Testament, de R. E. Brown (New York: Doubleday, 1997). "
       "Em nível mais popular, porém mais detalhado do que este estudo, v. Introducing the New "
       "Testament, de J. DRANE (Minneapolis: Fortress, 2001). [Em português, o leitor pode consultar "
       "as seguintes publicações: Teologia do Novo Testamento, de Leon Morris (São Paulo: Vida Nova, "
       "2003); Introdução ao Novo Testamento, de D. A. Carson, Douglas J. Moo e Leon Morris (São "
       "Paulo: Vida Nova, 1997); Merece Confiança o Novo Testamento, de F. F. BRUCE, 3. ed. (São "
       "Paulo: Vida Nova, 1984; reimp. 1998); Panorama do Novo Testamento, de Robert H. GUNDRY, 2. ed. "
       "(São Paulo: Vida Nova, 1998); Teologia bíblica ou teologia sistemática? Unidade e diversidade "
       "no Novo Testamento, de D. A. Carson (São Paulo: Vida Nova, 2001).]")
rep("são as cartas de Paulo.¹ Elas são anteriores não só a obras como Atos e Apocalipse, mas também,",
    "são as cartas de Paulo.¹\n\n" + FN1 + "\n\nElas são anteriores não só a obras como Atos e "
    "Apocalipse, mas também,", "fn1 insere")

rep("Um autor’ cristão posterior diz o seguinte:", "Um autor² cristão posterior diz o seguinte:", "mk2")
rep("no local de destino e na congregação.” Isso vale",
    "no local de destino e na congregação.³\n\n2 O autor deste livro não defende a autoria petrina "
    "de 2Pedro, embora tradicionalmente essa carta seja atribuída ao apóstolo Pedro. (N. do E.)\n\n"
    "3 Antigamente, sozinho (v. At 8.30), quase todas as leituras eram feitas em voz alta, mesmo "
    "quando o leitor estava só.\n\nIsso vale", "fn2-3")

rep("intocados”.* Paulo tinha", "intocados”.⁴\n\n4 The Social Pattern of Christian Groups in the "
    "First Century. Londres: Tyndale, 1960, p. 52, 60.\n\nPaulo tinha", "fn4")
rep("redação de discursos”.? Paulo manifesta",
    "redação de discursos”.⁵\n\n5 Paul: A Critical Life. Oxford: Oxford University Press, 1996, "
    "p. 50. [Publicado no Brasil sob o título Paulo: biografia crítica (São Paulo: Loyola, 2000).]"
    "\n\nPaulo manifesta", "fn5")

rep("que ocorreu no ano 50.o Não temos", "que ocorreu no ano 50.⁶ Não temos", "mk6")
rep("então Cristo morreu inutilmente.\n\nPaulo parece estar preocupado",
    "então Cristo morreu inutilmente.\n\n6 V. a discussão extensa em meu livro Grace in Galatia: A "
    "Commentary on St. Paul's Letter to the Galatians (Grand Rapids: Eerdmans, 1998), p. 8-48."
    "\n\nPaulo parece estar preocupado", "fn6")

rep("onde os rituais têm papel secundário.” O tema do comportamento",
    "onde os rituais têm papel secundário.⁷\n\n7 Observe como Paulo fala pouco sobre o batismo "
    "nessa carta e como ele enfatiza a vida no Espírito (cf. Gl 3 e 5).\n\nO tema do comportamento",
    "fn7")
rep("idolatria associadas àqueles locais.” A carta reconhece",
    "idolatria associadas àqueles locais.⁸\n\n8 V. o livro The Brother of Jesus: The Dramatic Story "
    "and Meaning of the First Archaeological Link to Jesus and His Family, que escrevi juntamente "
    "com H. SHANKS (San Francisco: HarperCollins, 2003), p. 132-9.\n\nA carta reconhece", "fn8")

rep("bem como na Galicia.’ A outra (e mais conhecida)",
    "bem como na Galácia.⁹\n\n9 Sobre isso, v. p. 65-67.\n\nA outra (e mais conhecida)", "fn9")
rep("ter usado o mesmo expediente.\" Mas será que Tiago",
    "ter usado o mesmo expediente.¹⁰\n\n10 V., de R. J. BAUCKHAM, “James and the Gentiles "
    "(Acts 15.13-21)”. In: History, Literature, and Society in the Book of Acts, organizado por "
    "B. WITHERINGTON (Cambridge: Cambridge University Press, 1996), p. 154-84.\n\nMas será que Tiago",
    "fn10")
rep("a Israel como um todo.”!! Essa carta parece",
    "a Israel como um todo.¹¹\n\n11 R. J. Bauckham, James: Wisdom of James, Disciple of Jesus the "
    "Sage. London: Routledge, 1999, p. 16.\n\nEssa carta parece", "fn11")

rep("2 Tessalonicenses ser pós-paulina são fracos.'? Em primeiro lugar",
    "2 Tessalonicenses ser pós-paulina são fracos.¹²\n\n12 V., p. ex., de C. WANAMAKER, 1 and 2 "
    "Thessalonians (Grand Rapids: Eerdmans, 1990).\n\nEm primeiro lugar", "fn12")

rep("ou de classes sociais.” Paulo, então, decide",
    "ou de classes sociais.¹³\n\n13 V. minha discussão desses assuntos em Conflict and Community "
    "in Corinth: A Socio-Rhetorical Commentary on 1 and 2 Corinthians (Grand Rapids: Eerdmans, "
    "1995), p. 155.\n\nPaulo, então, decide", "fn13")

rep("por volta de 56 ou\n\n57. Ao contrário das cartas paulinas anteriores",
    "por volta de 56 ou 57.¹⁴\n\n14 Sobre essa carta, v. a obra que Darlene Hyatt e eu escrevemos "
    "em The Epistle to the Romans (Grand Rapids: Eerdmans, 2003), p. 155.\n\nAo contrário das "
    "cartas paulinas anteriores", "fn14")

rep("durante o período de 60-62.\" Talvez haja algum tipo de relação literária",
    "durante o período de 60-62.¹⁵\n\n15 Existe uma hipótese de que Paulo escreveu essas cartas em "
    "Cesaréia Marítima, quando esteve em prisão domiciliar naquela cidade. Essas cartas da prisão, "
    "porém, transmitem uma atmosfera de perigo que não combina com a situação de Paulo em Cesaréia. "
    "Sendo cidadão romano, ele sempre podia apelar a César, se não gostasse do modo como as coisas "
    "estavam indo em Cesaréia. É mais provável que essas cartas tenham sido escritas num local onde "
    "o caso de Paulo seria resolvido, de um modo ou de outro.\n\nTalvez haja algum tipo de relação "
    "literária", "fn15")

rep("quer com sua soltura.'é Essas cartas apresentam temas em comum",
    "quer com sua soltura.¹⁶\n\n16 V. a discussão no livro que escrevi com Darlene Hyatt, "
    "Colossians, Ephesians, and Philemon (Grand Rapids: Baker, 2001), e meu livro New Testament "
    "History: A Narrative Account (Grand Rapids: Eerdmans, 1983), p. 326-9.\n\nEssas cartas "
    "apresentam temas em comum", "fn16")
rep("2Pedro não foi escrita por Pedro,” e as razões",
    "2Pedro não foi escrita por Pedro,¹⁷ e as razões", "mk17")
rep("em 2Pedro — é um docu- mento composto. É possível",
    "em 2Pedro — é um docu- mento composto.\n\n17 Outros especialistas em NT defendem a autoria "
    "petrina. Veja a defesa que Michael GREEN faz em Peter and Judas (São Paulo: Vida Nova, 1983), "
    "p. 12-33. (N. do E.)\n\nÉ possível", "fn17")

rep("e talvez também Romanos.\" Esses ecos de outras cartas",
    "e talvez também Romanos.¹⁸\n\n18 V. meu artigo “The Influence of Galatians on Hebrews”, New "
    "Testament Studies 37 (1991): 146-52.\n\nEsses ecos de outras cartas", "fn18")

rep("Paulo tenha escrito essas cartas.” Porém, para que elas",
    "Paulo tenha escrito essas cartas.¹⁹\n\n19 Estudiosos de renome, como J. N. D. KELLY, favorecem "
    "a autoria paulina. V. seus argumentos em 1 e 2 Timóteo e Tito (São Paulo: Vida Nova, 1983), "
    "p. 36-41.\n\nPorém, para que elas", "fn19")

rep("ouvindo a voz de Paulo diretamente.” As cartas são basicamente pessoais",
    "ouvindo a voz de Paulo diretamente.²⁰\n\n20 Em The Writings of the New Testament "
    "(Minneapolis: Fortress, 1999), p. 423-49, L. T. Johnson apresenta uma hipótese bem estruturada "
    "de que 2Timóteo tenha sido ditada por Paulo.\n\nAs cartas são basicamente pessoais", "fn20")

# ============ 5. BOXES LATERAIS ============
BOX1 = ("> Os dois anos de ministério de Paulo em Corinto tiveram um grande impacto na cidade e "
        "resultaram na conversão de um alto funcionário local, chamado Erasto (v. Rm 16.23), que é "
        "mencionado nessa inscrição encontrada em Corinto, em frente ao teatro: “Erasto, em pedra, "
        "o edil, pavimentou isto”. Ela diz, basicamente, o seguinte:")
rep("É claro que nem\n\ntodos os documentos entraram no NT, até mesmo os dos apóstolos. 1 Corintios parece ter sido",
    "É claro que nem todos os documentos entraram no NT, até mesmo os dos apóstolos.\n\n" + BOX1 +
    "\n\n1 Corintios parece ter sido", "box1")

BOX2 = ("> Paulo executou trabalho manual em Corinto, como fabricante de tendas. Provavelmente, "
        "também lá tenha escrito algumas de suas cartas, incluindo Romanos. Foi lá que ele conheceu "
        "Erasto, que devia estar coletando impostos como tesoureiro da cidade.")
rep("com um pé no paganismo e outro na igreja.\n\n## Romanos",
    "com um pé no paganismo e outro na igreja.\n\n" + BOX2 + "\n\n## Romanos", "box2")

# ============ 6. LISTA DA ESTRUTURA DA CARTA ANTIGA ============
rep("4. Corpo, composto de fórmula introdutória, corpo propriamente dito, conclusão, às vezes uma "
    "narrativa de viagem. Parênese, ou observações éticas. Saudações finais. Processo de escrita e "
    "assinatura. CONN Bênção final. Exceto o número 8",
    "4. Corpo, composto de fórmula introdutória, corpo propriamente dito, conclusão, às vezes uma "
    "narrativa de viagem.\n5. Parênese, ou observações éticas.\n6. Saudações finais.\n7. Processo "
    "de escrita e assinatura.\n8. Bênção final.\n\nExceto o número 8", "lista 1-8")

# ============ 7. EXERCÍCIOS ============
rep("* — Pegue uma carta", "1. Pegue uma carta", "ex1")
rep("Durante que período da história foram escritas as cartas de Paulo?",
    "2. Durante que período da história foram escritas as cartas de Paulo?", "ex2")
rep("Já foi dito que as cartas de Paulo podem ser separadas",
    "3. Já foi dito que as cartas de Paulo podem ser separadas", "ex3")
rep("O que é homilia? Existem homilias no NT?",
    "4. O que é homilia? Existem homilias no NT?", "ex4")
rep("Por que você acha que temos tantas cartas no NT?",
    "5. Por que você acha que temos tantas cartas no NT?", "ex5")

# ============ 8. JUNÇÕES DE QUEBRA DE PÁGINA ============
txt = re.sub(r"\n{3,}", "\n\n", txt)
JOINS = [
    ("mas também,\n\nprovavelmente, aos próprios evangelhos", "mas também, provavelmente, aos próprios evangelhos"),
    ("Entretanto, a primeira carta\n\nproduzida pela pena de Paulo", "Entretanto, a primeira carta produzida pela pena de Paulo"),
    ("destinatários. Colossenses\n\n4.16 deixa evidente", "destinatários. Colossenses 4.16 deixa evidente"),
    ("um documento\n\ncomo Filemom.", "um documento como Filemom."),
    ("fato de comer\n\ncomida sacrificada aos ídolos", "fato de comer comida sacrificada aos ídolos"),
    ("“Os primeiros judeus cristãos\n\nnão se consideravam", "“Os primeiros judeus cristãos não se consideravam"),
    ("seria por caso Cristo\n\nministro do pecado?", "seria por caso Cristo ministro do pecado?"),
    ("coisas do\n\ngênero. Em particular", "coisas do gênero. Em particular"),
    ("passagem de 2Coríntios\n1.8-10 é usada", "passagem de 2Coríntios 1.8-10 é usada"),
    ("e 1 Corintios\n\n15.32 provavelmente", "e 1Coríntios 15.32 provavelmente"),
    ("do vale do\n\nLico, na Ásia Menor", "do vale do Lico, na Ásia Menor"),
    ("Paulo escreve motivado\n\npor essa série", "Paulo escreve motivado por essa série"),
    ("foi talvez o\n\núltimo desses documentos", "foi talvez o último desses documentos"),
    ("Como 1 Pedro\n\n5.13 deixa evidente", "Como 1 Pedro 5.13 deixa evidente"),
    ("Clemente 1.3;\n\n21.6; 37.2", "Clemente 1.3; 21.6; 37.2"),
    ("convertidos dessas\n\ncongregações. Aparentemente", "convertidos dessas congregações. Aparentemente"),
    ("explica as\n\ndiferenças? Por que", "explica as diferenças? Por que"),
]
for i, (o, n2) in enumerate(JOINS):
    rep(o, n2, f"join{i}")

# ============ 9. NORMALIZAÇÕES ============
for o, n2 in [
    ("1 Corintios", "1Coríntios"),
    ("1Corintios", "1Coríntios"),
    ("gentilica", "gentílica"),
    ("bilíngiie", "bilíngüe"),
    ("G13 e 5", "Gl 3 e 5"),
    ("Espirito", "Espírito"),
    ("Th 4.11", "Tg 4.11"),
    ("Cord", "Coré"),
    ("nés mesmos", "nós mesmos"),
    ("¢ não por obras", "e não por obras"),
    ("vida vivo agora no corpo", "vida que vivo agora no corpo"),
    ("ha pouca controvérsia", "há pouca controvérsia"),
    ("À questão é controversa", "A questão é controversa"),
    ("À datação dessa carta", "A datação dessa carta"),
    ("À tentativa de retratar", "A tentativa de retratar"),
    ("À impressão que temos", "A impressão que temos"),
    ("Às crenças escatológicas", "As crenças escatológicas"),
    ("À genuína fé cristá", "A genuína fé cristã"),
    ("À pergunta retórica", "A pergunta retórica"),
    ("À maioria desses documentos", "A maioria desses documentos"),
    ("pagá", "pagã"),
    ("esteva em prisão", "estivesse em prisão"),
    ("década de G60", "década de 60"),
    ("feiros", "feitas"),
    ("2Timéteo", "2Timóteo"),
    ("comb imitadores", "como imitadores"),
    ("I Pedro", "1 Pedro"),
    ("| Pedro", "1 Pedro"),
    ("| Coríntios", "1 Coríntios"),
    ("prepara-me também pousada", "prepara-me também a pousada"),
    ("REVISAO", "REVISÃO"),
    ("(1Co 11— 14)", "(1Co 11—14)"),
]:
    txt = txt.replace(o, n2)

# hifenização de quebra de linha
txt = re.sub(r"(?u)([a-zçá-úâ-ûã-õ])-\s+(?=[a-zçá-úâ-ûã-õ])", r"\1", txt)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

# ============ 10. DIAGNÓSTICO ============
print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
resto_pipe = [l for l in txt.split("\n") if l.strip().startswith("|")]
print("LINHAS COM '|' RESTANTES:", len(resto_pipe))
for l in resto_pipe[:5]:
    print("   ", l[:100])
print("U+FFFD:", txt.count("\ufffd"))
print("--- HEADINGS ---")
for h in txt.split("\n"):
    if h.startswith("#"):
        print(" ", h)
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
