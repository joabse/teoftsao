# -*- coding: utf-8 -*-
"""Correções finais do 08: inserção das notas 12-16 em limites mesclados por espaço."""
import io

F = r"E:\00_ATUAL\04_PROJETO\teoftsa\materias\biblia3\01_markdown\adicionais\08-Witherington_Joao.md"
with io.open(F, "r", encoding="utf-8") as f:
    txt = f.read()

missing = []
def rep(old, new):
    global txt
    if old in txt:
        txt = txt.replace(old, new, 1)
    else:
        missing.append(old[:80])

rep("embora seu nome possa ter sido João. O autor desse evangelho",
    "embora seu nome possa ter sido João.\n\n"
    "12 Sobre esse assunto, v. meu livro John's Wisdom: A Commentary on the Fourth Gospel "
    "(Louisville: Westminster/John Knox, 1995).\n\n"
    "13 Também conhecida por Livro da Sabedoria, essa obra é considerada apócrifa, isto é, não inspirada, "
    "na teologia protestante. A Igreja Católica Romana, em contrapartida, considera seu conteúdo inspirado "
    "por Deus. Para mais informações, v. o verbete Livros Apócrifos do Dicionário Ilustrado da Bíblia "
    "(São Paulo: Vida Nova, 2004), p. 868. (N. do E.)\n\n"
    "O autor desse evangelho")

rep("na região onde hoje se encontra a Turquia. Alguns temas em 1João",
    "na região onde hoje se encontra a Turquia.\n\n14 V. p. 60-3.\n\nAlguns temas em 1João")

rep("à exceção de Apocalipse. Por quê?” É claro que existem",
    "à exceção de Apocalipse. Por quê?”¹⁵\n\n"
    "15 Sobre todo o assunto a seguir, v. meu livro Revelation "
    "(Cambridge: Cambridge University Press, 2003).\n\nÉ claro que existem")

rep("Já no evangelho, é o inverso. Essas diferenças de redação",
    "Já no evangelho, é o inverso.\n\n"
    "16 Isso é pouco provável, tendo em vista que o autor acha natural usar o AT hebraico "
    "como sua maior fonte externa.\n\nEssas diferenças de redação")

with io.open(F, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)

print("faltando:", len(missing))
for m in missing:
    print("  -", m)

# verificação completa
checks = {
    "marcador 12": "ensinamentos.¹²" in txt,
    "marcador 13": "Salomão.¹³" in txt,
    "marcador 14": "Decreto¹⁴" in txt,
    "marcador 15": "Por quê?”¹⁵" in txt,
    "marcador 16": "semitiza”)¹⁶" in txt,
    "nota 12": "12 Sobre esse assunto, v. meu livro John's Wisdom" in txt,
    "nota 13": "13 Também conhecida por Livro da Sabedoria" in txt,
    "nota 14": "14 V. p. 60-3." in txt,
    "nota 15": "15 Sobre todo o assunto a seguir" in txt,
    "nota 16": "16 Isso é pouco provável" in txt,
    "heading João": "## João" in txt,
    "heading Epístolas": "## As epístolas de João e Apocalipse" in txt,
    "heading Conclusões": "## Conclusões" in txt,
    "heading Exercícios": "## Exercícios e questões para estudo e reflexão" in txt,
    "blockquote 1": "> A única história de milagre" in txt,
    "blockquote 2": "> Entre as cidades às quais João" in txt,
    "exercício 1": "1. Os três primeiros evangelhos" in txt,
    "exercício 2": "2. Qual é o verdadeiro significado" in txt,
    "exercício 3": "3. Que tipo ou tipos" in txt,
    "exercício 4": "4. Na sua opinião" in txt,
    "exercício 5": "5. Faça uma tabela" in txt,
    "exercício 6": "6. Quem era o discípulo amado" in txt,
    "Patmos": "ilha de Patmos" in txt,
    "obra-prima": "obra-prima" in txt,
}
falhas = [k for k, v in checks.items() if not v]
print("verificações falhas:", falhas if falhas else "NENHUMA — tudo OK")
print("U+FFFD:", txt.count(chr(0xFFFD)))
print("linhas:", txt.count("\n") + 1, "| bytes:", len(txt.encode("utf-8")))
print("blockquotes:", sum(1 for l in txt.split("\n") if l.startswith("> ")))
