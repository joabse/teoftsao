# Repository Guidelines

> Repositório Git privado (`joabse/teoftsao`) gerenciado no Orca — workspace de uma equipe de agentes de IA (FTSA) que produz textos teológicos a partir de materiais de estudo. Ver `ESTRUTURA.md` para o detalhamento completo de papéis e regras, e `ORCA.md` para instruções de operação no Orca.
>
> **Este é o arquivo canônico multi-LLM do projeto.** `AGENTS.md` é o padrão aberto que a maioria dos CLIs de agente lê automaticamente na raiz do repositório — além do Codex CLI, é reconhecido por **opencode**. Ferramentas com convenção de arquivo própria têm um wrapper fino que remete para este arquivo + `ESTRUTURA.md`/`ORCA.md`: **`CLAUDE.md`** (Claude Code), **`GEMINI.md`** (Antigravity), **`QWEN.md`** (Qwen Code), **`.clinerules`** (Cline). Todos descrevem as mesmas regras e a mesma execução — ver seção "Sincronização multi-LLM" abaixo. **`mmx` não é um agente que leia arquivos de projeto** — é a CLI da MiniMax para configurar *outros* agentes (Claude Code, Codex, opencode, grok, hermes, pi) a usar modelos MiniMax como provedor; não precisa de wrapper. **Kimi Code e DeepSeek**: removidos do projeto a pedido do Joab (2026-09-19) — ainda não serão usados; se isso mudar, criar wrapper de novo.

## Execução pelo Codex

- Este arquivo é a configuração de projeto reconhecida pelo Codex CLI. Execute o Codex a partir da raiz `E:\00_ATUAL\04_PROJETO\teoftsao`; não crie nem exija um repositório Git para trabalhar aqui.
- **Seu papel depende do terminal em que você está, não do fato de ser Codex (Joab, 2026-09-19).** O projeto tem 5 terminais nomeados no Orca — `ftsalider`, `Teólogo 1`, `Teólogo 2`, `Teólogo 3`, `comitador` — com papel fixo por terminal, mas ocupante variável. Hoje (2026-09-19) você (Codex) está no terminal **Teólogo 2**; não assuma isso permanentemente — confirme o nome do seu terminal ou pergunte ao Joab/ftsalider. Como Teólogo, não assume as funções de `file2md`, Bereano, Escriba, `tecfix` ou `comitador`, salvo pedido explícito.
- **Commits passam pelo comitador**, não pelo ftsalider nem pelos teólogos: nunca rode `git commit` você mesmo — se algo precisar ser comitado, avise o ftsalider.
- **O terminal `ftsalider`** — hoje ocupado por Claude Code — orquestra o trabalho entre os 3 terminais de Teólogo e os demais agentes; distribui tarefas, valida entregas com o Joab e registra a memória. Quem estiver no `ftsalider` não produz rascunhos teológicos diretamente.
- Antes de produzir conteúdo para uma matéria, leia `ftsabrain/materias/<nome>/00-visao-geral.md`, as notas pertinentes em `ftsabrain/materias/<nome>/fontes/` e o registro de memória da matéria. Para entender o estado global, consulte `ftsabrain/memoria/00-registro-geral.md`.
- Para tarefas de conteúdo, salve primeiro o resultado em `materias/<nome>/02_rascunhos/`. Não coloque texto teológico diretamente em `04_aprovados/`: a aprovação cabe ao Bereano, e eventuais versões humanizadas pertencem a `03_revisao/`.
- Ao concluir uma etapa material, atualize o registro de memória pertinente, com data, papel/agente, escopo, resultado e caminho do arquivo. Não registre apenas consultas ou diagnósticos sem mudança.

## Project Structure & Module Organization

- `materias/<nome>/` — uma pasta por disciplina, sempre com o mesmo pipeline de 5 etapas: `00_originais/` (arquivos enviados, imutáveis) → `01_markdown/` (convertidos pelo agente file2md) → `02_rascunhos/` (textos dos teólogos) → `03_revisao/` (ciclo de humanização, versionado `v1.md`, `v2.md`…) → `04_aprovados/` (entrega final). Copie `materias/_TEMPLATE/` para criar uma nova disciplina.
- `ftsabrain/` — vault Obsidian (o "cérebro" do projeto): `materias/<nome>/` guarda notas de conhecimento extraídas (`fontes/`); `memoria/` é o log de atividades (`00-registro-geral.md` para eventos gerais, `memoria/materias/<nome>/registro.md` por disciplina).
- `materias/biblia3/*.py` — scripts avulsos de limpeza/consolidação de OCR (ver seção abaixo).

## Pipeline de Conteúdo

- `00_originais/` nunca é alterado; qualquer transformação gera arquivo em outra pasta.
- Todo rascunho produzido por um teólogo passa obrigatoriamente pelo ciclo de humanização antes de `04_aprovados/`: **Bereano** (detector de IA) aprova ou reprova; se reprovado, **Escriba** humaniza e salva nova versão numerada em `03_revisao/` (nunca sobrescrever versão anterior); repete até aprovação.
- Toda a documentação e todo o conteúdo produzido é em português brasileiro.
- Ao concluir uma etapa, registre a entrada em `ftsabrain/memoria/` (geral ou por matéria) — é a única forma de rastrear progresso, já que não há git.

## Changelog e Lições Aprendidas (raiz do projeto)

- **`CHANGELOG.md`** — registre toda alteração de estrutura/arquivos do projeto (data/hora, motivo) **antes de um commit** ou **ao finalizar a tarefa**. É banco de consulta: **não leia automaticamente** ao iniciar sessão; abra só quando precisar de histórico específico ou o Joab pedir. Nunca apague entradas antigas.
- **`LESSONS.md`** — registre erros, acertos e pendências não resolvidas, no mesmo ritmo do changelog. Diferente do changelog, **pode e deve ser consultado** quando relevante para a tarefa atual.

## Linear — banco de tarefas do projeto (Joab, 2026-09-19)

Projeto `teoftsao` no Linear (workspace Joabse, time JOA), via ferramentas `mcp__claude_ai_Linear__*`. **Sempre que você identificar algo para resolver/executar no futuro** (pendência, divergência, decisão a tomar, próximo passo) — não só o que o Joab pedir diretamente — crie uma issue com `save_issue` (`team: "Joabse"`, `project: "teoftsao"`), título com prefixo da matéria entre colchetes, descrição com contexto e passos. Não basta anotar isso em memória/changelog: tem que virar tarefa executável no Linear.

## Scripts de Processamento (materias/biblia3/)

Scripts Python autônomos, de uso único, para reparo de OCR e consolidação de capítulos específicos (prefixos `_consolida_`, `_repara_`, `_fix`, `_diag`, `_dbg`). Cada um tem caminhos absolutos Windows hardcoded para um arquivo específico (ex.: `RAW = r"E:\...\08-Witherington_Joao.md"`) e não são uma biblioteca reutilizável. Executar individualmente com `python <script>.py`; não usar como base para uma nova ferramenta genérica sem adaptar os caminhos.

## Papéis da Equipe de Agentes

**Papel = terminal, não LLM.** A tabela mostra o papel fixo de cada terminal e quem o ocupa hoje — a ocupação pode mudar a critério do Joab.

| Terminal (papel) | Função | Ocupante atual (2026-09-19) |
|---|---|---|
| ftsalider | Líder/Orquestrador. Coordena os 3 teólogos e o comitador, distribui tarefas, valida com o usuário, registra na memória. Não produz rascunhos teológicos diretamente. | Claude Code |
| Teólogo 1 | Analisa materiais em `fontes/` e produz rascunhos | Claude Code (terminal dedicado) |
| Teólogo 2 | Idem | Codex CLI (você, hoje) |
| Teólogo 3 | Idem | Antigravity |
| comitador | Faz commits git a pedido do ftsalider, com a descrição que ele fornecer. Nunca decide sozinho o que comitar. | Claude Code (terminal dedicado) |

Outros agentes (sem um dos 5 terminais nomeados):

| Agente | Função |
|---|---|
| file2md | Converte originais para Markdown (contexto isolado por arquivo — sempre reenviar instruções completas) |
| Bereano | Detector de IA — aprova/reprova no ciclo de humanização |
| Escriba | Humaniza textos reprovados pelo Bereano |
| tecfix | Manutenção técnica do projeto e ambiente Orca (não produz conteúdo teológico) |

Teólogos podem buscar a Bíblia (texto, comentários, léxicos) via MCPs de busca ou pelo browser integrado do Orca (`orca tab`) sem pedir autorização, mas as notas de `fontes/` são sempre a fonte primária — em conflito, prevalece o material enviado. Questões de múltipla escolha exigem tabela-resumo final (resposta de cada teólogo + sugestão de quem estiver no ftsalider).

## Operação com Orca
- O projeto está registrado no Orca como repositório de pasta (`teoftsao`), rodando em **5 terminais nomeados** com papel fixo e ocupante variável: `ftsalider`, `Teólogo 1`, `Teólogo 2` (você, Codex, hoje), `Teólogo 3`, `comitador`.
- Agentes podem ser executados em abas dedicadas via `orca terminal create` (`claude`, `codex`, `agy`) — o comando usado determina a LLM, mas o `--title` é que define o papel.
- A documentação e comandos específicos do Orca encontram-se em `ORCA.md`.

## Sincronização multi-LLM (Joab, 2026-09-19)

O projeto precisa ser entendido por qualquer LLM que trabalhe nele — não só o Claude Code. **Regra para o ftsalider (e para qualquer agente que alterar regras/estrutura do projeto): toda vez que `CLAUDE.md`, `AGENTS.md`, `ESTRUTURA.md` ou `ORCA.md` mudar, propague a mesma mudança para TODOS os arquivos de instrução por ferramenta**, listados na tabela abaixo, para que todas as LLMs sigam as mesmas regras e a mesma execução que o Claude tem:

| Arquivo | Ferramenta | Status |
|---|---|---|
| `CLAUDE.md` | Claude Code | wrapper (consolida AGENTS.md + ESTRUTURA.md + ORCA.md) |
| `AGENTS.md` | Codex CLI, opencode, e demais CLIs do padrão AGENTS.md | canônico (este arquivo) |
| `GEMINI.md` | Antigravity | wrapper |
| `QWEN.md` | Qwen Code | wrapper |
| `.clinerules` | Cline | wrapper |
| — | **mmx** | não aplicável — CLI da MiniMax para configurar outros agentes (Claude Code, Codex, opencode, grok, hermes, pi); não lê arquivos de projeto |
| — | **Kimi Code, DeepSeek** | removidos/não usados no projeto (Joab, 2026-09-19, JOA-19) — sem wrapper por ora |

Se uma ferramenta nova aparecer sem convenção de arquivo conhecida, ela deve encontrar orientação lendo `AGENTS.md` (padrão de fato do ecossistema) — e, se depois descobrirmos que ela usa um nome de arquivo próprio, crie o wrapper e registre isso no `CHANGELOG.md`.
