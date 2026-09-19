# Repository Guidelines

> Repositório Git privado (`joabse/teoftsa`) gerenciado no Orca — workspace de uma equipe de agentes de IA (FTSA) que produz textos teológicos a partir de materiais de estudo. Ver `ESTRUTURA.md` para o detalhamento completo de papéis e regras, e `ORCA.md` para instruções de operação no Orca.

## Execução pelo Codex

- Este arquivo é a configuração de projeto reconhecida pelo Codex CLI. Execute o Codex a partir da raiz `E:\00_ATUAL\04_PROJETO\teoftsa`; não crie nem exija um repositório Git para trabalhar aqui.
- O Codex atua como **2º teólogo** da FTSA. Não assume as funções de `file2md`, Bereano, Escriba ou `tecfix`, salvo pedido explícito do usuário ou do líder.
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

## Scripts de Processamento (materias/biblia3/)

Scripts Python autônomos, de uso único, para reparo de OCR e consolidação de capítulos específicos (prefixos `_consolida_`, `_repara_`, `_fix`, `_diag`, `_dbg`). Cada um tem caminhos absolutos Windows hardcoded para um arquivo específico (ex.: `RAW = r"E:\...\08-Witherington_Joao.md"`) e não são uma biblioteca reutilizável. Executar individualmente com `python <script>.py`; não usar como base para uma nova ferramenta genérica sem adaptar os caminhos.

## Papéis da Equipe de Agentes

| Agente | Função |
|---|---|
| ftsalider | Líder — coordena, distribui tarefas, valida com o usuário, registra na memória |
| Claude Code / Codex CLI / Antigravity | **Únicos teólogos** — analisam materiais em `fontes/` e produzem rascunhos |
| file2md | Converte originais para Markdown (contexto isolado por arquivo — sempre reenviar instruções completas) |
| Bereano | Detector de IA — aprova/reprova no ciclo de humanização |
| Escriba | Humaniza textos reprovados pelo Bereano |
| tecfix | Manutenção técnica do projeto, ambiente Orca e AionUi (não produz conteúdo teológico) |

Teólogos podem buscar a Bíblia (texto, comentários, léxicos) via MCPs de busca ou pelo browser integrado do Orca (`orca tab`) sem pedir autorização, mas as notas de `fontes/` são sempre a fonte primária — em conflito, prevalece o material enviado. Questões de múltipla escolha exigem tabela-resumo final (resposta de cada teólogo + sugestão do líder).

## Operação com Orca
- O projeto está registrado no Orca como repositório de pasta (`teoftsa`).
- Agentes podem ser executados em abas dedicadas via `orca terminal create` (`claude`, `codex`, `agy`).
- A documentação e comandos específicos do Orca encontram-se em `ORCA.md`.
