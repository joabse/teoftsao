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
