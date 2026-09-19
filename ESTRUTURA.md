# ESTRUTURA.md — Projeto FTSA

> FTSA — Fluxo de Trabalho de Textos com Agentes (equipe de agentes coordenada no Orca).

## 1. Visão geral

Este diretório é o workspace oficial da equipe FTSA. A equipe produz **textos teológicos de qualidade humana** a partir de materiais de estudo enviados pelo usuário (Joab), usando um pipeline de agentes com etapa de detecção e humanização de texto gerado por IA.

```
E:\00_ATUAL\04_PROJETO\teoftsao\
├── ESTRUTURA.md          ← este arquivo (organização geral, papéis e pipeline)
├── ORCA.md               ← guia de operação da equipe e comandos no Orca
├── CLAUDE.md             ← wrapper de instruções para o Claude Code
├── AGENTS.md             ← wrapper canônico (Codex CLI, opencode)
├── GEMINI.md             ← wrapper de instruções para o Antigravity
├── QWEN.md               ← wrapper de instruções para o Qwen Code
├── .clinerules            ← wrapper de instruções para o Cline
├── CHANGELOG.md          ← banco de alterações estruturais (não ler automaticamente)
├── LESSONS.md            ← lições aprendidas (consultar quando relevante)
├── materias\             ← uma pasta por matéria (disciplina), com fluxo padronizado
│   ├── README.md         ← documentação do fluxo de matérias
│   ├── _TEMPLATE\        ← modelo de pastas para criar novas matérias
│   ├── biblia2\          ← matéria "Bíblia 2"
│   └── biblia3\          ← matéria "Bíblia 3"
└── ftsabrain\            ← cérebro do projeto (vault Obsidian, organizado por matéria)
    ├── pipeline.md       ← resumo do pipeline de produção
    ├── materias.md       ← MOC/índice geral das matérias (links para cada matéria)
    ├── materias\         ← notas de conhecimento por matéria
    │   ├── biblia2\      ← 00-visao-geral.md + fontes\ (conhecimento extraído dos materiais)
    │   ├── biblia3\      ← idem — matéria "Bíblia 3"
    │   └── _TEMPLATE\    ← modelo para novas matérias
    └── memoria\          ← memória de trabalho do projeto (log por etapa)
        ├── 00-registro-geral.md  ← log de atividades gerais (montagem, manutenção, estrutura)
        └── materias\             ← log por matéria (<nome>\registro.md; _TEMPLATE\ = modelo)
```

## 2. Papéis da equipe

O Orca roda o projeto em **5 terminais nomeados** (Joab, 2026-09-19): **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3** e **comitador**. **O papel pertence ao terminal, não à LLM que o ocupa** (Joab, 2026-09-19, revisão 13:16): o líder é sempre quem estiver no terminal `ftsalider` — hoje Claude Code, mas o Joab pode trocar para Codex, Antigravity ou qualquer outra LLM a qualquer momento. O mesmo vale para os 3 terminais de Teólogo e para o comitador. A tabela abaixo mostra o papel fixo de cada terminal e o ocupante **atual** (um estado, não uma regra).

| Terminal (papel) | Responsabilidade no pipeline | Ocupante atual (2026-09-19) |
|---|---|---|
| **ftsalider** — Líder/Orquestrador | Orquestra toda a equipe: coordena os 3 teólogos e o comitador, distribui tarefas, valida entregas com o usuário, registra a memória. **Não produz rascunhos teológicos diretamente.** | Claude Code |
| **Teólogo 1** | Analisa os arquivos da matéria e **produz textos** (rascunhos em `02_rascunhos\`). | Claude Code (terminal dedicado, separado do ftsalider) |
| **Teólogo 2** | Íd. — análise de materiais e produção de textos. | Codex CLI |
| **Teólogo 3** | Íd. — análise de materiais e produção de textos. | Antigravity |
| **comitador** | Faz commits git a pedido do ftsalider, com a descrição detalhada que ele fornecer. **Nunca decide sozinho** o que comitar ou a mensagem. | Cline (terminal dedicado, já aberto pelo Joab) |
| ~~**gbooklm**~~ | ~~Teólogo~~ | **REMOVIDO pelo Joab em 2026-09-13.** Era o especialista NotebookLM (4º teólogo). Assistente permanece no catálogo (`custom-1789227611495-859d`); se re-adicionado, restaurar a regra própria. |
| **file2md** | Conversor | **Converte qualquer arquivo para Markdown** (PDF, DOCX, PPTX etc.) e salva em `01_markdown\`. |
| **Bereano** | Detector de IA | **Detecta se o texto foi gerado por IA**; aprova ou reprova textos no ciclo de revisão. |
| **Escriba** | Humanizador | **Humaniza textos reprovados** pelo Bereano (reescreve para soar humano). |
| **tecfix** | Manutenção técnica | **Manutenção do projeto e do Orca**: estrutura de pastas, configuração, diagnósticos e infraestrutura. Não produz conteúdo teológico. |

## 3. Pipeline de produção

```
Usuário envia materiais da matéria
        │
        ▼
materias\<nome>\00_originais\        (originais imutáveis)
        │  file2md converte
        ▼
materias\<nome>\01_markdown\         (Markdown pronto para análise)
        │  teólogos analisam e escrevem
        ▼
materias\<nome>\02_rascunhos\        (textos produzidos pelos teólogos)
        │
        ▼
╔═════════════ CICLO DE HUMANIZAÇÃO ═════════════╗
║                                                ║
║   texto ──► Bereano (detector de IA)           ║
║                │                               ║
║        aprovado? ── SIM ──► 04_aprovados\      ║
║                │ NÃO                           ║
║                ▼                               ║
║        Escriba humaniza o texto                ║
║                │                               ║
║        nova versão (v1, v2, v3… em 03_revisao\)║
║                │                               ║
║        └──► volta ao Bereano ──┐               ║
║              (repete até aprovação)            ║
╚════════════════════════════════════════════════╝
        │
        ▼
materias\<nome>\04_aprovados\        (texto final validado como humano)
        │
        ▼
Entrega ao usuário (via ftsalider)
```

### Regras do ciclo de humanização

1. Todo texto produzido pelos teólogos **obrigatoriamente** passa pelo Bereano.
2. Reprovado → Escriba humaniza → nova versão numerada em `03_revisao\` → Bereano avalia de novo.
3. O loop repete **até aprovação**; só então o texto vai para `04_aprovados\`.
4. Manter sempre o histórico de versões em `03_revisao\` (nunca sobrescrever versão anterior).

### Regra do contexto fresco por arquivo (file2md) — **REVISADA (tecfix, 2026-09-13)**

1. Cada nova conversão é uma **ação independente** — um arquivo convertido não tem relação com o anterior.
2. **Solução adotada (opção A, aprovada pelo Joab):** regra no system prompt do file2md — "processe APENAS o arquivo da mensagem atual; ignore conversões anteriores nesta conversa". O contexto LLM acumula tokens, mas o agente trata cada arquivo isoladamente.
3. O lead **sempre reenvia as instruções completas** (origem, destino, escopo, formato do report) em cada despacho — o agente processa cada arquivo como se fosse o primeiro.
4. Isso **isola as conversões** e impede que artefatos/OCR residual de uma conversão se infiltrem na seguinte.
5. Aplica-se a **todos os lotes** (PDFs, transcrições, futuros arquivos), sem exceção.

### ~~Regra especial do gbooklm (4º teólogo)~~ — DESCONTINUADA (Joab, 2026-09-13)

> **Status:** gbooklm foi **removido da equipe pelo Joab**. Os teólogos são agora SOMENTE Claude Code, Codex CLI e Antigravity. Esta regra fica arquivada aqui apenas como histórico; **não está mais em vigor**. Se o Joab re-adicionar o gbooklm, restaurar os 4 pontos abaixo.
>
> 1. O gbooklm **já possui todo o conteúdo** enviado aos demais teólogos (em seus notebooks do NotebookLM) — portanto **NUNCA se envia conteúdo/arquivos a ele**.
> 2. O que o líder envia ao gbooklm: **apenas a pergunta/tarefa + o NOME do notebook do NotebookLM** no qual ele deve consultar.
> 3. O nome do notebook **somente o usuário (Joab) sabe** — antes de qualquer delegação ao gbooklm, o líder **sempre pergunta ao Joab qual notebook usar**.
> 4. Se o Joab não indicar notebook, a tarefa do gbooklm fica **pausada** até a indicação (os demais teólogos seguem normalmente).

### Regra de pesquisa na Bíblia (teólogos com MCPs de busca)

1. **PRIORIDADE ABSOLUTA — MATERIAL ENVIADO (Joab, 2026-09-13):** todas as respostas dos teólogos devem ser **baseadas nas notas de estudo em `fontes\`** (as 27 notas de biblia3, e equivalentes para outras matérias). O material do curso é a **fonte primária e obrigatória**; a busca externa é apenas **complementar** para confirmar/verificar.
2. Caso precisem consultar a Bíblia (texto bíblico, comentários, lexicos, dicionários, contexto histórico) para fundamentar uma resposta, os teólogos (terminais Teólogo 1, 2 e 3 — ver ocupantes atuais na seção 2) estão **livres para buscar na internet** usando os MCPs de busca ou o browser integrado do Orca (`orca tab`).
3. **Não é necessário pedir autorização** ao líder a cada busca — o uso é parte do trabalho normal de pesquisa teológica.
4. Os teólogos devem **sempre indicar a fonte** da consulta externa (URL, obra, autor) na resposta ao usuário, para que o líder possa validar e citar.
5. Em caso de **conflito** entre o material enviado e uma fonte externa, **prevalece o material enviado** (a menos que o Joab decida o contrário).
6. Decisão registrada pelo usuário em 2026-09-13.

### Regra — Papéis pertencem ao terminal, não à LLM (Joab, 2026-09-19, 13:16)

1. **O Orca roda o projeto em 4 terminais nomeados:** `ftsalider`, `Teólogo 1`, `Teólogo 2`, `Teólogo 3`. O **papel** de cada terminal é fixo; a **LLM que o ocupa é um estado, não uma regra**, e pode ser trocada pelo Joab a qualquer momento (ex.: colocar Codex no terminal `ftsalider`, ou Claude Code num terminal de Teólogo).
2. **Terminal `ftsalider`** — quem estiver nele lidera a equipe: distribui tarefas aos 3 teólogos, valida entregas com o Joab, consolida tabelas de múltipla escolha, registra a memória. **Não produz rascunhos teológicos diretamente.** Ocupante atual: Claude Code.
3. **Terminais `Teólogo 1`, `Teólogo 2`, `Teólogo 3`** — quem estiver neles analisa materiais em `fontes\` e produz rascunhos em `02_rascunhos\`. Ocupantes atuais: Claude Code (Teólogo 1, terminal dedicado), Codex CLI (Teólogo 2), Antigravity (Teólogo 3).
4. **Nenhuma LLM deve assumir seu papel só pela própria identidade** — antes de agir, confirme o nome do terminal em que está (no Orca) ou pergunte ao Joab/ftsalider. A mesma LLM pode ocupar papéis diferentes em terminais diferentes (caso do Claude Code hoje: ftsalider num terminal, Teólogo 1 em outro).
5. file2md, Bereano, Escriba e tecfix continuam com papéis próprios (conversão, detecção, humanização, técnica) — **não são teólogos**, não ocupam um dos 4 terminais nomeados, e não recebem questões. (gbooklm foi removido da equipe em 2026-09-13.)

### Regra — Terminal comitador (Joab, 2026-09-19, 13:35, issue JOA-20)

1. **Terminal `comitador`** — 5º terminal nomeado no Orca. Faz commits git a pedido do ftsalider.
2. **O ftsalider é responsável por redigir uma descrição detalhada** do commit (o que mudou, por quê) antes de pedir ao comitador. O comitador nunca decide sozinho o que comitar ou como descrever.
3. O comitador executa exatamente com a descrição recebida — não resume, não reinterpreta.
4. Antes de instruir o comitador, **verificar qual LLM/CLI ocupa aquele terminal** para adaptar a sintaxe do comando e obter a melhor performance.
5. Commits deixam de ser feitos diretamente pelo ftsalider ou pelos teólogos — passam sempre pelo comitador.

### ~~Regra anterior — Estrutura de 4 terminais nomeados no Orca (Joab, 2026-09-19, 11:40)~~ — SUPERSEDIDA

> Arquivada como histórico: definia a estrutura de 4 terminais, mas ainda amarrava cada papel à LLM específica ("ftsalider = Claude Code", "Teólogo 2 = Codex CLI") como se fosse regra fixa, não estado. Corrigida ~1h35min depois: o Joab esclareceu que o papel pertence ao terminal, e a LLM ocupante pode variar (ex.: trocar para Codex ou Antigravity no terminal ftsalider).

### ~~Regra anterior — Claude Code é o ftsalider, só 2 teólogos (Joab, 2026-09-19, 11:27)~~ — SUPERSEDIDA

> Arquivada como histórico: dizia que os teólogos de produção eram SOMENTE 2 (Codex CLI e Antigravity), sem papel de teólogo para Claude Code. Substituída ~13 minutos depois pela estrutura de 4 terminais acima, quando o Joab renomeou os terminais do Orca e explicou que Claude Code também atuaria como Teólogo 1 em terminal separado.

### ~~Regra anterior — quem são os teólogos (Joab, 2026-09-13)~~ — SUPERSEDIDA em 2026-09-19

> Arquivada como histórico: "Os teólogos são SOMENTE 3: Claude Code (1º), Codex CLI (2º), Antigravity (3º)." (a estrutura atual chegou de volta a esse número, mas agora com terminais nomeados e o papel de ftsalider formalizado.)

### Regra de consolidação de questões de múltipla escolha

1. Quando o Joab enviar **questões de múltipla escolha**, os teólogos respondem individualmente e o líder **consolida no final uma tabela-resumo** com:
   - **Nº da questão** e enunciado (resumido)
   - **Resposta de cada teólogo** (A/B/C/D/E)
   - **Sugestão do líder** (letra marcada como correta + justificativa em 1 linha, com base nas notas de `fontes\` e/ou fonte externa citada)
2. A tabela vem **depois de todas as questões respondidas** (nunca intercalada).
3. Se houver divergência entre teólogos, o líder destaca a questão e explica os argumentos antes de sugerir a resposta.
4. Decisão registrada pelo usuário em 2026-09-13.

### Memória de trabalho (`ftsabrain\memoria\`)

Toda etapa concluída por qualquer assistente é registrada na memória do projeto (dentro do vault ftsabrain), para consulta futura por assistentes e pelo usuário:

- Atividades **gerais** (montagem, manutenção, mudanças estruturais) → `ftsabrain\memoria\00-registro-geral.md`.
- Atividades de uma **matéria** → `ftsabrain\memoria\materias\<nome>\registro.md`.
- Quem registra: o **ftsalider**, após validar a conclusão da etapa.
- Formato: frontmatter `tipo: registro` + entradas cronológicas (mais recente no topo) com agente, tarefa, o que foi feito e local do produto gerado.

### `CHANGELOG.md` e `LESSONS.md` (raiz do projeto)

Duas ferramentas de rastreio complementares à memória do `ftsabrain\` (que é sobre **conteúdo teológico**; estas duas são sobre **o projeto em si** — estrutura, arquivos, processo).

- **`CHANGELOG.md`** — banco de dados de alterações estruturais/arquivos: data/hora, agente e motivo. **Nunca lido automaticamente** por nenhuma LLM ao iniciar sessão; é consultado só quando alguém precisa reconstruir um histórico específico ou o Joab pede. Toda LLM/agente que alterar estrutura ou arquivos do projeto adiciona uma entrada **antes do commit** ou **ao finalizar a tarefa**. Nunca apagar/reescrever entradas antigas sem autorização explícita do Joab.
- **`LESSONS.md`** — erros, acertos e pendências não resolvidas durante o trabalho, para orientar a própria LLM ou outra sessão/LLM no futuro. Ao contrário do changelog, **pode e deve ser consultado** quando for relevante para a tarefa atual. Mesmo ritmo de registro (antes do commit ou ao finalizar a tarefa); entradas obsoletas se marcam `~~DESCONTINUADA~~`, nunca se apagam.

### Linear — banco de tarefas do projeto (Joab, 2026-09-19)

- **Projeto `teoftsao`** no Linear (workspace Joabse, time JOA), acessado via ferramentas `mcp__claude_ai_Linear__*`. Diferente da memória e do changelog/lessons (que registram o que **já aconteceu**), o Linear é para **trabalho futuro/pendente**.
- **Regra-chave:** sempre que qualquer agente (ftsalider ou teólogo) identificar algo para resolver ou executar depois — pendência, divergência de auditoria, decisão a tomar, próximo passo — deve criar uma issue no Linear (`save_issue`, `team: "Joabse"`, `project: "teoftsao"`), proativamente, sem esperar o Joab pedir.
- Título com prefixo da matéria/área entre colchetes; descrição com contexto e passos; prioridade e estado (`Todo` se executável já, `Backlog` se depende de algo antes). Ao concluir, atualizar o `state` para `Done`/`Canceled`.
- Quem não tiver acesso direto à ferramenta do Linear (ex.: Antigravity, dependendo da configuração) pede ao ftsalider para criar a issue.

### Sincronização multi-LLM (Joab, 2026-09-19)

O projeto precisa ser entendido por **qualquer LLM** que trabalhe nele, não só o Claude Code. Arquivos de instrução por ferramenta: `CLAUDE.md` (Claude Code), `AGENTS.md` (canônico — Codex CLI, opencode), `GEMINI.md` (Antigravity), `QWEN.md` (Qwen Code), `.clinerules` (Cline). `mmx` **não** é um agente que leia arquivos de projeto — é a CLI da MiniMax para configurar outros agentes (Claude Code, Codex, opencode, grok, hermes, pi) a usar modelos MiniMax; não precisa de wrapper. **Kimi Code e DeepSeek foram removidos/não são usados no projeto** (Joab, 2026-09-19, issue **JOA-19** no Linear) — se isso mudar no futuro, criar o wrapper correspondente.

**Regra:** sempre que o ftsalider (ou qualquer agente) alterar `CLAUDE.md`, `AGENTS.md`, `ESTRUTURA.md` ou `ORCA.md` — regras, papéis, estrutura de pastas, pipeline — deve propagar a mesma mudança para **todos** os arquivos acima, para que todas as LLMs sigam as mesmas regras e a mesma execução que o Claude tem. Uma ferramenta sem convenção de arquivo própria e conhecida deve encontrar orientação em `AGENTS.md` (padrão de fato do ecossistema); se depois se descobrir que ela tem convenção própria, criar o wrapper correspondente e registrar no `CHANGELOG.md`.

## 4. Convenções

- **Idioma:** todo conteúdo e documentação em português brasileiro.
- **Nomes de matéria:** minúsculas, sem espaços, hífens para separar palavras (ex.: `teologia-sistematica1`).
- **Originais:** arquivos em `00_originais\` nunca são alterados.
- **Nova matéria:** copiar `materias\_TEMPLATE\` e registrar em `ftsabrain\materias.md` (detalhes em `materias\README.md`).
- **ftsabrain:** cérebro do projeto (vault Obsidian) — repositório central de conhecimento, organizado por matéria (`materias\<nome>\00-visao-geral.md` + `fontes\`), consultado pelos teólogos. Manter o MOC `materias.md` e `pipeline.md` sempre atualizados.

## 5. Manutenção

Alterações estruturais (novas pastas globais, mudança de pipeline) são responsabilidade do **tecfix**, acionado pelo líder. Dúvidas sobre onde salvar um arquivo? Consultar `materias\README.md` ou perguntar ao líder.
