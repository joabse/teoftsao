# CLAUDE.md — Projeto teoftsao

> Este arquivo é carregado automaticamente pelo Claude Code no início de cada sessão neste diretório. Consolida `AGENTS.md`, `ESTRUTURA.md` e `ORCA.md` para que o Claude Code opere corretamente sem precisar reler os três arquivos separadamente. **Seu papel neste projeto (ftsalider ou Teólogo) depende do terminal em que você está, não do fato de você ser Claude Code** — ver regra 2. Em caso de dúvida ou divergência, os arquivos originais (`AGENTS.md`, `ESTRUTURA.md`, `ORCA.md`) são a fonte de verdade.

## 0. Regras críticas (leia antes de qualquer ação)

1. **Sem VCS tradicional.** Este projeto NÃO usa git — é gerenciado como pasta/worktree no Orca. Nunca rode `git init`, `git add`, commits etc. aqui, a menos que o usuário peça explicitamente.
2. **Papéis pertencem ao TERMINAL, não à LLM (Joab, 2026-09-19).** O projeto roda em 4 terminais nomeados no Orca: **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3**. O papel de cada terminal é fixo (ver seção 4); **quem ocupa cada terminal pode mudar** — o Joab pode colocar qualquer LLM em qualquer terminal (ex.: Codex no terminal `ftsalider`, Claude Code no `Teólogo 2`). Ocupação atual (2026-09-19): `ftsalider` = Claude Code, `Teólogo 1` = Claude Code, `Teólogo 2` = Codex CLI, `Teólogo 3` = Antigravity — mas isso é um estado, não uma regra fixa. **Nunca assuma seu papel só porque você é Claude Code** — confirme em qual terminal está (nome do terminal no Orca) ou pergunte ao Joab/ftsalider antes de agir.
3. **Idioma:** todo conteúdo e documentação produzidos são em **português brasileiro**.
4. **`00_originais/` é imutável.** Qualquer transformação de um arquivo original gera um novo arquivo em outra pasta — nunca sobrescreva ou edite um original.
5. **Fonte primária = material enviado.** As notas em `ftsabrain/materias/<nome>/fontes/` (extraídas dos originais do usuário) são a fonte mandatória e prioritária para qualquer resposta teológica. Busca externa (web, MCPs bíblicos) é só complementar, e em caso de conflito o material enviado prevalece — a menos que o usuário (Joab) diga o contrário.
6. **Sem memória automática de progresso.** Como não há git, o único jeito de rastrear o que foi feito é registrar em `ftsabrain/memoria/` (ver seção 5). Quem registra formalmente é você mesmo (o ftsalider), após validar a conclusão de cada etapa — própria ou de outro agente.
7. **Nunca sobrescreva versões em `03_revisao/`** — cada nova versão do ciclo de humanização é um arquivo novo (`v1.md`, `v2.md`, ...).
8. **`CHANGELOG.md` (raiz) — obrigatório antes de cada commit/finalização de tarefa.** Registre toda alteração feita na estrutura ou nos arquivos do projeto, com data/hora e o motivo que originou a mudança (ver seção 10). É um banco de dados de consulta, **não leia `CHANGELOG.md` automaticamente** ao iniciar a sessão nem para responder perguntas gerais — consulte-o só quando precisar reconstruir um histórico específico ou quando o Joab pedir.
9. **`LESSONS.md` (raiz) — registre erros, acertos e pendências não resolvidas.** Sempre que você (ou outro agente) errar algo, corrigir algo, ou não conseguir resolver um problema, registre em `LESSONS.md` (ver seção 10). Ao contrário do `CHANGELOG.md`, este arquivo **pode e deve ser consultado** quando for relevante para a tarefa atual.
10. **Sempre que encontrar algo para resolver/executar no futuro, crie uma tarefa no Linear.** Projeto `teoftsao` (workspace Joabse, time JOA) no Linear (ferramentas `mcp__claude_ai_Linear__*`) é o gerenciador de tarefas do projeto. Toda pendência, decisão a tomar, bug, ou trabalho futuro que você identificar (não só o que o Joab pedir diretamente) deve virar uma issue lá com `save_issue` — não basta anotar em memória/changelog/lessons. Ver seção 11.
11. **Sincronize os arquivos de todas as LLMs sempre que alterar regras/estrutura.** Além deste `CLAUDE.md`, existem wrappers equivalentes para outras ferramentas: `AGENTS.md` (canônico — Codex CLI, opencode), `GEMINI.md` (Antigravity), `QWEN.md` (Qwen Code), `.clinerules` (Cline). `mmx` não é um agente que leia arquivos de projeto (é a CLI da MiniMax para configurar outros agentes) — não tem wrapper. Kimi Code e DeepSeek foram removidos/não são usados no projeto (Joab, 2026-09-19, JOA-19). Toda vez que você mudar uma regra crítica, papel da equipe, estrutura de pastas ou pipeline aqui, **propague a mesma mudança para todos os wrappers existentes** — nenhuma LLM que trabalhar neste projeto deve ver uma versão desatualizada ou divergente das regras. Ver seção 12.

## 1. Visão geral do projeto

O `teoftsao` é o workspace de uma equipe de agentes de IA (**FTSA — Fluxo de Trabalho de Textos com Agentes**) que produz **textos teológicos de qualidade humana** a partir de materiais de estudo (apostilas, livros, transcrições de aulas) enviados pelo usuário (Joab). A equipe é coordenada no **Orca**, em 4 terminais nomeados cujos papéis são fixos — **ftsalider** (orquestrador), **Teólogo 1**, **Teólogo 2**, **Teólogo 3** — mas cuja **LLM ocupante pode mudar** a critério do Joab. Hoje (2026-09-19): Claude Code no `ftsalider` e no `Teólogo 1`, Codex CLI no `Teólogo 2`, Antigravity no `Teólogo 3`.

Não é um projeto de software: não há build, testes ou dependências no sentido tradicional. O "produto" é texto (Markdown) em português, revisado por um ciclo de detecção/humanização de IA.

## 2. Estrutura de diretórios

```
teoftsao\
├── CLAUDE.md             ← este arquivo (carregado automaticamente pelo Claude Code)
├── AGENTS.md              ← wrapper canônico (Codex CLI, opencode)
├── GEMINI.md              ← wrapper para o Antigravity
├── QWEN.md                ← wrapper para o Qwen Code
├── .clinerules             ← wrapper para o Cline
├── ESTRUTURA.md           ← detalhamento completo de papéis, pipeline e regras
├── ORCA.md                ← comandos e operação específica no Orca
├── CHANGELOG.md           ← banco de alterações estruturais (não ler automaticamente)
├── LESSONS.md             ← lições aprendidas (consultar quando relevante)
├── materias\               ← uma pasta por disciplina/matéria
│   ├── README.md           ← documentação do fluxo de matérias
│   ├── _TEMPLATE\          ← modelo de pastas para criar nova matéria
│   ├── biblia2\            ← matéria "Bíblia 2"
│   ├── biblia3\            ← matéria "Bíblia 3" (contém também scripts .py avulsos de OCR)
│   └── <nome>\
│       ├── 00_originais\   ← arquivos enviados pelo usuário — IMUTÁVEL
│       ├── 01_markdown\    ← convertidos pelo agente file2md
│       ├── 02_rascunhos\   ← textos produzidos pelos teólogos
│       ├── 03_revisao\     ← ciclo de humanização, versionado (v1.md, v2.md, ...)
│       └── 04_aprovados\   ← entrega final, aprovada pelo Bereano
└── ftsabrain\              ← vault Obsidian, o "cérebro" do projeto
    ├── Bem-vindo.md
    ├── materias.md         ← MOC/índice geral das matérias
    ├── pipeline.md         ← resumo do pipeline de produção
    ├── materias\<nome>\    ← notas de conhecimento extraídas (00-visao-geral.md + fontes\)
    └── memoria\
        ├── 00-registro-geral.md      ← log de atividades gerais
        └── materias\<nome>\registro.md ← log por matéria
```

Nova matéria: copiar `materias\_TEMPLATE\` e registrar em `ftsabrain\materias.md` (detalhes em `materias\README.md`).

## 3. Pipeline de produção de conteúdo

```
Usuário envia materiais da matéria
        │
        ▼
materias\<nome>\00_originais\        (imutável)
        │  file2md converte
        ▼
materias\<nome>\01_markdown\         (Markdown pronto para análise)
        │  teólogos analisam e escrevem
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
materias\<nome>\04_aprovados\   → Entrega ao usuário (via ftsalider)
```

Regras do ciclo:
1. Todo texto produzido pelos teólogos passa **obrigatoriamente** pelo Bereano.
2. Reprovado → Escriba humaniza → nova versão numerada em `03_revisao\` (nunca sobrescrever) → volta ao Bereano.
3. Repete até aprovação; só então vai para `04_aprovados\`.

## 4. Equipe de agentes e papéis

**Os 4 papéis abaixo pertencem ao terminal (nome fixo no Orca), não à LLM.** A coluna "Ocupante atual" é um estado — o Joab pode trocá-lo a qualquer momento, sem que o papel/responsabilidade do terminal mude.

| Terminal (papel) | Responsabilidade | Ocupante atual (2026-09-19) |
|---|---|---|
| **ftsalider** — Líder/Orquestrador | Coordena os 3 teólogos, distribui tarefas, valida entregas com o usuário, registra na memória. **Não produz rascunhos teológicos diretamente** (só sob pedido explícito do Joab ou indisponibilidade dos teólogos). | Claude Code |
| **Teólogo 1** | Analisa materiais em `fontes\` e produz rascunhos em `02_rascunhos\`. | Claude Code (terminal dedicado, separado do ftsalider) |
| **Teólogo 2** | Idem | Codex CLI |
| **Teólogo 3** | Idem | Antigravity |

Outros agentes, sem terminal fixo dedicado dentre os 4 nomeados:

| Agente | Papel | Responsabilidade |
|---|---|---|
| **file2md** | Conversor | Converte originais (PDF, DOCX, PPTX etc.) para Markdown em `01_markdown\` |
| **Bereano** | Detector de IA | Aprova/reprova textos no ciclo de humanização |
| **Escriba** | Humanizador | Humaniza textos reprovados pelo Bereano |
| **tecfix** | Manutenção técnica | Estrutura de pastas, configuração, infraestrutura do Orca — não produz conteúdo teológico |

**Antes de agir, confirme seu papel pelo terminal em que você está** (nome do terminal no Orca), não pela sua identidade de ferramenta — a mesma LLM pode ser ftsalider num terminal e Teólogo em outro (é o caso do Claude Code hoje), e o Joab pode reatribuir qualquer terminal a qualquer LLM. Questões e produção teológica vão para os 3 terminais de Teólogo; o ftsalider consolida e valida. (Estrutura de 4 terminais nomeados definida pelo Joab em 2026-09-19; papéis desacoplados de LLM específica em 2026-09-19, mesmo dia — ver `ESTRUTURA.md` para o histórico completo. O agente `gbooklm`/NotebookLM foi **removido** pelo usuário em 2026-09-13.)

## 5. Memória de trabalho (`ftsabrain\memoria\`)

Como não há git, a memória do vault é a única forma de rastrear progresso:
- Atividades **gerais** (montagem, manutenção, mudanças estruturais) → `ftsabrain\memoria\00-registro-geral.md`.
- Atividades de uma **matéria** → `ftsabrain\memoria\materias\<nome>\registro.md`.
- Formato: frontmatter `tipo: registro` + entradas cronológicas (mais recente no topo) com agente, tarefa, o que foi feito e local do produto gerado.
- Quem registra formalmente: **quem estiver no terminal ftsalider** (hoje Claude Code — ver seção 4), após validar a conclusão da etapa — própria ou de Teólogo 1/2/3/qualquer outro agente.

## 6. Regra de pesquisa bíblica (Teólogos 1, 2 e 3)

1. Prioridade absoluta é o material enviado em `fontes\` — busca externa é só complementar, para confirmar/verificar.
2. Podem buscar a Bíblia (texto, comentários, léxicos) via MCPs de busca ou pelo browser integrado do Orca (`orca tab`) sem pedir autorização.
3. Em caso de conflito, prevalece o material enviado.
4. Sempre indicar a fonte da consulta externa (URL, obra, autor) na resposta ao usuário.

## 7. Questões de múltipla escolha

Quando o usuário enviar questões de múltipla escolha, Teólogo 1, Teólogo 2 e Teólogo 3 respondem individualmente; o ftsalider consolida ao final uma tabela-resumo com: nº da questão, resposta de cada teólogo (A/B/C/D/E), e a sugestão do líder (letra + justificativa em 1 linha, citando `fontes\` e/ou fonte externa). A tabela vem **depois** de todas as questões respondidas, nunca intercalada.

## 8. Scripts de processamento (`materias\biblia3\*.py`)

Scripts Python autônomos e de uso único para reparo de OCR e consolidação de capítulos (prefixos `_consolida_`, `_repara_`, `_fix`, `_diag`, `_dbg`). Cada um tem caminhos absolutos Windows hardcoded para um arquivo específico. Executar individualmente com `python <script>.py`; **não** usar como base para uma ferramenta genérica sem adaptar os caminhos.

## 9. Operação no Orca (resumo — detalhes em `ORCA.md`)

- Projeto registrado no Orca como repositório de pasta (`teoftsao`).
- 4 terminais nomeados no Orca, com papel fixo e ocupante variável (ver seção 4): **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3**. Ocupação atual: Claude Code (`ftsalider` e `Teólogo 1`), `codex` (`Teólogo 2`), `agy`/Antigravity (`Teólogo 3`). O ftsalider cria/gerencia os terminais dos teólogos: `orca terminal create --title "Teologo 2" --command "codex"` (idem para `agy` ou `claude`, dependendo de quem o Joab designar).
- Navegador integrado para pesquisa bíblica: `orca tab create --url "..."`, `orca snapshot`.
- Contexto isolado para conversões do file2md: criar terminal novo por conversão.

## 10. `CHANGELOG.md` e `LESSONS.md` (raiz do projeto)

Duas ferramentas de rastreio complementares à memória do `ftsabrain/` (que é sobre **conteúdo teológico**; estas duas são sobre **o projeto em si** — estrutura, arquivos, processo).

### `CHANGELOG.md` — banco de dados de alterações estruturais

- Registra **o que mudou** na estrutura/arquivos do projeto: data/hora, agente e motivo.
- **Nunca leia este arquivo automaticamente** ao iniciar sessão ou para responder perguntas gerais — ele não é contexto de trabalho, é um log de consulta. Só abra quando precisar reconstruir um histórico específico ou quando o Joab pedir algo do histórico.
- Toda LLM/agente que alterar estrutura ou arquivos do projeto adiciona uma entrada **antes do commit** ou **ao finalizar a tarefa** (o que vier primeiro). Nunca apague ou reescreva entradas antigas — só o Joab pode autorizar isso explicitamente.
- Formato de entrada: `## AAAA-MM-DD HH:MM — <agente> — <resumo>` seguido de **Motivo**, **O que mudou** e **Local**.

### `LESSONS.md` — lições aprendidas

- Registra erros, acertos e pendências não resolvidas durante o trabalho, para orientar a própria LLM ou outra sessão/LLM no futuro.
- Ao contrário do `CHANGELOG.md`, **pode e deve ser consultado** quando for relevante para a tarefa atual (ex.: antes de repetir uma ação que já deu problema).
- Registre sempre que: algo deu errado e foi corrigido; uma abordagem não-óbvia funcionou; ou um problema ficou pendente. Mesmo ritmo do changelog — antes do commit ou ao finalizar a tarefa.
- Formato de entrada: `## AAAA-MM-DD — <agente> — <resumo>` seguido de **O que aconteceu**, **Erro/acerto**, **Correção/solução** e **Lição**. Não apague entradas; se uma lição ficar obsoleta, marque `~~DESCONTINUADA~~` com data e motivo, mas mantenha o registro.

## 11. Linear — banco de tarefas do projeto (Joab, 2026-09-19)

- **Projeto:** `teoftsao`, workspace **Joabse**, time **JOA** (ferramentas `mcp__claude_ai_Linear__*`). É o gerenciador de tarefas oficial do projeto — diferente da memória (`ftsabrain/memoria/`, que é log de **conteúdo teológico já feito**) e do `CHANGELOG.md`/`LESSONS.md` (histórico e lições). O Linear é para **trabalho futuro/pendente**.
- **Regra-chave: crie a tarefa você mesmo, proativamente.** Sempre que, durante qualquer trabalho, você (ftsalider ou qualquer teólogo) identificar algo que precisa ser resolvido ou executado depois — uma pendência, uma divergência encontrada em auditoria, uma decisão que falta tomar, um próximo passo óbvio — crie uma issue no Linear com `save_issue` (`team: "Joabse"`, `project: "teoftsao"`). Não espere o Joab pedir; e não deixe a pendência só documentada em memória/changelog — ela tem que aparecer como tarefa executável.
- **Formato da issue:**
  - `title`: prefixo da matéria/área entre colchetes + resumo (ex.: `[Bíblia 2] Extrair notas de fontes\...`).
  - `description`: contexto (o que foi encontrado, onde), ação necessária em passos, e referência ao arquivo/memória de onde veio.
  - `priority`: 1=Urgent, 2=High, 3=Medium, 4=Low (default 0=None se não tiver certeza).
  - `state`: `Todo` se já executável agora; `Backlog` se depende de algo antes.
- Antes de começar uma sessão de trabalho, é uma boa prática dar `list_issues` no projeto `teoftsao` para ver o que está pendente. Ao concluir uma issue, atualize seu `state` para `Done` (ou `Canceled`) via `save_issue` com o `id`.

## 12. Sincronização multi-LLM (Joab, 2026-09-19)

O projeto precisa ser entendido por **qualquer LLM** que trabalhe nele, não só você (Claude Code). Isso surgiu de um pedido explícito: "gostaria que as demais LLMs também pudessem entender o projeto... garanta que o líder sempre que mexer na estrutura do projeto atualize para as demais LLMs entenderem e sigam as mesmas regras e execuções que o Claude tem."

Esta tabela é sobre **qual arquivo cada ferramenta lê** — é ortogonal à seção 4 (que é sobre **qual papel cada terminal tem**). Uma LLM lê sempre o mesmo arquivo (pela sua identidade de ferramenta), mas seu papel no projeto (ftsalider ou Teólogo) depende de qual terminal ela está ocupando no momento — os dois eixos não se confundem.

**Arquivos de instrução por ferramenta:**

| Arquivo | Ferramenta(s) |
|---|---|
| `CLAUDE.md` | Claude Code (este arquivo) |
| `AGENTS.md` | **Canônico** — Codex CLI, opencode |
| `GEMINI.md` | Antigravity |
| `QWEN.md` | Qwen Code |
| `.clinerules` | Cline |
| *(sem wrapper)* | **mmx** — não lê arquivos de projeto; é a CLI da MiniMax para configurar outros agentes (Claude Code, Codex, opencode, grok, hermes, pi) a usar modelos MiniMax |
| *(removidos)* | **Kimi Code, DeepSeek** — não usados no projeto (Joab, 2026-09-19, JOA-19) |

**Regra permanente:** sempre que você (ftsalider) — ou qualquer agente — alterar uma regra crítica, papel da equipe, estrutura de pastas ou pipeline em `CLAUDE.md`, `AGENTS.md`, `ESTRUTURA.md` ou `ORCA.md`, **propague a mesma mudança para todos os arquivos da tabela acima**, mesmo que a ferramenta correspondente não esteja ativa no momento. O objetivo é que, se qualquer uma dessas LLMs for chamada para trabalhar no projeto (mesmo pela primeira vez), ela encontre as regras e a execução atualizadas, iguais às suas.

Se uma ferramenta nova aparecer sem arquivo de convenção conhecido, ela deve encontrar orientação em `AGENTS.md` (o padrão de fato mais disseminado). Se depois descobrirmos que ela tem convenção própria, crie o wrapper correspondente e registre no `CHANGELOG.md`.
