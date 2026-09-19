---
tipo: registro
materia: geral
atualizado_em: 2026-09-19
tags:
  - memoria
---

# 🧠 Registro Geral do Projeto FTSA

> Memória de trabalho do projeto: log de atividades **gerais** (montagem, manutenção, mudanças estruturais). Logs de cada matéria ficam em `materias/<nome>/registro` (ex.: [[memoria/materias/biblia2/registro|Registro Bíblia 2]]).
> **Regra:** após cada etapa concluída e validada, o **ftsalider** registra a entrada aqui (ou no registro da matéria correspondente). Entradas em ordem cronológica decrescente (mais recente no topo).

---

## 2026-09-19 11:38 — Claude Code — Estrutura de 4 terminais nomeados no Orca: ftsalider + Teólogo 1/2/3, testada e confirmada

- **Matéria:** geral (equipe/processo) | **Status:** **CONCLUÍDO** ✅
- **Decisão do Joab:** renomeou os terminais do Orca para `ftsalider`, `Teólogo 1`, `Teólogo 2` e `Teólogo 3`. Teólogo 1 é feito também pelo Claude Code (em outro terminal); Teólogo 2 é o Codex CLI; Teólogo 3 é o Antigravity. O ftsalider (este terminal) lidera os 3, enviando demandas e recebendo respostas. Pediu para testar a configuração dando um "olá" aos teólogos.
- **O que foi feito:** localizei os terminais do projeto via `orca terminal list`/`read` e enviei mensagens de teste via `orca terminal send` aos 3 teólogos. **Codex CLI (Teólogo 2)** e **Antigravity (Teólogo 3)** confirmaram normalmente. **Teólogo 1 (outra instância de Claude Code)** recusou assumir o papel, corretamente, porque o `CLAUDE.md` que ele tinha carregado ainda dizia que Claude Code é só ftsalider — pediu confirmação com o Joab antes de agir (ver `LESSONS.md`, entrada de acerto). Atualizei `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`, `ftsabrain/pipeline.md`, `ftsabrain/materias.md` e `materias/README.md` para documentar a estrutura de 4 terminais: Claude Code ocupa dois papéis em terminais diferentes (ftsalider por padrão; Teólogo 1 só quando designado explicitamente no terminal), Codex CLI = Teólogo 2, Antigravity = Teólogo 3. A regra anterior (só 2 teólogos, sem Claude Code) foi arquivada como histórico em `ESTRUTURA.md`, não apagada.
- **Próxima etapa:** o Teólogo 1 (outro terminal) já pode assumir o papel — a documentação está atualizada; se ele reler o `CLAUDE.md`/`AGENTS.md` ou for informado disso, deve aceitar produzir rascunhos normalmente.
- **Resultado/Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`); `ftsabrain/pipeline.md`, `ftsabrain/materias.md`, `materias/README.md`; `CHANGELOG.md`, `LESSONS.md`.

## 2026-09-19 11:27 — Claude Code — Passa a ser o ftsalider (líder/orquestrador de todo o projeto)

- **Matéria:** geral (equipe/processo) | **Status:** **CONCLUÍDO** ✅
- **Decisão do Joab:** "Você sempre será o ftsalider, aqui no Orca. Estruture para isso. O orquestrador de todo o projeto." Confirmado em seguida: a mudança vale para o projeto todo (dentro e fora do Orca), e o Claude Code passa a **só orquestrar** — deixa de produzir rascunhos teológicos diretamente.
- **O que foi feito:** Claude Code sai da lista de teólogos e assume formalmente o papel de **ftsalider**: coordena Codex CLI e Antigravity, distribui tarefas, valida entregas com o Joab, consolida tabelas de múltipla escolha e registra a memória. Os teólogos de produção de conteúdo passam a ser **somente Codex CLI (1º) e Antigravity (2º)**. Atualizados `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`, `ftsabrain/pipeline.md`, `ftsabrain/materias.md` e `materias/README.md`. A regra antiga ("teólogos = Claude Code + Codex CLI + Antigravity") foi arquivada como histórico em `ESTRUTURA.md`, não apagada — segue o mesmo padrão usado para a descontinuação do gbooklm.
- **Próxima etapa:** a partir de agora, delegar produção teológica a Codex CLI e/ou Antigravity (via terminais do Orca ou pedido direto), reservando produção própria só para pedido explícito do Joab ou indisponibilidade dos teólogos.
- **Resultado/Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`); `ftsabrain/pipeline.md`, `ftsabrain/materias.md`, `materias/README.md`.

## 2026-09-19 11:21 — Codex CLI (2º teólogo) — Auditoria de prontidão para próximas execuções

- **Matéria:** geral (documentação operacional) | **Status:** **CONCLUÍDO** ✅
- **O que foi feito:** conferidas as regras do projeto, o pipeline, o estado das matérias e os inventários de arquivos. As referências operacionais ativas ao agente removido `gbooklm` foram corrigidas em `ftsabrain\pipeline.md`, `ftsabrain\materias.md` e `materias\README.md`. O MOC passou a refletir o estado real: Bíblia 2 tem Markdown convertido, porém ainda não tem notas em `fontes\`; Bíblia 3 está concluída, mas exige conferência do inventário de aprovados.
- **Pendência identificada:** o histórico da Bíblia 3 declara 32 entregas (Q1–Q26 e R1–R6), enquanto `materias\biblia3\04_aprovados\` contém 27 arquivos (Q6–Q26 e R1–R6). Os arquivos Q1–Q5 não foram localizados no workspace e não foram recriados nem removidos nesta auditoria.
- **Resultado/Local:** `ftsabrain\pipeline.md`, `ftsabrain\materias.md`, `materias\README.md`, `ftsabrain\materias\biblia3\00-visao-geral.md`.

## 2026-09-19 11:15 — Claude Code — Criadas as funcionalidades CHANGELOG.md e LESSONS.md

- **Matéria:** geral (infra/processo) | **Status:** **CONCLUÍDO** ✅
- **O que foi feito:** o Joab pediu duas funcionalidades que o projeto ainda não tinha: um changelog de alterações estruturais/arquivos (banco de consulta, não deve ser lido automaticamente pela LLM) e um registro de lições aprendidas (erros, acertos, pendências, consultável pela LLM quando relevante). Criados `CHANGELOG.md` e `LESSONS.md` na raiz do projeto, cada um com regra de formato e uso no topo do próprio arquivo. `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` e `ESTRUTURA.md` atualizados com as novas regras críticas e uma seção explicando os dois arquivos, para que todos os teólogos (Claude Code, Codex CLI, Antigravity) sigam o mesmo processo: registrar em ambos os arquivos antes de um commit ou ao finalizar uma tarefa.
- **Resultado/Local:** `CHANGELOG.md`, `LESSONS.md` (raiz); `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`.

## 2026-09-19 — Claude Code — Removidas todas as referências ao AionUi e Maestri (pedido explícito do Joab)

- **Matéria:** geral (infra/documentação) | **Status:** **CONCLUÍDO** ✅
- **O que foi feito:** Maestri não tinha nenhuma referência no projeto (nada a remover). AionUi foi removido de `CLAUDE.md`, `AGENTS.md`, `ESTRUTURA.md` e `ftsabrain/pipeline.md` (equipe agora descrita como coordenada só no Orca; papel do tecfix sem menção a AionUi). Removida a subseção "backend aionrs não suporta context reset" de `ESTRUTURA.md` e `ftsabrain/pipeline.md`. Em `ftsabrain/memoria/00-registro-geral.md`, excluídas por completo 4 entradas históricas inteiramente sobre mecânica interna do AionUi (assistants/aioncore/aionrs/modelo "9aionui"/membro "arquivista"), a pedido do Joab (removeu inclusive histórico, diferente do padrão usual de preservar registros antigos). Em `ftsabrain/memoria/materias/biblia3/registro.md`, 3 menções pontuais a ferramentas internas do AionUi (`team_clear_agent_context`, `team_interrupt_agent`) foram reescritas de forma genérica, mantendo o restante do relato (instabilidade do Codex CLI) intacto.
- **Observação:** diferente da renomeação `teoftsa→teoftsao` (entrada abaixo), aqui o próprio Joab pediu para apagar também o histórico de memória, não apenas atualizar a documentação ativa.

## 2026-09-19 — Claude Code — Projeto e repositório renomeados de `teoftsa` para `teoftsao`

- **Matéria:** geral (infra/vcs) | **Status:** **CONCLUÍDO** ✅
- **O que foi feito:** atendendo à solicitação do Joab, todas as referências ao nome antigo do projeto (`teoftsa`) foram atualizadas para `teoftsao` em `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md` e nos caminhos absolutos hardcoded dos scripts de `materias/biblia3/` (`_consolida_08.py`, `_consolida_04_alter.py`, `_fix08.py`). O remote `origin` do git foi trocado para o novo repositório e feito o primeiro commit/push no novo endereço. A regra de `.claude/settings.json` que bloqueava `Bash(git *)` foi removida a pedido explícito do usuário, já que o projeto usa git nesta pasta.
- **Repositório remoto (novo):** `https://github.com/joabse/teoftsao.git`
- **Observação:** entradas anteriores desta memória que citam `teoftsa`/`joabse/teoftsa` foram mantidas como registro histórico do estado do projeto na época — não foram reescritas.

## 2026-09-18 22:15 — opencode (2º teólogo, pedido explícito do Joab) — Projeto preparado para uso com o opencode

- **Matéria:** geral (infra/opencode) | **Status:** **CONFIGURADO** ✅
- **O que foi feito:** criação da configuração do opencode no projeto: `opencode.json` (schema oficial, agente padrão `teologo`, permissões — negados edit em `00_originais/` e `_TEMPLATE/`, negado `rm -rf *`, `git *` sob aprovação); agentes em `.opencode/agent/` — `teologo.md` (agente primário, papel do 2º teólogo), `bereano.md` (subagente detector de IA, somente leitura) e `escriba.md` (subagente humanizador, grava versões numeradas em `03_revisao/`); comando `/ciclo-humanizacao` em `.opencode/command/` que orquestra Bereano→Escriba até aprovação, move para `04_aprovados/` e registra na memória. Config validada com `opencode debug config` (sem erros). Regras de conteúdo continuam em `AGENTS.md` (carregado automaticamente pelo opencode).
- **Próxima etapa:** produção teológica sob demanda; demais ferramentas (Orca, Claude Code, Antigravity) permanecem válidas.

## 2026-09-18 22:05 — Antigravity — Repositório Git inicializado e publicado no GitHub (joabse/teoftsa)

- **Matéria:** geral (infra/vcs) | **Status:** **PUBLICADO** ✅
- **O que foi feito:** atendendo à solicitação do Joab, o projeto foi inicializado como repositório Git com `.gitignore` configurado (protegendo originais pesados e temporários de OCR). Foi criado o repositório privado no GitHub (`joabse/teoftsa`) e realizado o primeiro commit e push na branch `main`. Diretrizes de documentação (`AGENTS.md`, `GEMINI.md`) atualizadas.
- **Repositório remoto:** `https://github.com/joabse/teoftsa`

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

## 2026-09-13 00:50 — ftsalider — Regra do contexto fresco por arquivo (file2md) [REVISADA]

- **Matéria:** geral (equipe/processo) | **Task:** —
- **Definição do Joab:** cada conversão do file2md é uma **ação independente**. Solução adotada: regra no prompt do file2md + despachos autocontidos (instruções completas reenviadas em cada mensagem).
- **Onde foi registrado:** `ESTRUTURA.md` (regra revisada), `ftsabrain\pipeline.md`, memória AppData (fluxo + roster).

## 2026-09-12 23:40 — ftsalider — Ajuste no fluxo do gbooklm (definido pelo Joab)

- **Matéria:** geral (equipe/processo) | **Task:** —
- **O que foi feito:** Joab definiu nova regra para o **gbooklm (4º teólogo)**: ele **já possui todo o conteúdo** enviado aos demais teólogos — **nunca mais se envia conteúdo/arquivos a ele**. A delegação passa a conter **apenas a pergunta/tarefa + o NOME do notebook do NotebookLM** em que ele deve consultar; esse nome **somente o Joab sabe**, então o líder **sempre pergunta a ele** antes de delegar ao gbooklm (sem indicação = tarefa do gbooklm pausada; demais teólogos seguem).
- **Onde foi registrado:** `ESTRUTURA.md` (regra especial do gbooklm + tabela de papéis), `ftsabrain\pipeline.md` (papéis + regras de ouro), memória AppData (fluxo-trabalho-ftsa.md + equipe-ftsa-roster.md).

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
