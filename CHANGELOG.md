# CHANGELOG

> Banco de dados de alterações estruturais e de arquivos do projeto **teoftsao**.
>
> **Este arquivo NÃO deve ser lido automaticamente por nenhuma LLM** ao iniciar uma
> sessão, nem usado como contexto geral. Ele é só uma fonte de consulta: use-o
> apenas quando precisar reconstruir um histórico específico ou quando o Joab
> pedir algo do histórico do projeto.
>
> **Regra de escrita:** toda LLM/agente que alterar a estrutura ou os arquivos do
> projeto deve adicionar uma entrada aqui **antes de fazer um commit** ou **ao
> finalizar uma tarefa** — o que vier primeiro. Nunca reescreva ou apague entradas
> antigas (apenas o Joab pode pedir isso explicitamente). Ordem cronológica
> decrescente (mais recente no topo).

Formato de cada entrada:

```
## AAAA-MM-DD HH:MM — <agente/LLM> — <resumo curto>
- **Motivo:** por que a alteração foi necessária (pedido do Joab, correção, etc.)
- **O que mudou:** arquivos/estrutura afetados, resumidamente
- **Local:** caminhos relevantes
```

---

## 2026-09-19 13:16 — Claude Code — JOA-15 fechada como Done; Kimi desmembrado para JOA-17

- **Motivo:** o Joab apontou que a JOA-15 não tinha sido marcada como concluída, apesar de mmx e DeepSeek já estarem resolvidos — só o Kimi Code restava pendente, e esse item específico exige login interativo (`kimi login`, device-code no navegador) que só o Joab pode autorizar. Perguntei como proceder; ele escolheu marcar a JOA-15 como concluída mesmo assim.
- **O que mudou:** JOA-15 atualizada (descrição resumindo o que foi resolvido: mmx corrigido, DeepSeek documentado como não instalado) e marcada **Done**. Aberta issue nova **JOA-17** (Backlog, baixa prioridade), só para o item real que restava: confirmar se o Kimi Code lê `AGENTS.md`/`KIMI.md` automaticamente, quando alguém fizer login nele.
- **Lição aplicada:** uma tarefa com partes resolvidas e uma parte pendente que depende de ação exclusiva do usuário deve ser fechada como concluída (com a parte executável já feita) e a parte pendente desmembrada em issue própria — não deixada em "In Progress" indefinidamente à espera de uma ação que não é minha.
- **Local:** Linear (JOA-15 → Done, JOA-17 criada).

## 2026-09-19 12:04 — Claude Code — Execução da JOA-15: investigação real de Kimi/mmx/DeepSeek, correção de suposição

- **Motivo:** issue JOA-15 (aberta por mim na JOA-14) pedia para verificar, quando Kimi/mmx/DeepSeek fossem de fato usados, se realmente leem `AGENTS.md`. O Joab pediu para executar a JOA-15 agora, então investiguei o que estava realmente disponível neste ambiente em vez de esperar.
- **O que foi encontrado:** `kimi` e `mmx` **estão instalados** neste ambiente (`~/.kimi-code/`, `~/AppData/Roaming/npm/mmx`); `deepseek` **não está instalado**. `mmx --help`/`mmx agent setup --help` revelou que **mmx não é um agente de codificação** — é a CLI da MiniMax para configurar *outros* agentes (claude-code, codex, opencode, grok, hermes, pi) a usar modelos MiniMax como provedor; nunca lê arquivos de projeto por conta própria. Minha suposição original (de que mmx lia `AGENTS.md`) estava **errada** e foi corrigida em todos os arquivos. Tentei rodar `kimi -p "..."` para perguntar diretamente o que ele carrega, mas falhou por falta de login/modelo configurado (`No model configured`) — não foi possível confirmar empiricamente. A arquitetura de hooks do Kimi Code (`UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PermissionRequest`, `Stop` — vistos em `~/.kimi-code/config.toml`) é idêntica à do Claude Code, sugerindo forte compatibilidade, mas sem confirmação real.
- **O que mudou:** corrigido `AGENTS.md`, `CLAUDE.md`, `ESTRUTURA.md` (remoção de "mmx" e "DeepSeek" da lista de leitores confirmados de `AGENTS.md`; nota explicando a real natureza do mmx). Criado `KIMI.md` como wrapper **defensivo** (mesmo padrão de `QWEN.md`/`GEMINI.md`), marcado explicitamente como não confirmado. Referências a `KIMI.md` adicionadas em `QWEN.md`, `.clinerules`, `GEMINI.md`. Issue JOA-15 atualizada no Linear com os achados; mantida em aberto (estado "In Progress") só para o item real pendente: confirmar Kimi Code com login real e verificar se DeepSeek chega a ser instalado.
- **Local:** raiz do projeto (`AGENTS.md`, `CLAUDE.md`, `ESTRUTURA.md`, `GEMINI.md`, `QWEN.md`, `.clinerules`, `KIMI.md` novo); Linear (JOA-15).

## 2026-09-19 11:58 — Claude Code — Execução da JOA-14: arquivos wrapper para todas as LLMs + regra de sincronização

- **Motivo:** issue JOA-14 do Joab — "gostaria que as demais LLMs também pudessem entender o projeto... garanta que o líder sempre que mexer na estrutura do projeto atualize ele para as demais LLMs entenderem e sigam as mesmas regras e execuções que o Claude tem." Ferramentas citadas: Antigravity, Codex, opencode, Cline, Kimi, mmx, Qwen Code, DeepSeek.
- **O que mudou:** `AGENTS.md` promovido a arquivo canônico multi-LLM (lido nativamente/por convenção por Codex CLI, opencode, Kimi, mmx e DeepSeek). Criados `QWEN.md` (wrapper para Qwen Code) e `.clinerules` (wrapper para Cline), no mesmo padrão de `CLAUDE.md`/`GEMINI.md`. Adicionada regra permanente de "Sincronização multi-LLM" em `CLAUDE.md` (item 11 + seção 12), `AGENTS.md`, `GEMINI.md`, `QWEN.md`, `.clinerules` e `ESTRUTURA.md`: sempre que uma regra crítica/papel/estrutura mudar em qualquer um dos arquivos-fonte (`CLAUDE.md`, `AGENTS.md`, `ESTRUTURA.md`, `ORCA.md`), a mudança deve ser propagada para todos os wrappers. Diagramas de estrutura de `CLAUDE.md` e `ESTRUTURA.md` atualizados para listar os novos arquivos. Criada issue **JOA-15** (Backlog, baixa prioridade) para verificar, quando essas ferramentas forem de fato usadas, se Kimi/mmx/DeepSeek realmente leem `AGENTS.md` por conta própria ou precisam de wrapper dedicado — essa parte foi assumida por convenção do ecossistema, sem confirmação direta.
- **Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `QWEN.md`, `.clinerules`, `ESTRUTURA.md`); Linear (issue JOA-15).

## 2026-09-19 11:49 — Claude Code — Linear (`teoftsao`) formalizado como banco de tarefas do projeto

- **Motivo:** o Joab apontou o projeto `teoftsao` no Linear (workspace Joabse, time JOA) como o gerenciador de tarefas correspondente ao que o ftsalider precisa executar. Encontrei o projeto vazio (0 issues); criei as 2 primeiras (JOA-12: localizar/reconstituir Q1–Q5 da Bíblia 3; JOA-13: extrair notas de fontes\ da Bíblia 2). O Joab então instruiu: sempre criar tarefas no Linear para soluções/pendências futuras encontradas, não só quando ele pedir.
- **O que mudou:** adicionada regra crítica (item 10) e nova seção 11 em `CLAUDE.md`; seções equivalentes em `AGENTS.md`, `GEMINI.md` e `ESTRUTURA.md`. A regra: toda pendência/decisão/próximo passo identificado por qualquer agente deve virar issue no Linear (`save_issue`, team "Joabse", project "teoftsao") proativamente — memória/changelog/lessons registram o que já aconteceu, o Linear é para o que falta fazer.
- **Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`).

## 2026-09-19 11:38 — Claude Code — Estrutura de 4 terminais nomeados: ftsalider + Teólogo 1/2/3

- **Motivo:** o Joab renomeou os terminais do Orca (`ftsalider`, `Teólogo 1`, `Teólogo 2`, `Teólogo 3`) e explicou que Claude Code atua em dois papéis: ftsalider (este terminal) e Teólogo 1 (outro terminal dedicado). Codex CLI = Teólogo 2, Antigravity = Teólogo 3. Pedido também incluía testar a configuração enviando um "olá" a cada teólogo.
- **O que mudou:** revertida a decisão das 11:27 (que só tinha 2 teólogos, sem papel de teólogo para Claude Code). Atualizados `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`, `ftsabrain/pipeline.md`, `ftsabrain/materias.md` e `materias/README.md` para refletir os 3 teólogos (Teólogo 1 = Claude Code em terminal dedicado, Teólogo 2 = Codex CLI, Teólogo 3 = Antigravity) coordenados pelo ftsalider (Claude Code no terminal principal). Documentado que Claude Code deve inferir seu papel pelo terminal em que está: ftsalider por padrão, Teólogo 1 só quando explicitamente designado. Teste de comunicação via `orca terminal send` confirmou que Codex CLI e Antigravity responderam normalmente; a outra instância de Claude Code (Teólogo 1) recusou corretamente assumir o papel novo até a documentação ser atualizada — ver `LESSONS.md`.
- **Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`); `ftsabrain/pipeline.md`, `ftsabrain/materias.md`, `materias/README.md`.

## 2026-09-19 11:27 — Claude Code — Claude Code passa a ser o ftsalider (líder/orquestrador do projeto)

- **Motivo:** pedido explícito do Joab — "Você sempre será o ftsalider, aqui no Orca. Estruture para isso. O orquestrador de todo o projeto." Decisão confirmada com o Joab: a mudança vale para o projeto todo (não só dentro do Orca) e Claude Code passa a SÓ orquestrar (deixa de produzir rascunhos teológicos diretamente).
- **O que mudou:** `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`, `ftsabrain/pipeline.md`, `ftsabrain/materias.md` e `materias/README.md` atualizados — Claude Code sai da lista de teólogos e assume o papel de ftsalider (líder/orquestrador de Codex CLI e Antigravity, validação de entregas, registro de memória, consolidação de tabelas de múltipla escolha). Teólogos de produção de conteúdo passam a ser SOMENTE Codex CLI (1º) e Antigravity (2º). Regra antiga ("teólogos = Claude Code + Codex CLI + Antigravity") arquivada como histórico em `ESTRUTURA.md`, não apagada.
- **Local:** raiz do projeto (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`, `ORCA.md`); `ftsabrain/pipeline.md`, `ftsabrain/materias.md`, `materias/README.md`.

## 2026-09-19 11:21 — Codex CLI — Correção da documentação operacional e registro de inventário

- **Motivo:** preparar o workspace para novas execuções com papéis, estados e inventários verificáveis.
- **O que mudou:** removidas referências operacionais residuais ao `gbooklm`; MOC atualizado para o estado efetivo das matérias; visão geral da Bíblia 3 passou a registrar a divergência entre seu histórico de 32 entregas e os 27 aprovados atualmente presentes.
- **Local:** `ftsabrain\pipeline.md`, `ftsabrain\materias.md`, `materias\README.md`, `ftsabrain\materias\biblia3\00-visao-geral.md`, `ftsabrain\memoria\00-registro-geral.md`.

## 2026-09-19 11:15 — Claude Code — Criação do CHANGELOG.md e do LESSONS.md

- **Motivo:** pedido explícito do Joab para criar duas funcionalidades que hoje não existiam no projeto: (1) um changelog de alterações estruturais/arquivos que sirva apenas como banco de consulta (não deve ser lido automaticamente pela LLM); (2) um registro de lições aprendidas (erros, acertos, pendências) para orientar outras sessões/LLMs.
- **O que mudou:** criados `CHANGELOG.md` (este arquivo) e `LESSONS.md` na raiz do projeto; `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` e `ESTRUTURA.md` atualizados com as novas regras críticas (obrigatoriedade de registrar antes de commit/finalização de tarefa) e uma seção explicando o formato e o uso dos dois arquivos.
- **Local:** raiz do projeto (`CHANGELOG.md`, `LESSONS.md`); `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`.
