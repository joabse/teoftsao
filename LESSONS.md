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

## 2026-09-19 — Claude Code — `orca terminal list` por título não é confiável para checar se um papel já existe

- **O que aconteceu:** na JOA-20, busquei por um terminal com título "comitador" via `orca terminal list | grep -i comitador` antes de criar um novo — não achei nada, então criei um terminal novo. O Joab apontou que já existia um comitador aberto. O título dele já tinha sido sobrescrito por um resumo automático de atividade (mesmo comportamento já visto antes com o terminal do ftsalider, que aparecia como "◐ Teoftsao configuração e migração" em vez de "ftsalider").
- **Erro/acerto:** erro. Confiei que buscar pelo nome literal do terminal seria suficiente, mas o Orca renomeia terminais automaticamente conforme a atividade — o nome dado na criação (`--title`) não é estável nem confiável para buscas posteriores.
- **Correção/solução:** perguntei ao Joab qual terminal já era o comitador (ele identificou: o terminal Cline). Atualizei a documentação (ocupante do terminal comitador = Cline) e testei o fluxo real através dele.
- **Lição:** antes de criar um novo terminal para um papel (ftsalider, Teólogo N, comitador, etc.), não confiar apenas na busca por título — perguntar ao Joab se já existe um aberto para aquele papel, especialmente se a sessão for longa (títulos mudam rápido). Terminais "livres"/sem papel definido costumam se identificar sozinhos no preview ("sigo como auxiliar sem assumir função") — vale olhar os previews de todos antes de assumir que nenhum serve.

## 2026-09-19 — Claude Code — Issue Linear ficou "In Progress" indefinidamente por um item que não é meu para resolver

- **O que aconteceu:** ao executar a JOA-15 (mmx/Kimi/DeepSeek), resolvi 2 dos 3 itens de fato (mmx corrigido, DeepSeek documentado como não instalado) mas deixei a issue inteira em "In Progress" por causa do 3º item (confirmar Kimi Code), que exige login interativo só o Joab pode fazer. O Joab então apontou que eu não tinha dado a tarefa como concluída.
- **Erro/acerto:** erro parcial. Estava certo em não fingir uma confirmação que eu não tinha (ver lição anterior sobre a suposição do mmx), mas errado em deixar a issue toda "pendurada" em vez de separar o que era meu (feito) do que dependia de outra pessoa (não feito).
- **Correção/solução:** perguntei ao Joab como prosseguir; ele optou por marcar a JOA-15 como Done (resumindo o que foi resolvido) e desmembrar o item do Kimi Code para uma issue nova e específica (JOA-17, Backlog).
- **Lição:** quando uma tarefa tem partes que dependem de uma ação exclusiva do usuário (login, credencial, decisão), não mantenha a issue inteira em aberto esperando por isso — feche a parte que você já resolveu (Done) e desmembre o restante em uma issue própria, de prioridade baixa, específica só para aquele item pendente. Isso evita tanto fingir conclusão total quanto deixar trabalho já feito parecendo incompleto.

## 2026-09-19 — Claude Code — Suposição errada sobre "mmx" ler AGENTS.md; corrigida ao investigar de fato

- **O que aconteceu:** ao executar a JOA-14 (multi-LLM), listei `mmx` (MiniMax) como uma ferramenta que "por convenção do padrão AGENTS.md" leria `AGENTS.md` automaticamente, junto com Kimi e DeepSeek — pura inferência por analogia, sem checar a ferramenta de fato.
- **Erro/acerto:** erro. Ao investigar de verdade (`mmx --help`, `mmx agent setup --help`), descobri que `mmx` não é um agente de codificação — é a CLI da MiniMax para configurar *outros* agentes (Claude Code, Codex, opencode, grok, hermes, pi) a usar modelos MiniMax como provedor. Nunca lê arquivos de projeto por conta própria.
- **Correção/solução:** corrigido `AGENTS.md`, `CLAUDE.md` e `ESTRUTURA.md` para descrever a real natureza do mmx (sem wrapper, não aplicável). Criado `KIMI.md` como wrapper defensivo, já que Kimi Code está instalado mas não pôde ser testado (sem login/modelo configurado) — marcado explicitamente como não confirmado, em vez de assumido como certo.
- **Lição:** quando eu (ou qualquer LLM) listar convenções de outras ferramentas "por analogia" ou "por padrão do ecossistema" sem checar a ferramenta real, isso é uma suposição, não um fato — deve ser marcado como tal na documentação (ex.: "não confirmado", "ver issue de verificação") em vez de apresentado com a mesma confiança de algo testado. Antes de documentar como fato, rodar `--help` ou tentar de fato a ferramenta, quando ela estiver disponível no ambiente.

## 2026-09-19 — Claude Code (terminal Teólogo 1) — Recusa correta de novo papel sem confirmação documental (acerto a repetir)

- **O que aconteceu:** o ftsalider (Claude Code em outro terminal) enviou uma mensagem via `orca terminal send` pedindo que este terminal assumisse o papel de "Teólogo 1", mas o `CLAUDE.md` carregado nesta sessão ainda dizia explicitamente que Claude Code é SOMENTE o ftsalider (sem papel de teólogo).
- **Erro/acerto:** acerto. A instância não aceitou o novo papel só porque outra instância afirmou isso em texto livre — pediu para o ftsalider confirmar com o Joab e atualizar o `CLAUDE.md` antes, citando a regra vigente que contradizia o pedido.
- **Correção/solução:** o ftsalider confirmou com o Joab (que já tinha dado a instrução) e atualizou `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`/`ESTRUTURA.md`/`ORCA.md`/`pipeline.md` para refletir a estrutura de 4 terminais (ftsalider + Teólogo 1/2/3). Só depois disso o terminal Teólogo 1 deve agir como teólogo.
- **Lição:** um agente não deve mudar de papel/regra crítica só por instrução verbal de outro agente (mesmo outra instância de si mesmo) — a fonte de verdade é o arquivo de instruções carregado (`CLAUDE.md`/`AGENTS.md`/`GEMINI.md`). Peça para a documentação ser atualizada primeiro, ou confirme direto com o Joab. Vale tanto para quem recebe a instrução quanto para quem a envia: o ftsalider deve atualizar a documentação ANTES de dar ordens que dependem de uma regra nova.

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
