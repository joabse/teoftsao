# Pipeline FTSA — Resumo

> Base de conhecimento da equipe. Versão detalhada em `..\ESTRUTURA.md`; regras das matérias em `..\materias\README.md`.

## Fluxo em uma frase

Originais → Markdown → Rascunhos → **Ciclo de Humanização (Bereano ⇄ Escriba)** → Aprovados → Usuário.

## Etapas

1. **Entrada** — usuário envia arquivos da matéria para `materias\<nome>\00_originais\` (imutáveis).
2. **Conversão** — **file2md** converte tudo para Markdown em `01_markdown\`.
3. **Produção** — teólogos (**Teólogo 1, Teólogo 2, Teólogo 3** — terminais nomeados no Orca; ocupantes atuais: Claude Code, Codex CLI, Antigravity, respectivamente) analisam os materiais e escrevem textos em `02_rascunhos\`.
4. **Ciclo de humanização** (em `03_revisao\`, versões numeradas v1, v2, v3…):
   - **Bereano** avalia se o texto parece gerado por IA.
   - **Aprovado** → vai para `04_aprovados\`.
   - **Reprovado** → **Escriba** humaniza → nova versão → volta ao Bereano → repete até aprovar.
5. **Entrega** — texto de `04_aprovados\` é entregue ao usuário por quem estiver no terminal **ftsalider** (hoje Claude Code).
6. **REGISTRO** — após cada etapa concluída, o **ftsalider** registra a entrada na memória (`ftsabrain\memoria\...`) correspondente: etapa geral → [[memoria/00-registro-geral|Registro Geral]]; etapa de matéria → `ftsabrain\memoria\materias\<nome>\registro.md`.

## Papéis (rápido)

- **ftsalider (terminal "ftsalider" — hoje Claude Code, mas o papel pertence ao terminal, não à LLM)** — orquestra toda a equipe: coordena os 3 teólogos e o comitador, distribui tarefas e valida entregas com o usuário. Não produz rascunhos teológicos diretamente (Joab, 2026-09-19; revisado 13:16).
- **Teólogo 1 / Teólogo 2 / Teólogo 3** — os 3 teólogos, um por terminal nomeado no Orca (papel fixo por terminal; ocupantes hoje: Claude Code, Codex CLI, Antigravity, respectivamente — mas podem mudar). Produzem textos. Anteriormente existia o gbooklm (4º teólogo NotebookLM), **removido pelo Joab** em 2026-09-13 — por isso essa função está descontinuada.
- **comitador (terminal dedicado, hoje Cline)** — faz commits git a pedido do ftsalider, com a descrição detalhada que ele fornecer. Nunca decide sozinho o que comitar (Joab, 2026-09-19, JOA-20).
  - 🌐 **Regra de pesquisa na Bíblia (Joab, 2026-09-13):** se precisarem consultar a Bíblia (texto, comentários, léxicos, contexto histórico), os teólogos estão **livres para buscar na internet** com os MCPs de busca do projeto ou pelo browser integrado do Orca (`orca tab`) — **sem necessidade de pedir autorização** ao líder. Devem **sempre indicar a fonte** (URL, obra, autor) na resposta. As notas em `fontes\` continuam sendo a base primária; a busca externa é complementar.
- **file2md** — converte arquivos para Markdown.
- **Bereano** — detector de IA (aprova/reprova).
- **Escriba** — humaniza textos reprovados.
- **tecfix** — manutenção técnica do projeto e ambiente Orca (estrutura, config, diagnóstico).

## Regras de ouro

- Originais nunca se alteram.
- Nenhum texto vai para o usuário sem aprovação do Bereano.
- ~~**gbooklm nunca recebe conteúdo — só pergunta + nome do notebook indicado pelo Joab.**~~ DESCONTINUADA (gbooklm removido em 2026-09-13).
- **PRIORIDADE ABSOLUTA: material enviado** — respostas baseadas nas notas de `fontes\`; internet/MCPs de busca apenas complementares para confirmar. Em conflito, prevalece o material. (Joab, 2026-09-13)
- **Teólogos podem buscar na internet com MCPs de busca** para consultar a Bíblia (texto/comentários/léxicos); citar sempre a fonte. Notas de `fontes\` são a base primária.
- **Múltipla escolha: sempre fechar com tabela-resumo** — nº da questão · resposta de cada teólogo · **sugestão do líder** (letra correta + justificativa 1 linha). Divergências destacadas e explicadas antes da sugestão. (Joab, 2026-09-13)
- **Teólogos = Teólogo 1 + Teólogo 2 + Teólogo 3**, um por terminal nomeado no Orca. O papel pertence ao terminal, não à LLM — ocupantes hoje são Claude Code, Codex CLI e Antigravity, mas o Joab pode trocar qualquer um deles, inclusive o `ftsalider`. (Joab, 2026-09-19, revisado 13:16)
- Manter histórico de versões em `03_revisao\`.
- **file2md: contexto isolado por arquivo** — regra no prompt do agente ("processe APENAS o arquivo atual; ignore anteriores") + o líder sempre reenvia instruções completas em cada despacho. Cada conversão é tratada como independente. (tecfix, 2026-09-13)
- Toda etapa concluída é registrada na memória do vault (`ftsabrain\memoria\`), por matéria ou no registro geral.
- Toda nova matéria copia `materias\_TEMPLATE\` e é registrada em `materias.md`.
- Conteúdo e documentação sempre em português brasileiro.
