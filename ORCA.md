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

Desde 2026-09-19, o Joab nomeou 4 terminais fixos no Orca para este projeto: **ftsalider**, **Teólogo 1**, **Teólogo 2**, **Teólogo 3**.

| Terminal (nome no Orca) | Executável / Agente | Papel FTSA | Finalidade |
|---|---|---|---|
| **ftsalider** | `claude` (Claude Code) | Líder/Orquestrador | Orquestra toda a equipe: distribui tarefas aos 3 teólogos, valida respostas com o Joab, registra a memória. **Não produz rascunhos teológicos diretamente.** |
| **Teólogo 1** | `claude` (Claude Code) | Teólogo | Análise e produção teológica. Terminal separado do ftsalider — mesmo agente (Claude Code), papel diferente. |
| **Teólogo 2** | `codex` | Teólogo | Análise e produção teológica. |
| **Teólogo 3** | `agy` (Antigravity) | Teólogo | Análise e produção teológica. |
| — | Script / CLI de conversão (**file2md**) | Conversor | Terminal sob demanda — conversão de originais para Markdown em `01_markdown/`. |
| — | Prompt / Sessão dedicada (**Bereano**) | Detector de IA | Terminal ou prompt de verificação — detecção de marcas de IA nos rascunhos em `02_rascunhos/`. |
| — | Prompt / Sessão dedicada (**Escriba**) | Humanizador | Terminal de redação — humanização e reescrita de textos reprovados em `03_revisao/`. |
| — | Manutenção técnica (**tecfix**) | Manutenção | Terminal shell (pwsh/bash) — ajustes na infraestrutura, scripts de OCR e pastas. |

---

## 3. Comandos Úteis do Orca para o Projeto

### 3.1 Gerenciamento de Terminais dos Agentes
Você (Claude Code / ftsalider) roda no terminal "ftsalider" e usa os terminais nomeados dos teólogos (Teólogo 1 = Claude Code em outro terminal; Teólogo 2 = Codex CLI; Teólogo 3 = Antigravity). Para criar novos terminais de teólogo quando necessário:
```bash
# Iniciar mais um Claude Code (ex.: Teólogo 1, se não estiver aberto)
orca terminal create --title "Teologo 1" --command "claude" --json

# Iniciar o Codex CLI (Teólogo 2)
orca terminal create --title "Teologo 2" --command "codex" --json

# Iniciar o Antigravity CLI (Teólogo 3)
orca terminal create --title "Teologo 3" --command "agy" --json
```

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
2. **Contexto Isolado para Conversões:** Diferente de outros ambientes onde o contexto acumula, no Orca basta criar um terminal novo ou isolado para cada conversão do `file2md`.
3. **Ciclo de Humanização:**
   - Textos produzidos pelos teólogos vão para `materias/<materia>/02_rascunhos/`.
   - São submetidos ao Bereano. Se reprovados, o Escriba grava em `materias/<materia>/03_revisao/v{n}.md`.
   - Somente após aprovação do Bereano o arquivo é movido para `04_aprovados/`.
4. **Memória Contínua:** Toda etapa finalizada deve ser registrada pelo líder (você, Claude Code/ftsalider) em `ftsabrain/memoria/`.
