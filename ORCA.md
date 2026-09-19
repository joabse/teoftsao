# ORCA.md — Guia de Operação da Equipe FTSA no Orca

> Este documento estabelece como a equipe de agentes de IA (**FTSA**) opera dentro do ambiente **Orca** no projeto `teoftsao`.

---

## 1. Visão Geral

O projeto **teoftsao** é um workspace colaborativo onde agentes de IA produzem textos e reflexões teológicas a partir de materiais acadêmicos (apostilas, livros, transcrições de aulas).

No **Orca**, o projeto é gerenciado como um espaço de trabalho multissessão, permitindo:
- Terminais independentes e paralelos para os diferentes papéis da equipe.
- Sessões limpas e isoladas para conversões do `file2md`.
- Navegador integrado (`orca tab`) para pesquisas bíblicas e teológicas complementares pelos teólogos.
- Orquestração estruturada via CLI (`orca terminal`, `orca orchestration`, `orca worktree`).

---

## 2. Mapeamento da Equipe FTSA no Orca

Desde 2026-09-19, o Joab nomeou 6 terminais fixos no Orca para este projeto: **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3**, **comitador** e **file2md**. **O papel FTSA pertence ao nome do terminal — é fixo. Quem/qual LLM ocupa cada terminal é um estado, não uma regra**, e o Joab pode trocar a qualquer momento (ex.: trocar o líder para Antigravity, Codex ou Claude Code). A coluna "Executável / Agente" abaixo é a ocupação **atual**.

| Terminal (nome no Orca) | Executável / Agente (ocupante atual) | Papel FTSA (fixo) | Finalidade |
|---|---|---|---|
| **ftsalider** | `agy` (Antigravity) | Líder/Orquestrador | Orquestra toda a equipe: distribui tarefas aos 3 teólogos, ao comitador e ao file2md, valida respostas com o Joab, registra a memória. **Não produz rascunhos teológicos diretamente.** |
| **Teólogo 1** | `claude` (Claude Code) | Teólogo | Análise e produção teológica. Terminal separado do ftsalider. |
| **Teólogo 2** | `codex` | Teólogo | Análise e produção teológica. |
| **Teólogo 3** | `agy` (Antigravity) | Teólogo | Análise e produção teológica. |
| **comitador** | `cline` (Cline) | Comitador | Faz commits git a pedido do ftsalider, com a descrição detalhada que ele fornecer. Verificar sempre qual LLM/CLI ocupa este terminal para adaptar a sintaxe do comando. |
| **file2md** | Shell / Agente (`pwsh` / CLI dedicada) | Conversor | Converte originais para Markdown em `01_markdown/` via `anydoc` ou OCR, alimenta `ftsabrain/file2md/` e registra em `00-indice.md`. O líder sempre verifica modelo/CLI antes de despachar. |
| — | Prompt / Sessão dedicada (**Bereano**) | Detector de IA | Terminal ou prompt de verificação — detecção de marcas de IA nos rascunhos em `02_rascunhos/`. |
| — | Prompt / Sessão dedicada (**Escriba**) | Humanizador | Terminal de redação — humanização e reescrita de textos reprovados em `03_revisao/`. |
| — | Manutenção técnica (**tecfix**) | Manutenção | Terminal shell (pwsh/bash) — ajustes na infraestrutura, scripts de OCR e pastas. |

---

## 3. Comandos Úteis do Orca para o Projeto

### 3.1 Gerenciamento de Terminais dos Agentes
Quem estiver no terminal "ftsalider" (hoje Claude Code) usa os terminais nomeados dos teólogos (hoje: Teólogo 1 = Claude Code em outro terminal; Teólogo 2 = Codex CLI; Teólogo 3 = Antigravity — mas o `--command` pode apontar para qualquer LLM, a critério do Joab). Para criar novos terminais de teólogo quando necessário:
```bash
# Iniciar mais um Claude Code (ex.: Teólogo 1, se não estiver aberto)
orca terminal create --title "Teologo 1" --command "claude" --json

# Iniciar o Codex CLI (Teólogo 2)
orca terminal create --title "Teologo 2" --command "codex" --json

# Iniciar o Antigravity CLI (Teólogo 3)
orca terminal create --title "Teologo 3" --command "agy" --json

# Iniciar o comitador (se não estiver aberto) — hoje ocupado por Cline
orca terminal create --title "comitador" --command "cline" --json

# Iniciar o terminal file2md (se não estiver aberto)
orca terminal create --title "file2md" --json
```

Fluxo de commit: o ftsalider redige a descrição detalhada e envia ao comitador via `orca terminal send` (ver `CLAUDE.md`, seção 4.1) — nunca comita diretamente.

Listar e monitorar terminais ativos:
```bash
# Ver lista de terminais
orca terminal list --json

# Ler o buffer do terminal de um teólogo
orca terminal read --terminal <handle> --limit 50 --json

# Enviar instrução/questão para o terminal
orca terminal send --terminal <handle> --text "Analise a questão 1 com base nas notas em fontes/" --enter --wait-submit 5 --json
```

### 3.2 Navegador Integrado para Pesquisa Bíblica
Teólogos podem utilizar o browser embutido do Orca para consultar textos em fontes bíblicas externas (Bible Gateway, Blue Letter Bible, etc.) sem sair do ambiente:
```bash
# Abrir aba de pesquisa bíblica
orca tab create --url "https://www.biblegateway.com/" --json

# Tirar snapshot da página para extrair versículos/comentários
orca snapshot
```

### 3.3 Status do Projeto e Espaço de Trabalho
```bash
# Verificar status da instância Orca
orca status --json

# Listar worktrees e agentes ativos
orca worktree ps --json
```

---

## 4. Regras Operacionais no Orca

1. **Prioridade das Fontes:** As notas em `ftsabrain/materias/<materia>/fontes/` são sempre a fonte mandatória primária.
2. **Terminal file2md e Alimentação Contínua do ftsabrain:** O agente opera no terminal nomeado `file2md`. O líder sempre verifica o modelo e a CLI em execução no terminal antes de despachar tarefas. Utiliza primariamente `anydoc` para documentos nativos e OCR local para PDFs escaneados. Cada conversão alimenta `ftsabrain/file2md/` e é registrada com timestamp no índice central `ftsabrain/file2md/00-indice.md`.
3. **Ciclo de Humanização:**
   - Textos produzidos pelos teólogos vão para `materias/<materia>/02_rascunhos/`.
   - São submetidos ao Bereano. Se reprovados, o Escriba grava em `materias/<materia>/03_revisao/v{n}.md`.
   - Somente após aprovação do Bereano o arquivo é movido para `04_aprovados/`.
4. **Memória Contínua:** Toda etapa finalizada deve ser registrada por quem estiver no terminal ftsalider (hoje Antigravity) em `ftsabrain/memoria/`.
