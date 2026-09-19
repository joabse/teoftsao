# -*- coding: utf-8 -*-
"""Consolida 04-Alter_NTLiterGrecoRomana.md (OCR de scan 2 colunas).
Fases:
  A) ajustes de titulos/democoes em texto puro (antes do strip de tabelas)
  B) strip generico de tabelas pipe (preserva ordem de leitura do arquivo)
  C) reassemblagens de notas de rodape/citacoes cuja ordem e inequivoca
  D) remocao de linhas de ruido de OCR e normalizacoes mecanicas
Nao inventa conteudo: apenas remove sintaxe de tabela, demove falsos
titulos, une fragmentos e reordena apenas onde a ordem original e certa.
"""
from pathlib import Path
import re, sys

P = Path(r"E:\00_ATUAL\04_PROJETO\teoftsa\materias\biblia3\01_markdown\adicionais\04-Alter_NTLiterGrecoRomana.md")
txt = P.read_text(encoding="utf-8").replace("\r\n", "\n")
erros = []

def rep(old, new, tag):
    global txt
    if old not in txt:
        erros.append(f"[NAO ENCONTRADO] {tag}: {old[:90]!r}")
        return
    txt = txt.replace(old, new, 1)

# ---------- FASE A ----------
rep("## O Novo Testamento\n\n# e a escrita greco-romana\n\n##### Helen Elsom",
    "# O Novo Testamento e a escrita greco-romana\n\n*Helen Elsom*", "A1 titulo")

rep("\n##### Guia literário da Bíblia\n", "\n", "A2 cabecalho pagina")

rep("são como\n\nEd\n\nO Novo Testamento e a escrita greco-romana\n\n"
    "##### outros textos gregos específicos, e portanto da mesma\n\n"
    "##### “espécie”. Por exemplo,\n\n"
    "##### com os diálogos socráticos de Platão\n\n"
    "##### e com a Memorabilia de",
    "são como\n\noutros textos gregos específicos, e portanto da mesma "
    "“espécie”. Por exemplo, com os diálogos socráticos de Platão e com a Memorabilia de",
    "A3 fragmentos titulo secao 1")

rep("\nOs Evangelhos e Atos: gêneros narrativos\n",
    "\n## Os Evangelhos e Atos: gêneros narrativos\n", "A4 secao Evangelhos/Atos")

rep("##### Biografia helenística e greco-romana",
    "## Biografia helenística e greco-romana", "A5 secao Biografia")

rep("CCC um quadro mais detalhado, ver Momigliano,\n\n"
    "A. The Development of Greek Biography, Cam-\n##### 3 Para\n\n"
    "bridge, Mass., e London, 1971,",
    "3 Para um quadro mais detalhado, ver Momigliano, A. The Development of "
    "Greek Biography, Cambridge, Mass., e London, 1971,", "A6 nota 3")

rep("##### Ambos referem-se a versões anteriores, ambos reivindicam\n\nprecisão e\n\nambos definem",
    "Ambos referem-se a versões anteriores, ambos reivindicam precisão e ambos definem",
    "A7 juncao frase")

rep("Novela\n\n##### poderem ser lidos como “buscas” de\n\nidentidade",
    "## Novela\n\npoderem ser lidos como “buscas” de\n\nidentidade", "A8 secao Novela")

rep("##### missão, sugerindo sobrevivência ou mesmo ressurreição\n\n"
    "##### de um só herói. As\n\n"
    "##### em particular, cobrem o terreno\n\n"
    "##### geográfico e às vezes ético\n\n"
    "##### viagens de Paulo,\n\n"
    "dos heróis da novela.",
    "missão, sugerindo sobrevivência ou mesmo ressurreição de um só herói. As "
    "viagens de Paulo, em particular, cobrem o terreno geográfico e às vezes "
    "ético dos heróis da novela.", "A9 frase Atos")

rep("##### As Epístolas", "## As Epístolas", "A10 secao Epistolas")

rep("## ver Stowers, S. K.\n\n## The Diatribe and Paul's\n\n"
    "## Letter to the Romans, Para um exame recet © desse tópico, 1\n\n"
    "Missoula, Mont.,1981.",
    "11 Ver Stowers, S. K. The Diatribe and Paul's Letter to the Romans, "
    "Para um exame recente desse tópico, Missoula, Mont., 1981.", "A11 nota 11")

rep("##### de Paulo é modificar a escrita legislativa\n\n"
    "##### imperial, e desse modo\n\n"
    "##### O objetivo\n\n",
    "O objetivo de Paulo é modificar a escrita legislativa imperial, e desse modo\n\n",
    "A12a frase objetivo")

rep("##### A imagem mais proeminente no ensino de Paulo\n\n"
    "##### é a do documento legal\n\n"
    "##### em todas as suas formas, incluindo a própria\n\n"
    "##### carta legislativa. A discussão da\n\n",
    "A imagem mais proeminente no ensino de Paulo é a do documento legal em "
    "todas as suas formas, incluindo a própria carta legislativa. A discussão da\n\n",
    "A12b frase imagem legal")

rep("\nSugestão de leituras\n", "\n## Sugestão de leituras\n", "A13 secao leituras")

# ---------- FASE B: strip de tabelas ----------
lines = txt.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith("|"):
        while i < len(lines) and lines[i].startswith("|"):
            row = lines[i].strip().strip("|")
            cells = [c.strip() for c in row.split("|")]
            if cells and all(c and set(c) <= set("-:") for c in cells):
                pass  # linha separadora
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

# ---------- FASE C ----------
rep("do Império Romano. As expectativas de seus possíveis leitores,\n\n"
    "de língua grega, do Império Romano. As expectativas de seus possíveis leitores,\n\n"
    "que devemos entender",
    "do Império Romano. As expectativas de seus possíveis leitores,\n\nque devemos entender",
    "C0 dedup sobreposicao")

rep("Visto que muitos antes tentaram ordenar um relato do cumprimento da profecia "
    "conforme nos foi transmitido por aqueles que foram testemunhas e servidores da "
    "observação escrever sobre todos os detalhes\n\n"
    "palavra, eu decidi depois de cuidadosa\n\n"
    "desde o início. (1:1-3 [TA])",
    "Visto que muitos antes tentaram ordenar um relato do cumprimento da profecia "
    "conforme nos foi transmitido por aqueles que foram testemunhas e servidores da "
    "palavra, eu decidi depois de cuidadosa observação escrever sobre todos os "
    "detalhes desde o início. (1:1-3 [TA])", "C1 citacao Lucas 1:1-3")

rep("4 Tácito descreve o suicídio forçado de Sêneca em uma paródia da morte de "
    "Sócrates (Anais 15:\n\n"
    "62-63); Dion de Prusa distorce (Oração 13).\n\n"
    "a história de seu exílio para se assemelhar a Sócrates",
    "4 Tácito descreve o suicídio forçado de Sêneca em uma paródia da morte de "
    "Sócrates (Anais 15:62-63); Dion de Prusa distorce a história de seu exílio "
    "para se assemelhar a Sócrates (Oração 13).", "C2 nota 4")

rep("8 Essa posição University, 1981). é bem delineada em Trembley, J. T, The Beloved "
    "Self (Tese de Doutorado, Princeton\n\n"
    "7 Aafirmação definitiva da concepção de que as novelas são narrativas de culto "
    "disfargadas é Roman",
    "8 Essa posição é bem delineada em Trembley, J. T, The Beloved Self (Tese de "
    "Doutorado, Princeton University, 1981).", "C3 notas 7/8 dedup")

rep("10 Ver White, J. L. New Testament Epistolary in the Framework of Ancient "
    "Epistolography,\n\n"
    "und Niedergang Welt II 25.2, Berlin, 1984, p.1730-56, esp. p.1733-51.\n\n"
    "L,terature Aufstieg der Rômischen",
    "10 Ver White, J. L. New Testament Epistolary Literature in the Framework of "
    "Ancient Epistolography, in Aufstieg und Niedergang der Römischen Welt II 25.2, "
    "Berlin, 1984, p.1730-56, esp. p.1733-51.", "C4 nota 10")

rep("eo 6 Poética 1452 a22-b13", "6 Poética 1452 a22-b13", "C5 nota 6 prefixo")

rep("CHALK, H. H. O. Eros and the Lesbian Pastorals of Longus, Journal of Hellenic "
    "Studies,\n\nv.80, p.32-51, 1960.",
    "CHALK, H. H. O. Eros and the Lesbian Pastorals of Longus, Journal of Hellenic "
    "Studies, v.80, p.32-51, 1960.", "C6 ref Chalk")

rep("WHITE, J. L. New Testament Epistolary Litarature in the Framework of Ancient "
    "Epistolography\n\nin Aufstieg und Niedergang der Rémischen Welt 1 25:2, Berlin, 1984, p.170-56.",
    "WHITE, J. L. New Testament Epistolary Literature in the Framework of Ancient "
    "Epistolography in Aufstieg und Niedergang der Römischen Welt 1 25:2, Berlin, "
    "1984, p.170-56.", "C7 ref White")

rep("(1:98), Ver Pseudo-Aristóteles, De mundo\n\n"
    "12 A descrição da cidade se origina em Heródoto\n\n"
    "imperial.\n\n"
    "Apuleio traduz De mundo de modo a fazê-lo refletir a mistificação da burocracia 398a11-b10.",
    "12 A descrição da cidade se origina em Heródoto (1:98), Ver Pseudo-Aristóteles, "
    "De mundo 398a11-b10. Apuleio traduz De mundo de modo a fazê-lo refletir a "
    "mistificação da burocracia imperial.", "C8 nota 12")

rep("\nClare College, University of Cambridge\n",
    "\n*Clare College, University of Cambridge*\n", "C9 afiliacao")

# ---------- FASE D: ruidos e normalizacoes ----------
RUIDOS = {"Digitalizado com CamScanner", "Fa", "Za", "q", "a a", "e..",
          "parte oe ——", "escrever, h", "CO —",
          "e a escrita greco-romana O Novo Testamento", "a"}
lines = [ln for ln in txt.split("\n") if ln.strip() not in RUIDOS]
txt = "\n".join(lines)

for old, new in [
    ("freqiiéncia", "freqüência"),
    ("freqiientemente", "freqüentemente"),
    ("Antigiiidade", "Antigüidade"),
    ("disfargadas", "disfarçadas"),
    ("Pscudo-Aristóteles", "Pseudo-Aristóteles"),
    ("Na Apologia, Socrates é julgado", "Na Apologia, Sócrates é julgado"),
    ("criticava 0 Império Romano", "criticava o Império Romano"),
    ("desde 0 início", "desde o início"),
    ("e 0 reconhe-", "e o reconhe-"),
    (" ¢ ", " e "),
    ("cpistolar", "epistolar"),
    ("autocratico,", "autocrático,"),
    ("filósoto", "filósofo"),
    ("(Rom, 1:14)", "(Rom. 1:14)"),
    ("1,terature", "Literature"),
]:
    txt = txt.replace(old, new)

txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
P.write_text(txt, encoding="utf-8")

heads = [ln for ln in txt.split("\n") if ln.startswith("#")]
print("ERROS:", len(erros))
for e in erros:
    print(" ", e)
print("--- HEADINGS ---")
for h in heads:
    print(" ", h)
print(f"--- {len(txt.splitlines())} linhas, {len(txt.encode('utf-8'))} bytes ---")
