---
tipo: registro
materia: geral
atualizado_em: 2026-09-18
tags:
  - memoria
---

# 🧠 Registro Geral do Projeto FTSA

> Memória de trabalho do projeto: log de atividades **gerais** (montagem, manutenção, mudanças estruturais). Logs de cada matéria ficam em `materias/<nome>/registro` (ex.: [[memoria/materias/biblia2/registro|Registro Bíblia 2]]).
> **Regra:** após cada etapa concluída e validada, o **ftsalider** registra a entrada aqui (ou no registro da matéria correspondente). Entradas em ordem cronológica decrescente (mais recente no topo).

---

## 2026-09-18 — Codex CLI — Projeto estruturado para execução do 2º teólogo

- **Matéria:** geral (infra/Codex) | **Status:** **CONFIGURADO** ✅
- **O que foi feito:** `AGENTS.md`, arquivo de instruções reconhecido automaticamente pelo Codex, foi complementado com o papel do Codex como 2º teólogo, procedimento de leitura do vault, destino obrigatório de rascunhos e regra de registro na memória. A configuração preserva o projeto sem Git e o pipeline FTSA.
- **Validação:** Codex CLI `0.155.0` está instalado; o projeto `E:\00_ATUAL\04_PROJETO\teoftsa` já consta como confiável no perfil local. Uma execução isolada confirmou que o agente recebe e interpreta as instruções de papel, fontes e ciclo Bereano→Escriba. O sandbox não interativo deste runtime bloqueia a chamada interna ao PowerShell para ler arquivos, limitação ambiental que não altera a configuração do projeto.
- **Como iniciar:** abrir um terminal na raiz e executar `codex`, ou criar a aba pelo Orca conforme `ORCA.md`.

## 2026-09-18 21:45 — Antigravity — Estrutura padrão do Antigravity configurada no projeto

- **Matéria:** geral (infra/antigravity) | **Status:** **CONFIGURADO** ✅
- **O que foi feito:** estruturação completa das pastas e arquivos padrão do Antigravity (`agy`): criação do diretório `.agents/skills/` com as skills do pipeline (`convert-documents-to-markdown`, `humanizer`, `no-ai-slop`), `.agents/rules/` com regras ativas (`regras-ftsa.md`), bloqueio de versão em `skills-lock.json`, e criação do arquivo raiz `GEMINI.md` detalhando o papel do 3º teólogo e links para a documentação do projeto.
- **Próxima etapa:** produção teológica ou processamento sob demanda.

## 2026-09-18 16:05 — Antigravity — Projeto preparado e integrado para uso com o Orca

- **Matéria:** geral (infra/orquestração) | **Status:** **INTEGRADO** ✅
- **O que foi feito:** verificado e validado o status do projeto no Orca CLI (já registrado como folder workspace `teoftsa`, host local pronto). Criado `ORCA.md` com guia operacional completo para a equipe FTSA no Orca (abertura de terminais para Claude Code, Codex CLI e Antigravity, browser integrado para pesquisa bíblica, isolamento de sessões do file2md). Atualizados `AGENTS.md`, `ESTRUTURA.md` e `ftsabrain/pipeline.md` com suporte e referências à operação no Orca.
- **Próxima etapa:** iniciar tarefas de produção ou conversão diretamente no Orca conforme direcionamento do Joab.

## 2026-09-13 21:55 — ftsalider — Bíblia 3 FECHADA · 26Q + 6R = 32 entregas · playbook de orquestração criado

- **Matéria:** geral (fechamento biblia3) | **Status:** **CONCLUÍDA** ✅
- **O que foi feito:** fechamento oficial da Bíblia 3 — 26 questões objetivas (Q1–Q26) + 6 reflexões (R1–R6) processadas, validadas e arquivadas em `materias\biblia3\04_aprovados\`. `00-visao-geral.md` da matéria atualizado para status **CONCLUÍDA**. Criado **`memory/playbook-novas-materias.md`** na memória de orquestração com todo o know-how replicável (workflows A/B, 3 tiques de IA, lições operacionais, padrões de arquivo, checklist pós-atividade).
- **Lições consolidadas:** Codex CLI pausado desde Q13 (workflow de 2 teólogos funciona); 3 reflexões passaram em 2 ciclos Bereano→Escriba (R4, R5) ou 1 ciclo + ajuste neutro (R6); regra de material prioritário do ftsabrain mantida em 100% das entregas.
- **Próxima etapa:** a critério do Joab — nova matéria, retomar Bíblia 2, ou produção de textos longos.

## 2026-09-13 10:50 — Joab — gbooklm REMOVIDO da equipe · 3 teólogos únicos definidos

- **Matéria:** geral | **Decisão do Joab:** "Lembrando que os teólogos são somente o Codex, claude e o Antigravity"
- **O que foi feito:** o próprio Joab removeu o gbooklm do time (slot `01a0973c-25e4-75f1-8b14-2d61ca165dd8`). Atualizei: `ESTRUTURA.md` (regra do gbooklm marcada como DESCONTINUADA), `pipeline.md` (Papéis sem gbooklm), `memory/equipe-ftsa-roster.md` (gbooklm movido para "Removidos"), `memory/fluxo-trabalho-ftsa.md` (linha do gbooklm riscada). **Equipe agora: 7 membros** (ftsalider, Claude Code, Codex CLI, Antigravity, escriba, tecfix, file2md, Bereano).
- **Próxima etapa:** a regra do gbooklm (NUNCA recebe conteúdo, só pergunta + nome do notebook) foi descontinuada. Se o Joab re-adicionar o gbooklm no futuro, restaurar a regra.

## 2026-09-13 10:20 — ftsalider — Regra de pesquisa na Bíblia (MCPs de busca) registrada

- **Matéria:** geral | **Decisão do Joab:** "caso precise consultar a Bíblia o teólogo está livre para buscar na internet com os nossos MCP de busca"
- **O que foi feito:** nova regra em `ESTRUTURA.md` ("Regra de pesquisa na Bíblia"), `ftsabrain\pipeline.md` (Papéis + Regras de ouro) e memória `fluxo-trabalho-ftsa.md`. Teólogos (Claude Code, Codex CLI, Antigravity, gbooklm) podem consultar a Bíblia via MCPs de busca **sem pedir autorização**; devem sempre citar a fonte. Notas de `fontes\` continuam como base primária.

## 2026-09-13 09:45 — ftsalider — Bíblia 3 FECHADA (27/27 notas) · gbooklm cancelado pelo Joab

- **Matéria:** geral | **Decisão:** "vamos deixar de lado o gbooklm"
- **O que foi feito:** task `[NT-gbooklm]` interrompida + deletada; pasta `fontes\gbooklm\` removida; visão-geral atualizada para `status: notas_prontas` com wikilinks das 27 notas. Inventário final: 11 PDFs (Claude Code) + 12 aulas (Codex CLI) + 4 extras (Antigravity) = **27 notas · 177.097 bytes**.
- **Próxima etapa:** definir com o Joab a produção de textos (escriba/Bereano) ou retomada da biblia2.

## 2026-09-13 08:50 — ftsalider — NotebookLM da biblia3 definido e despachado

- **Matéria:** biblia3 | **Task:** [NT-gbooklm]
- **O que foi feito:** notebook confirmado pelo Joab como **"Bíblia III - Introdução ao Novo Testamento"** (ele retificou após informar inicialmente "Psicologia da Religião" por engano). Despachado ao gbooklm com 4 blocos temáticos. **Posteriormente cancelado pelo Joab.**

## 2026-09-13 07:40 — ftsalider — Despacho da Bíblia 3 aos teólogos (etapa de produção iniciada)

- **Matéria:** geral (decisão do usuário: "Entregues para os teologos") | **Tasks:** 4 novas no board
- **O que foi feito:** divisão da biblia3 entre os teólogos para produção de **notas de estudo** (padrão unificado com frontmatter, H2 fixo, wikilinks): **Claude Code** → 11 PDFs (apostila + 10 adicionais → `fontes\pdfs\`); **Codex CLI** → 12 aulas de Lucas Merlo (T1-T12 → `fontes\aulas\`); **Antigravity** → 4 extras (T13-T16 → `fontes\extras\`); **gbooklm** → PAUSADO (tarefa `[NT-gbooklm]` no board, aguardando Joab indicar o nome do notebook). Pastas `fontes\pdfs`, `aulas`, `extras`, `gbooklm` criadas.
- **Próxima etapa:** consolidar as notas, atualizar a visão-geral e o MOC, e perguntar ao Joab o notebook do NotebookLM para o gbooklm.

## 2026-09-13 07:10 — ftsalider — Bíblia 3: fila de conversões CONCLUÍDA (11 PDFs + 16 transcrições)

- **Matéria:** geral | **Task:** [T16/16] fechada + consolidado geral
- **O que foi feito:** file2md entregou a T16/16 (diálogo "Profeta e luz no Ev. de João", 89 linhas) e o **consolidado geral das 16 transcrições**: 989 linhas / 189.502 bytes / 118 seções H2 / 0 U+FFFD em todos; 13 solos (Lucas Merlo) + 2 diálogos + 1 entrevista tripla; aulas 4, 8 e 12 não existem na pasta original. `00-visao-geral.md` atualizado para `status: fontes_prontas` com o índice completo das 16 transcrições.
- **Próxima etapa:** definir com o Joab o entregável dos teólogos (sugestão pendente: notas de estudo por aula/unidade em `ftsabrain\fontes\`) e lembrar da **regra do gbooklm** (só pergunta + nome do notebook — perguntar ao Joab).

## 2026-09-13 03:25 — tecfix — Linha "Isolamento por despacho" no prompt do file2md (persistida e verificada)

- **Matéria:** geral (equipe/infra) | **Task:** —
- **Conteúdo:** "Processe APENAS o arquivo da mensagem atual; ignore conversões anteriores nesta conversa. Cada despacho é uma ação independente — as instruções completas (origem, destino, escopo, formato do report) virão sempre na mensagem do líder." — mesma linha nas 3 variantes de locale (pt-BR, default, default sem sufixo; 5.855 bytes), `config assistants get` verificada (rules.content termina na nova linha; defaults intactos: model 9aionui, permission yolo, skills convert-documents-to-markdown, mcps [google-drive-upload, composio]).
- **Lições (tecfix, salvar para futuros edits de assistants):** (1) mexer em `rules.content` usa `config assistants rule write`, não `assistants update`; (2) `assistants update` substitui sub-objetos inteiros (defaults, rules) — sempre enviar o sub-objeto completo ou só campos não-aninhados; (3) `assistants get` mostra o locale default, mas o runtime usa o locale da UI (pt-BR) — conferir `*.pt-BR.md` no disco.
- **Vigência:** a regra vale a partir do **próximo despacho** recebido pelo file2md. Fila T2–T16 intocada.

## 2026-09-13 01:40 — tecfix + ftsalider — Diagnóstico: backend aionrs não suporta context reset (solução A autorizada)

- **Matéria:** geral (equipe/infra) | **Task:** —
- **Causa raiz (3 tentativas, RuntimeContextMissing):** `"Team member does not support context reset: 01a096e8-…"` — o backend aionrs (assistente custom do file2md) **não implementa** `team_clear_agent_context`. A tool é lead_only e chega ao executor, mas o backend recusa imediatamente (duration_ms: 0). Não é permissão nem runtime ocupado.
- **Solução A (autorizada pelo ftsalider):** 1 linha no system prompt do file2md — "processe APENAS o arquivo da mensagem atual; ignore conversões anteriores nesta conversa". O contexto LLM continua acumulando tokens, mas o agente trata cada arquivo isoladamente. O líder sempre reenvia instruções completas em cada despacho.
- **Plano B (reserva):** remover e re-adicionar o membro → contexto realmente zerado, mas a fila precisa ser reenviada item a item. Só usar se o acúmulo quebrar o file2md de fato.
- **Estado:** estrutura revisada (`ESTRUTURA.md`, `pipeline.md`, memória); tecfix aplicando a linha no prompt. Fila T2–T16 intocada.

## 2026-09-13 00:50 — ftsalider — Regra do contexto fresco por arquivo (file2md) [REVISADA]

- **Matéria:** geral (equipe/processo) | **Task:** —
- **Definição do Joab:** cada conversão do file2md é uma **ação independente**. Tentativa inicial: limpar contexto via `team_clear_agent_context` — **falhou** (backend aionrs não suporta). Solução A (prompt + despachos autocontidos) adotada — ver entrada 01:40 acima.
- **Onde foi registrado:** `ESTRUTURA.md` (regra revisada), `ftsabrain\pipeline.md`, memória AppData (fluxo + roster).

## 2026-09-12 23:40 — ftsalider — Ajuste no fluxo do gbooklm (definido pelo Joab)

- **Matéria:** geral (equipe/processo) | **Task:** —
- **O que foi feito:** Joab definiu nova regra para o **gbooklm (4º teólogo)**: ele **já possui todo o conteúdo** enviado aos demais teólogos — **nunca mais se envia conteúdo/arquivos a ele**. A delegação passa a conter **apenas a pergunta/tarefa + o NOME do notebook do NotebookLM** em que ele deve consultar; esse nome **somente o Joab sabe**, então o líder **sempre pergunta a ele** antes de delegar ao gbooklm (sem indicação = tarefa do gbooklm pausada; demais teólogos seguem).
- **Onde foi registrado:** `ESTRUTURA.md` (regra especial do gbooklm + tabela de papéis), `ftsabrain\pipeline.md` (papéis + regras de ouro), memória AppData (fluxo-trabalho-ftsa.md + equipe-ftsa-roster.md).

## 2026-09-12 23:10 — tecfix — Diagnóstico e correção do assistente "arquivista" (aguardando re-adição pelo Joab)

- **Matéria:** geral (equipe/infra) | **Task:** —
- **Causa raiz (logs aioncore):** `runtime_start_failed ... Bad request: Provider 'aionrs' not found` — o assistente custom do arquivista estava com `defaults.model = auto`, resolvendo para provider "aionrs"/modelo "default" inexistente; o runtime do membro nunca subia (status error, mensagens falhavam). Todos os demais custom saudáveis usam modelo **fixado "9aionui"**.
- **Correções aplicadas pelo tecfix (persistidas):** `defaults.model` → `fixed: "9aionui"`; efeito colateral corrigido no mesmo passe (reset de `defaults.mcps` restaurado para fixed: notion + abrain-filesystem). Estado final verificado: assistente enabled, team_selectable, regra intacta, MCPs fixados.
- **Pendente (ação do Joab na UI):** re-adicionar o membro "arquivista" ao time teoftsa (o slot foi removido durante o diagnóstico; o assistente em si está saudável). Pós-adição: conferir que o roster mostra model **"9aionui"** (se mostrar "default", chamar o tecfix); depois mensagem-teste.

## 2026-09-12 22:45 — ftsalider — Novo membro "arquivista" adicionado e removido (falha de inicialização)

- **Matéria:** geral (equipe) | **Task:** —
- **O que foi feito:** Joab adicionou manualmente o membro **arquivista** (slot_id 01a097f3-ef56-79b0-ada1-c469dacae84a), que ficou em **status: error** — 2 tentativas de briefing via team_send_message falharam ("local team tool returned an error"). Diagnóstico delegado ao tecfix, mas o agente foi **removido da equipe** pouco depois (mesmo dia), encerrando o incidente. Roster de memória atualizado com registro da remoção; se for re-adicionado, refazer o briefing.
- **Resultado/Local:** memória AppData `equipe-ftsa-roster.md` atualizada; nenhum impacto no fluxo (fila biblia3 segue com file2md)

## 2026-09-12 15:20 — tecfix — Organização do vault ftsabrain por matéria (horário aproximado)

- **Matéria:** geral (todas) | **Task:** Organizar vault ftsabrain (cérebro do projeto) por matéria
- **O que foi feito:** vault reorganizado como cérebro do projeto — notas principais `00-visao-geral.md` (biblia2 e _TEMPLATE), pastas `fontes\` por matéria, `materias.md` convertido em MOC com wikilinks, ESTRUTURA.md atualizado.
- **Resultado/Local:** `ftsabrain\materias\biblia2\00-visao-geral.md`, `ftsabrain\materias\_TEMPLATE\`, `ftsabrain\materias.md`, `ESTRUTURA.md`

## 2026-09-12 15:00 — tecfix — Documentação do gbooklm como 4º teólogo (horário aproximado)

- **Matéria:** geral (documentação do projeto) | **Task:** Atualizar documentação: gbooklm como 4º teólogo da equipe FTSA
- **O que foi feito:** gbooklm incluído como Teólogo na tabela de papéis (ESTRUTURA.md), nas listas de teólogos do pipeline (ftsabrain\pipeline.md, etapa 3 e seção Papéis) e na linha da pasta 02_rascunhos (materias\README.md).
- **Resultado/Local:** `ESTRUTURA.md`, `ftsabrain\pipeline.md`, `materias\README.md`

## 2026-09-12 14:50 — tecfix — Montagem da estrutura do projeto FTSA (horário aproximado)

- **Matéria:** geral (todas) | **Task:** Montagem da estrutura do projeto FTSA (pastas, pipeline e documentação)
- **O que foi feito:** criado o fluxo padronizado de matérias (00_originais → 04_aprovados) em `materias\biblia2\`, `_TEMPLATE` para novas matérias, e a documentação base (ESTRUTURA.md, materias\README.md, ftsabrain\pipeline.md, ftsabrain\materias.md).
- **Resultado/Local:** raiz do projeto `E:\00_ATUAL\04_PROJETO\teoftsa\`

> ⚠️ Entradas semeadas na criação desta memória (2026-09-12); horários aproximados. Todas as etapas executadas por **tecfix** e validadas por **ftsalider**.
