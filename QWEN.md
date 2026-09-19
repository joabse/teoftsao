# QWEN.md — Diretrizes para Qwen Code no Projeto teoftsao

> Este arquivo é carregado automaticamente pelo **Qwen Code** no início de cada sessão neste diretório. Consolida as diretrizes de `AGENTS.md` (arquivo canônico), `ESTRUTURA.md` e `ORCA.md` para que qualquer LLM rodando como Qwen Code neste projeto entenda a estrutura, os papéis e as regras sem precisar reler os três arquivos separadamente. Em caso de dúvida ou divergência, `AGENTS.md`/`ESTRUTURA.md`/`ORCA.md` são a fonte de verdade — este arquivo é um espelho.

---

## 0. Regras Críticas (Obrigatórias)

1. **Controle de Versão:** Repositório Git privado (`joabse/teoftsao`) gerenciado no Orca. **Commits passam pelo terminal comitador** — nunca rode `git commit` por conta própria; avise o ftsalider se algo precisar ser comitado.
2. **Papéis pertencem ao terminal, não à LLM (Joab, 2026-09-19):** o projeto roda em 6 terminais nomeados no Orca — **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3**, **comitador** e **file2md** — cada um com papel fixo, mas ocupante variável a critério do Joab. Hoje: Antigravity no `ftsalider`, Claude Code no `Teólogo 1`, Codex CLI no `Teólogo 2`, Antigravity no `Teólogo 3`, Cline no `comitador`, Shell/Agente no `file2md`. Se você (Qwen Code) for chamado para atuar no projeto, pergunte ao Joab ou ao ftsalider qual terminal você ocupa — nunca assuma um papel só por ser Qwen Code.
3. **Idioma:** toda comunicação, documentação e textos produzidos são em **português do Brasil**.
4. **`00_originais/` é imutável:** arquivos brutos recebidos nunca são alterados. Qualquer conversão/processamento gera novos arquivos em outra pasta.
5. **Fonte primária obrigatória (`fontes/`):** as notas em `ftsabrain/materias/<nome>/fontes/` são a base mandatória para qualquer análise ou rascunho. Busca externa é só complementar; em conflito, prevalece o material do curso.
6. **Ciclo de Humanização:** nenhum texto vai para `04_aprovados/` sem passar pelo Bereano (detector de IA) e, se reprovado, pelo Escriba em `03_revisao/` (versionado `v1.md`, `v2.md`...). Nunca sobrescrever versões anteriores.
7. **Memória de Trabalho:** progresso registrado em `ftsabrain/memoria/` (`00-registro-geral.md` + `materias/<nome>/registro.md`).
8. **`CHANGELOG.md` (raiz):** registre toda alteração de estrutura/arquivos (data/hora, motivo) antes de um commit ou ao finalizar a tarefa. Banco de consulta — não leia automaticamente ao iniciar sessão.
9. **`LESSONS.md` (raiz):** registre erros, acertos e pendências não resolvidas, no mesmo ritmo do changelog. Pode e deve ser consultado quando relevante.
10. **Linear (projeto `teoftsao`, workspace Joabse, time JOA):** banco de tarefas do projeto. Sempre que encontrar algo para resolver/executar no futuro, crie uma issue lá — não basta anotar em memória. Se você não tiver acesso à ferramenta do Linear, avise o ftsalider (Claude Code) para criar a issue por você.
11. **Sincronização multi-LLM:** este arquivo é um espelho de `AGENTS.md`/`ESTRUTURA.md`/`ORCA.md` para o Qwen Code. Outras ferramentas têm o seu: `CLAUDE.md` (Claude Code), `GEMINI.md` (Antigravity), `.clinerules` (Cline). Se você perceber que uma regra sua está desatualizada em relação a `AGENTS.md`/`ESTRUTURA.md`, avise o ftsalider para sincronizar todos os arquivos.

---

## 1. Estrutura de Diretórios do Workspace

```
teoftsao\
├── CLAUDE.md              ← wrapper para Claude Code
├── AGENTS.md              ← arquivo canônico (Codex CLI, opencode)
├── GEMINI.md              ← wrapper para Antigravity
├── QWEN.md                ← este arquivo (wrapper para Qwen Code)
├── .clinerules             ← wrapper para Cline
├── ESTRUTURA.md           ← detalhamento completo de papéis, pipeline e regras
├── ORCA.md                ← comandos e operação específica no Orca
├── CHANGELOG.md           ← banco de alterações estruturais (não ler automaticamente)
├── LESSONS.md             ← lições aprendidas (consultar quando relevante)
├── materias\              ← uma pasta por disciplina/matéria
│   ├── README.md          ← documentação do fluxo de matérias
│   ├── _TEMPLATE\         ← modelo de pastas para novas disciplinas
│   └── <nome>\
│       ├── 00_originais\  ← arquivos brutos recebidos (imutáveis)
│       ├── 01_markdown\   ← convertidos pelo file2md
│       ├── 02_rascunhos\  ← textos teológicos produzidos
│       ├── 03_revisao\    ← ciclo de humanização versionado (v1.md, v2.md...)
│       └── 04_aprovados\  ← entregas finais validadas
└── ftsabrain\             ← vault Obsidian ("cérebro" do projeto)
    ├── materias.md        ← MOC/índice geral das matérias
    ├── pipeline.md        ← resumo do pipeline de produção
    ├── materias\<nome>\   ← notas temáticas (00-visao-geral.md + fontes\)
    └── memoria\           ← memória de trabalho (registro-geral e por matéria)
```

---

## 2. Pipeline de Produção

```
Usuário envia materiais
         │
         ▼
materias\<nome>\00_originais\        (imutável)
         │  file2md converte
         ▼
materias\<nome>\01_markdown\         (Markdown pronto para estudo)
         │  Teólogos estudam e produzem rascunhos
         ▼
materias\<nome>\02_rascunhos\        (textos produzidos pelos teólogos)
         │
         ▼
╔═════════════ CICLO DE HUMANIZAÇÃO ═════════════╗
║  texto ──► Bereano (detector de IA)            ║
║       aprovado? ── SIM ──► 04_aprovados\       ║
║       │ NÃO                                    ║
║       ▼                                        ║
║  Escriba humaniza → nova versão em 03_revisao\ ║
║       └──► volta ao Bereano (repete até OK)    ║
╚═════════════════════════════════════════════════╝
         │
         ▼
materias\<nome>\04_aprovados\   → Entrega final ao Joab (via ftsalider)
```

---

## 3. Papéis da Equipe FTSA

**Papel = terminal, não LLM.** Papel fixo por terminal; ocupante pode mudar a critério do Joab.

| Terminal (papel) | Função Principal | Ocupante atual (2026-09-19) |
|---|---|---|
| **ftsalider** — Líder da equipe | Orquestra o fluxo, distribui tarefas, valida respostas e registra a memória. Não produz rascunhos teológicos diretamente. | Antigravity |
| **Teólogo 1** | Análise e produção teológica. | Claude Code (terminal dedicado) |
| **Teólogo 2** | Análise e produção teológica. | Codex CLI |
| **Teólogo 3** | Análise das fontes do curso, produção de rascunhos e reflexões teológicas. | Antigravity |
| **comitador** | Faz commits git a pedido do ftsalider, com a descrição que ele fornecer. | Cline (terminal dedicado, já aberto pelo Joab) |
| **file2md** | Converte originais para Markdown via `anydoc`/OCR, alimenta `ftsabrain/file2md/` e registra em `00-indice.md`. O líder sempre verifica modelo/CLI antes de despachar. | Shell / Agente dedicado no terminal `file2md` |

Outros agentes (sem terminal fixo entre os 6 nomeados):

| Agente | Papel | Função Principal |
|---|---|---|
| **Bereano** | Detector de IA | Avalia os textos contra padrões sintéticos de IA; aprova ou reprova. |
| **Escriba** | Humanizador | Reescreve textos reprovados pelo Bereano para garantir tom natural. |
| **tecfix** | Manutenção técnica | Ajustes de infraestrutura, ambiente Orca e organização de pastas. |

*(Se o Qwen Code for convocado para o projeto, confirme o nome do seu terminal antes de agir — não presuma um papel de teólogo por padrão só por ser Qwen Code.)*

---

## 4. Diretrizes Gerais

1. **Pesquisa Externa Complementar:** autonomia para consultar a Bíblia, comentários e léxicos via MCPs de busca ou browser do Orca (`orca tab`), sem autorização prévia. Sempre citar a fonte.
2. **Questões de Múltipla Escolha:** cada teólogo responde individualmente; o ftsalider consolida ao final uma tabela-resumo (nº da questão, resposta de cada teólogo, sugestão do líder). Tabela só depois de todas as questões respondidas.
3. **Registro de Atividades:** ao finalizar qualquer etapa relevante, documente no arquivo correspondente em `ftsabrain/memoria/`.
