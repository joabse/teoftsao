# 📚 materias — Fluxo de Produção de Textos FTSA

Esta pasta contém uma subpasta por matéria (disciplina). Cada matéria segue **exatamente o mesmo padrão de subpastas**, que representa as etapas do pipeline de produção de textos da equipe FTSA.

## Subpastas do fluxo (em toda matéria)

| Pasta | O que contém | Quem usa |
|---|---|---|
| `00_originais\` | Arquivos **como enviados pelo usuário** (PDF, DOCX, PPTX etc.). Nunca modificar o conteúdo original. | Usuário → arquivo de entrada |
| `01_markdown\` | Conversões dos originais para **Markdown**, produzidas pelo agente **file2md**. | file2md |
| `02_rascunhos\` | **Textos produzidos pelos teólogos** (Claude Code, Codex CLI, Antigravity, gbooklm) a partir dos materiais. | Teólogos |
| `03_revisao\` | Textos em **ciclo de revisão/humanização** (Bereano detecta IA, Escriba humaniza), com versões numeradas (`v1.md`, `v2.md`, …). | Bereano + Escriba |
| `04_aprovados\` | Textos **finais validados** (aprovados pelo Bereano como humanos). Entrega para o usuário. | Saída final |

## Como criar uma nova matéria

1. Crie uma pasta em `materias\` com o nome da disciplina, sem espaços, em minúsculas
   (ex.: `materias\teologia-sistematica1\`). Se precisar de separação, use hífen `-`.
2. Copie para dentro dela as subpastas do modelo `materias\_TEMPLATE\`
   (ou apenas copie a pasta `_TEMPLATE` inteira e renomeie).
3. A estrutura final deve ficar assim:

```
materias\<nome-da-materia>\
├── 00_originais\
├── 01_markdown\
├── 02_rascunhos\
├── 03_revisao\
└── 04_aprovados\
```

4. **Registre a nova matéria** no índice `ftsabrain\materias.md`.

## Regras do fluxo

- O original em `00_originais\` é imutável — qualquer transformação gera arquivo em outra pasta.
- Toda conversão para Markdown vai para `01_markdown\` (responsável: file2md).
- Rascunhos dos teólogos nascem em `02_rascunhos\`.
- Todo texto precisa passar pelo **ciclo de humanização** antes de ir para `04_aprovados\`:
  texto → **Bereano** (detector de IA); se reprovado → **Escriba** humaniza → Bereano de novo → repete até aprovação.
- Em `03_revisao\`, salve cada nova versão com numeração crescente (`nome_v1.md`, `nome_v2.md`, …) para manter histórico.
- Só entram em `04_aprovados\` textos explicitamente aprovados pelo Bereano.

## Matérias existentes

- `biblia2\` — Bíblia 2
- `_TEMPLATE\` — modelo (copiar ao criar nova matéria; não usar como matéria real)

Ver também: `..\ESTRUTURA.md` (organização geral e papéis) e `..\ftsabrain\pipeline.md` (resumo do pipeline).
