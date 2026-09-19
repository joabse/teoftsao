# LESSONS.md — Lições Aprendidas

> Registro de erros, acertos e pendências não resolvidas durante o trabalho no
> projeto **teoftsao**. Diferente do `CHANGELOG.md`, este arquivo **pode e deve
> ser consultado pela LLM** sempre que for relevante para a tarefa atual — é
> conhecimento operacional para você mesma e para outras sessões/LLMs.
>
> **Regra de escrita:** registre aqui sempre que (1) algo deu errado e precisou
> ser corrigido, (2) uma abordagem não-óbvia funcionou e vale repetir, ou
> (3) um problema não pôde ser resolvido e ficou pendente. Registre **antes de
> um commit** ou **ao finalizar a tarefa**, junto com o `CHANGELOG.md`. Nunca
> apague entradas antigas — se uma lição deixar de valer, marque como
> `~~DESCONTINUADA~~` com a data e o motivo, mas mantenha o registro.

Formato de cada entrada:

```
## AAAA-MM-DD — <agente/LLM> — <resumo curto>
- **O que aconteceu:** contexto e o que foi tentado
- **Erro/acerto:** o que deu errado ou certo, e por quê
- **Correção/solução:** como foi resolvido (ou por que ficou pendente)
- **Lição:** o que a próxima sessão/LLM deve saber para não repetir o erro (ou repetir o acerto)
```

---

## 2026-09-19 — Claude Code — Bash bloqueado por regra `deny` em `.claude/settings.json`

- **O que aconteceu:** ao trocar o remote do git e comitar a renomeação do projeto (`teoftsa` → `teoftsao`), todo comando `git *` no Bash falhava com "Permission... has been denied", inclusive comandos simples como `git status`, mesmo após o usuário aprovar. Comandos não-git (`pwd`, `ls`) funcionavam normalmente.
- **Erro/acerto:** a causa não era permissão de sessão nem falta de aprovação — era uma regra `"deny": ["Bash(git *)"]` em `.claude/settings.json`, reflexo da política antiga do projeto ("sem git") descrita no `CLAUDE.md`. Insistir em repetir o mesmo comando não resolveria.
- **Correção/solução:** perguntei ao Joab como prosseguir (ele já havia pedido explicitamente para usar git); ele autorizou remover a regra de `deny` do `.claude/settings.json`. Após a edição, os comandos git passaram a funcionar normalmente.
- **Lição:** quando um comando Bash é negado repetidamente mesmo após aprovação do usuário, verificar `.claude/settings.json` (e `.claude/settings.local.json`) por regras `deny`/`allow` antes de assumir bloqueio de sessão ou repetir a mesma chamada.

## 2026-09-19 — Claude Code — Remoção de referências ao AionUi incluiu histórico de memória (confirmar antes de apagar)

- **O que aconteceu:** o Joab pediu para remover "tudo relacionado ao AionUi e Maestri". A documentação ativa (`CLAUDE.md`, `AGENTS.md` etc.) era um caso simples de edição, mas `ftsabrain/memoria/00-registro-geral.md` tinha entradas históricas inteiras sobre diagnósticos de infraestrutura do AionUi (aioncore, aionrs, modelo "9aionui", membro "arquivista").
- **Erro/acerto:** o `CLAUDE.md` pede, por padrão, para nunca reescrever histórico de memória (registros passados documentam fatos). Apagar essas entradas sem confirmar seria uma ação arriscada e possivelmente indesejada.
- **Correção/solução:** antes de apagar qualquer coisa, perguntei explicitamente ao Joab se ele queria remover só a documentação ativa ou também o histórico de memória. Ele confirmou que queria tudo, incluindo a memória — só então as entradas foram apagadas.
- **Lição:** pedidos de remoção ampla ("tudo relacionado a X") que tocam registros históricos/memória devem ser confirmados explicitamente antes de apagar histórico, mesmo que a instrução pareça abranger tudo — a regra padrão do projeto é preservar histórico, então a exceção precisa ser explícita.
