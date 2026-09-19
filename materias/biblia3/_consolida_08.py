# -*- coding: utf-8 -*-
"""Consolida 08-Witherington_Joao.md (pp. 85-96 do cap. 4) — fidelidade 1:1."""
import io, re

RAW = r"E:\00_ATUAL\04_PROJETO\teoftsa\materias\biblia3\01_markdown\adicionais\08-Witherington_Joao.md"

with io.open(RAW, "r", encoding="utf-8") as f:
    raw = f.read()
print("U+FFFD antes:", raw.count(chr(0xFFFD)))
lines = raw.split("\n")

missing = []
def rep(txt, old, new, must=True):
    if old in txt:
        return txt.replace(old, new)
    if must:
        missing.append(old[:70])
    return txt

# ---------------------------------------------------------------- filtros de linha
hdr_valia = re.compile(r"PENA\s+REGISTRAR\s+SOBRE\s+AS\s+BOAS\s+NOVAS", re.I)
hdr_hist = re.compile(r"HIST[OÓ]RIA\s+DO\s+NOVO\s+[FT]ESTAMENTO", re.I)

DROP = set()
DROP.update(range(1, 9))          # capa mojibake (reconstruída)
DROP.update(range(82, 88))        # notas 12-13 cruas (reconstruídas)
DROP.update((151, 152, 153))      # ruído da caixa do milagre
DROP.update((154, 155))           # legenda 1 (vira blockquote)
DROP.add(240)                     # nota 14 crua
DROP.add(283)                     # nota 15 crua
DROP.update((413, 414))           # nota 16 crua
DROP.update(range(418, 440))      # ruído da foto de Éfeso
DROP.update((440, 441, 442))      # legenda 2 (vira blockquote)

# quebras de parágrafo a inserir (linhas sem linha em branco no bruto)
BREAK_BEFORE = {21, 22, 27, 32, 33, 34,   # capa
                54, 55,                    # heading João
                177, 178,                  # heading Epístolas de João
                477, 478,                  # heading Conclusões
                498, 499,                  # heading Exercícios
                504, 505, 508, 510, 514}   # itens 2-6 dos exercícios

kept = []
for i, ln in enumerate(lines, start=1):
    if i in DROP:
        continue
    s = ln.strip()
    if not s:
        if i > 45:  # mantém blanks do miolo (capa tem os nossos)
            kept.append("")
        continue
    if hdr_valia.search(s) or (hdr_hist.search(s) and len(s) < 80):
        continue
    if i in BREAK_BEFORE and kept and kept[-1] != "":
        kept.append("")
    kept.append(ln)
    if i == 45:  # fim dos créditos da capa
        kept.append("")

txt = "\n".join(kept)

# ---------------------------------------------------------------- reflow de parágrafos
paras, buf = [], []
for ln in txt.split("\n"):
    if ln.strip() == "":
        if buf:
            paras.append(" ".join(buf)); buf = []
        paras.append("")
    else:
        buf.append(ln.strip())
if buf:
    paras.append(" ".join(buf))
txt = "\n".join(paras)
txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"

# ---------------------------------------------------------------- emendas de parágrafos (cabeçalhos/notas removidos)
joins = [
    ("do ministério\n\nde Jesus em que os filhos de Zebedeu", "do ministério de Jesus em que os filhos de Zebedeu"),
    ("primeiro estágio da\n\nexaltação de Jesus", "primeiro estágio da exaltação de Jesus"),
    ("cerne das verdades\n\ncristológicas", "cerne das verdades cristológicas"),
    ("ao que encontramos\n\nem João 1.", "ao que encontramos em João 1."),
    ("coletânea de visões\n\norganizada dentro", "coletânea de visões organizada dentro"),
    ("que, por sua\n\nvez, a transmite", "que, por sua vez, a transmite"),
    ("autor arcaíza\n\n(nesse caso", "autor arcaíza (nesse caso"),
    ("uma em\n\ncada oito palavras", "uma em cada oito palavras"),
    ("paradoxalmente,\n\nnão existia", "paradoxalmente, não existia"),
]
for old, new in joins:
    txt = rep(txt, old, new)

# des-hifenização de fim de linha
txt = re.sub(r"(?u)([a-zçá-úâ-ûã-õ])-\s+(?=[a-zçá-úâ-ûã-õ])", r"\1", txt)

# ---------------------------------------------------------------- capa
txt = rep(txt, "Copyright O 2004", "Copyright © 2004")
txt = rep(txt, "O 1995 Sociedade", "© 1995 Sociedade")
txt = rep(txt, "O 2005 Sociedade", "© 2005 Sociedade")
txt = rep(txt, "2.o edição", "2.a edição")
txt = rep(txt, "1.3 edição", "1.a edição")
txt = rep(txt, "1.2 edição: 2005", "1.a edição: 2005")

# ---------------------------------------------------------------- headings
txt = re.sub(r"(?m)^JoÃo$", "## João", txt)
txt = re.sub(r"(?m)^ÀS EPÍSTOLAS DE JOÃO E APOCALIPSE$", "## As epístolas de João e Apocalipse", txt)
txt = re.sub(r"(?m)^CONCLUSÕES$", "## Conclusões", txt)
txt = re.sub(r"(?m)^ExERCÍCIOS E QUESTÕES PARA ESTUDO E REFLEXÃO$",
             "## Exercícios e questões para estudo e reflexão", txt)
for h in ("## João", "## As epístolas de João e Apocalipse", "## Conclusões",
          "## Exercícios e questões para estudo e reflexão"):
    if h not in txt:
        missing.append("HEADING " + h)

# ---------------------------------------------------------------- marcadores das notas
txt = rep(txt, "ensinamentos.'? Somente", "ensinamentos.¹² Somente")
txt = rep(txt, "Sabedoria de Salomão.'* O quarto", "Sabedoria de Salomão.¹³ O quarto")
txt = rep(txt, "reforçar o Decreto e a epístola", "reforçar o Decreto¹⁴ e a epístola")
txt = rep(txt, "(nesse caso, “semitiza”)!o deliberadamente", "(nesse caso, “semitiza”)¹⁶ deliberadamente")

# ---------------------------------------------------------------- notas de rodapé (estilo idêntico ao 06)
txt = rep(txt,
    "embora seu nome possa ter sido João.\n\nO autor desse evangelho",
    "embora seu nome possa ter sido João.\n\n"
    "12 Sobre esse assunto, v. meu livro John's Wisdom: A Commentary on the Fourth Gospel "
    "(Louisville: Westminster/John Knox, 1995).\n\n"
    "13 Também conhecida por Livro da Sabedoria, essa obra é considerada apócrifa, isto é, não inspirada, "
    "na teologia protestante. A Igreja Católica Romana, em contrapartida, considera seu conteúdo inspirado "
    "por Deus. Para mais informações, v. o verbete Livros Apócrifos do Dicionário Ilustrado da Bíblia "
    "(São Paulo: Vida Nova, 2004), p. 868. (N. do E.)\n\n"
    "O autor desse evangelho")

txt = rep(txt,
    "na região onde hoje se encontra a Turquia.\n\nAlguns temas em 1João",
    "na região onde hoje se encontra a Turquia.\n\n14 V. p. 60-3.\n\nAlguns temas em 1João")

txt = rep(txt,
    "à exceção de Apocalipse. Por quê?”\n\nÉ claro que existem",
    "à exceção de Apocalipse. Por quê?”¹⁵\n\n"
    "15 Sobre todo o assunto a seguir, v. meu livro Revelation "
    "(Cambridge: Cambridge University Press, 2003).\n\nÉ claro que existem")

txt = rep(txt,
    "Já no evangelho, é o inverso.\n\nEssas diferenças de redação",
    "Já no evangelho, é o inverso.\n\n"
    "16 Isso é pouco provável, tendo em vista que o autor acha natural usar o AT hebraico "
    "como sua maior fonte externa.\n\nEssas diferenças de redação")

# ---------------------------------------------------------------- caixas laterais → blockquotes
txt = rep(txt,
    "apresenta longos discursos e narrativas.\n\nAlguém já disse",
    "apresenta longos discursos e narrativas.\n\n"
    "> A única história de milagre que todos os escritores dos evangelhos acharam necessário ser "
    "incluída em seus livros foi a da alimentação dos cinco mil, ou o milagre da multiplicação "
    "dos pães e peixes.\n\nAlguém já disse")

txt = rep(txt,
    "o restante do corpus joanino e/ou com suas comunidades.\n\nPara compreender o livro",
    "o restante do corpus joanino e/ou com suas comunidades.\n\n"
    "> Entre as cidades às quais João endereçou Apocalipse — ou, pelo menos, aos cristãos dessas "
    "cidades — estava Éfeso, um importante centro de comércio, religião e erudição, como sugere a "
    "impressionante biblioteca de Celso.\n\nPara compreender o livro")

# ---------------------------------------------------------------- correções de OCR / digitação
fixes = [
    ("segiiências", "sequências"),
    ("cle terminará", "ele terminará"),
    ("aguilo", "aquilo"),
    ("ilha de Parmos", "ilha de Patmos"),
    ("meretrriz", "meretriz"),
    ("amion", "arnion"),
    ("lingiiístico", "lingüístico"),
    ("traduzí-la", "traduzi-la"),
    ("1.e.", "i.e."),
    ("epistolas joaninas", "epístolas joaninas"),
    ("em um língua", "em uma língua"),
    ("aa modo", "ao modo"),
    ("nas costas da Ásia", "na costa da Ásia"),
    ("Jo 1220", "Jo 12—20"),
    ("Jo 14— 17", "Jo 14—17"),
    ("(v. Jo. 20", "(v. Jo 20"),
    ("(v. Jo. 3.16", "(v. Jo 3.16"),
    ("em Jo. 12", "em Jo 12"),
    ("“sinais são", "“sinais” são"),
    ("À cruz aqui é vista", "A cruz aqui é vista"),
    ("À julgar por João 20.31", "A julgar por João 20.31"),
    ("À tradição de que teria sido", "A tradição de que teria sido"),
    ("À comunidade a que o livro se destina", "A comunidade a que o livro se destina"),
    ("À justiça será feita", "A justiça será feita"),
    ("obra prima", "obra-prima"),
    ("v., p. ex.; a descrição", "v., p. ex., a descrição"),
    ("podem ser visto com um olhar", "podem ser vistos com um olhar"),
    ("o faro de não sabermos", "o fato de não sabermos"),
]
for old, new in fixes:
    txt = rep(txt, old, new, must=False)

# ---------------------------------------------------------------- exercícios numerados
ex = [
    ("é Ostrês primeiros evangelhos", "1. Os três primeiros evangelhos"),
    ("à Qual é o verdadeiro significado", "2. Qual é o verdadeiro significado"),
    ("à — Que tipo ou tipos", "3. Que tipo ou tipos"),
    ("à Nasua opinião", "4. Na sua opinião"),
    ("à Faça uma tabela", "5. Faça uma tabela"),
    ("à» — Quem era o discípulo amado", "6. Quem era o discípulo amado"),
]
for old, new in ex:
    txt = rep(txt, old, new)

# ---------------------------------------------------------------- gravação + verificação
with io.open(RAW, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)

print("U+FFFD depois:", txt.count(chr(0xFFFD)))
print("linhas:", txt.count("\n") + 1, "| bytes:", len(txt.encode("utf-8")))
if missing:
    print("\n[NAO ENCONTRADO] (%d):" % len(missing))
    for m in missing:
        print("  -", m)
else:
    print("\nTodas as substituicoes exatas aplicadas.")

resid = [l for l in txt.split("\n")
         if re.search(r"PENA REGISTRAR|NOVO [FT]ESTAMENTO", l, re.I)
         or re.search(r"'\?|'\*|!o |Jo\. \d", l)]
print("\nresiduo suspeito:", len(resid))
for l in resid[:10]:
    print("  >", l[:100])

quebrados = re.findall(r".{40}[a-z,;]\n\n[a-zà-ú].{20}", txt)
print("\nparagrafos possivelmente quebrados:", len(quebrados))
for q in quebrados[:10]:
    print("  ~", q.replace("\n", "⏎"))

print("\n--- INICIO ---")
print(txt[:400])
print("--- FIM ---")
print(txt[-500:])
