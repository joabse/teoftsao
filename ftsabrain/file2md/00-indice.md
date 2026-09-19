---
tipo: indice
agente: file2md
atualizado_em: 2026-09-19
descricao: Índice geral de conversões de materiais originais para Markdown no projeto FTSA
tags:
  - file2md
  - indice
  - conversoes
---

# 📑 file2md — Índice de Conversões

> Este índice é o registro centralizado de todos os arquivos originais convertidos para Markdown pelo agente **file2md** no projeto **teoftsao**.
> Todo arquivo convertido para `materias/<nome>/01_markdown/` deve ser obrigatoriamente registrado aqui com a data e hora da conversão, ferramenta utilizada e status.

---

## 🛠️ Diretrizes Operacionais do file2md

1. **Terminal Dedicado:** O agente file2md opera no terminal nomeado `file2md` no Orca.
2. **Verificação Prévia Obrigatória:** Antes de despachar qualquer conversão, o líder (**ftsalider**) deve inspecionar qual modelo e CLI estão em execução no terminal `file2md` (via `orca terminal list` e `orca terminal read`) para adaptar instruções e comandos.
3. **Ferramenta Nativa (anydoc):** Para documentos digitais nativos (`.docx`, `.pptx`, `.xlsx`, `.pdf` nativo, `.epub`, `.csv`), o file2md utiliza a CLI `anydoc` (`@firecrawl/anydoc`).
4. **Tratamento de OCR (PDFs Escaneados):** PDFs escaneados ou baseados em imagens acionam aviso de necessidade de OCR no `anydoc`. Para estes arquivos, utilizam-se scripts locais de OCR dedicados (como os consolidados em Python em `materias/biblia3/` ou pipeline específico).
5. **Alimentação do ftsabrain:** Toda conversão alimenta o conhecimento do projeto, gerando as notas em `01_markdown/` e alimentando o `ftsabrain` (`ftsabrain/materias/<nome>/fontes/` e este índice `ftsabrain/file2md/00-indice.md`).

---

## 📋 Registro Cronológico de Conversões

| Data / Hora | Matéria | Arquivo Original | Formato | Destino Markdown | Ferramenta | Status |
|---|---|---|---|---|---|---|
| 2026-09-19 14:11 | biblia2 | `Apostila - Bíblia II - Introdução ao AT.pdf` | PDF nativo | `scratch/test_apostila.md` (validação anydoc) | `anydoc 0.2.4` | ✅ Sucesso (311 KB limpo) |
| 2026-09-12 17:38 | biblia2 | `Apostila - Bíblia II - Introdução ao AT.pdf` | PDF nativo | `materias/biblia2/01_markdown/Apostila - Bíblia II - Introdução ao AT.md` | `file2md` | ✅ Convertido |
| 2026-09-12 17:49 | biblia2 | `01_HILL_Andrew_51_70.pdf` | PDF escaneado | `materias/biblia2/01_markdown/adicionais/01_Hill_Andrew_51-70.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 17:51 | biblia2 | `01_HILL_Andrew_51_70a.pdf` | PDF escaneado | `materias/biblia2/01_markdown/adicionais/01_Hill_Andrew_51-70a.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 17:52 | biblia2 | `02_A ética do AT - GERSTENBERGER_107_118.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/02_Gerstenberger_Etica_do_AT.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 17:54 | biblia2 | `03_MENDONÇA, Élcio Valmiro...pdf` | PDF | `materias/biblia2/01_markdown/adicionais/03_Mendonca_Livro_de_Juizes...md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:11 | biblia2 | `04_Zenger_Erich_Introd. ao AT_61-88.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/04_Zenger_Introd_ao_AT_pp61-88.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:17 | biblia2 | `05_PDF - Débora Thomaz Cavalcante Dutra.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/05_Dutra_Debora_Thomaz.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:19 | biblia2 | `06-MILHORANZA, Alexandre. “Literatura Profética”.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/06_Milhoranza_Literatura_Profetica.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:22 | biblia2 | `08_Zenger_Erich_Introd. ao AT_96-112.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/08_Zenger_Introd_ao_AT_pp96-112.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:24 | biblia2 | `09_Zenger_Erich_Introd. ao AT_159-169.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/09_Zenger_Introd_ao_AT_pp159-169.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:29 | biblia2 | `10_Zenger_Erich_Introd. ao AT_283-290.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/10_Zenger_Introd_ao_AT_pp283-290.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 18:33 | biblia2 | `11_Zenger_Erich_Introd. ao AT_267-280.pdf` | PDF | `materias/biblia2/01_markdown/adicionais/11_Zenger_Introd_ao_AT_pp267-280.md` | OCR / Python | ✅ Convertido |
| 2026-09-12 19:10 | biblia3 | `Apostila_Bíblia III -  Introução ao NT.pdf` | PDF nativo | `materias/biblia3/01_markdown/Apostila_Bíblia III -  Introução ao NT.md` | `file2md` | ✅ Convertido |
| 2026-09-12 21:50 | biblia3 | `01-Stambaugh,Bauch_ContextoHistorico.pdf` a `10-Boer...` (10 PDFs) | PDFs | `materias/biblia3/01_markdown/adicionais/` (10 itens) | OCR / Python | ✅ Convertido |
| 2026-09-12 21:55 | biblia3 | 12 Aulas + 4 Podcasts/Extras (áudio/vídeo) | Transcrição (.txt) | `materias/biblia3/01_markdown/transcricoes/` (16 itens) | Transcrição / Text | ✅ Convertido |

---

## 🗂️ Navegação Rápida

- [[../materias|MOC de Matérias]]
- [[../pipeline|Pipeline FTSA]]
- [[../memoria/00-registro-geral|Registro Geral]]



