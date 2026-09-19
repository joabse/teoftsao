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

| Papel FTSA | Executável / Agente no Orca | Como Ativar no Orca | Finalidade |
|---|---|---|---|
| **ftsalider** | `claude` (Claude Code) | Sessão principal do Claude Code no Orca | Orquestra toda a equipe: distribui tarefas a Codex CLI e Antigravity, valida respostas com o Joab, registra a memória. **Não produz rascunhos teológicos diretamente** (desde 2026-09-19). |
| **Codex CLI** | `codex` | `orca terminal create --title "Teólogo Codex" --command "codex"` | 1º Teólogo — análise e produção teológica. |
| **Antigravity** | `agy` | `orca terminal create --title "Teólogo Antigravity" --command "agy"` | 2º Teólogo — análise e produção teológica. |
| **file2md** | Script / CLI de conversão | Terminal sob demanda | Conversão de originais para Markdown em `01_markdown/`. |
| **Bereano** | Prompt / Sessão dedicada | Terminal ou prompt de verificação | Detecção de marcas de IA nos rascunhos em `02_rascunhos/`. |
| **Escriba** | Prompt / Sessão dedicada | Terminal de redação | Humanização e reescrita de textos reprovados em `03_revisao/`. |
| **tecfix** | Manutenção técnica | Terminal shell (pwsh/bash) | Ajustes na infraestrutura, scripts de OCR e pastas. |

---

## 3. Comandos Úteis do Orca para o Projeto

### 3.1 Gerenciamento de Terminais dos Agentes
Você (Claude Code / ftsalider) roda na sessão principal e abre abas dedicadas para os teólogos:
```bash
# Iniciar o Codex CLI (1º Teólogo)
orca terminal create --title "Teologo Codex" --command "codex" --json

# Iniciar o Antigravity CLI (2º Teólogo)
orca terminal create --title "Teologo Antigravity" --command "agy" --json
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
