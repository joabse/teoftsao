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

## 2026-09-19 11:15 — Claude Code — Criação do CHANGELOG.md e do LESSONS.md

- **Motivo:** pedido explícito do Joab para criar duas funcionalidades que hoje não existiam no projeto: (1) um changelog de alterações estruturais/arquivos que sirva apenas como banco de consulta (não deve ser lido automaticamente pela LLM); (2) um registro de lições aprendidas (erros, acertos, pendências) para orientar outras sessões/LLMs.
- **O que mudou:** criados `CHANGELOG.md` (este arquivo) e `LESSONS.md` na raiz do projeto; `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` e `ESTRUTURA.md` atualizados com as novas regras críticas (obrigatoriedade de registrar antes de commit/finalização de tarefa) e uma seção explicando o formato e o uso dos dois arquivos.
- **Local:** raiz do projeto (`CHANGELOG.md`, `LESSONS.md`); `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `ESTRUTURA.md`.
