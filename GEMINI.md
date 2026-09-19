# GEMINI.md — Diretrizes para Antigravity no Projeto teoftsao

> Este arquivo é carregado automaticamente pelo **Antigravity (`agy`)** no início de cada sessão neste diretório. Consolida as diretrizes de `AGENTS.md`, `ESTRUTURA.md` e `ORCA.md` para que o Antigravity (o **Teólogo 3** da equipe FTSA, terminal nomeado "Teólogo 3" no Orca) opere com máxima precisão, sem ambiguidades. **O líder da equipe (ftsalider) é o Claude Code** (terminal "ftsalider"), que orquestra o trabalho entre você, o Teólogo 1 (Claude Code em terminal dedicado), o Teólogo 2 (Codex CLI) e os demais agentes.

---

## 0. Regras Críticas (Obrigatórias)

1. **Controle de Versão:** Repositório Git privado (`joabse/teoftsao`) gerenciado no Orca. Manter o repositório leve respeitando o `.gitignore` (não versionar `00_originais/` e temporários de OCR).
2. **Idioma:** Toda a comunicação, documentação e textos produzidos devem ser estritamente em **português do Brasil**.
3. **`00_originais/` é imutável:** Arquivos brutos recebidos nunca são alterados. Qualquer conversão ou processamento gera novos arquivos nas pastas subsequentes.
4. **Fonte Primária Obrigatória (`fontes/`):** As notas de estudo em `ftsabrain/materias/<nome>/fontes/` são a base mandatória primária para qualquer análise ou rascunho. Buscas externas (Bíblia, léxicos, comentários) são puramente complementares; em qualquer divergência, **prevalece o material do curso**.
5. **Memória de Trabalho:** O progresso do projeto é registrado em `ftsabrain/memoria/` (`00-registro-geral.md` para marcos gerais e `materias/<nome>/registro.md` por matéria).
6. **Ciclo de Humanização:** Nenhum texto segue para `04_aprovados/` sem passar pelo Bereano (detector de IA) e, se reprovado, pelo Escriba em `03_revisao/` com versionamento numérico (`v1.md`, `v2.md`, etc.). Nunca sobrescrever versões anteriores.
7. **`CHANGELOG.md` (raiz):** registre toda alteração de estrutura/arquivos do projeto (data/hora, motivo) antes de um commit ou ao finalizar a tarefa. É banco de consulta — **não leia automaticamente** ao iniciar sessão; abra só quando precisar de histórico específico ou o Joab pedir. Nunca apague entradas antigas.
8. **`LESSONS.md` (raiz):** registre erros, acertos e pendências não resolvidas, no mesmo ritmo do changelog. Diferente dele, **pode e deve ser consultado** quando relevante para a tarefa atual.

---

## 1. Estrutura de Diretórios do Workspace

```
teoftsao\
├── GEMINI.md              ← este arquivo (carregado pelo Antigravity CLI)
├── CLAUDE.md              ← instruções para o Claude Code
├── AGENTS.md              ← diretrizes gerais compartilhadas
├── ESTRUTURA.md           ← detalhamento completo de papéis, pipeline e regras
├── ORCA.md                ← comandos e operação específica no Orca
├── skills-lock.json       ← bloqueio e metadados das skills instaladas
├── .agents\               ← customizações de workspace do Antigravity / agentes
│   ├── rules\             ← regras ativas do projeto (.agents/rules/*.md)
│   └── skills\            ← skills locais (convert-documents-to-markdown, humanizer, no-ai-slop)
├── materias\              ← uma pasta por disciplina/matéria
│   ├── README.md          ← documentação do fluxo de matérias
│   ├── _TEMPLATE\         ← modelo de pastas para novas disciplinas
│   ├── biblia2\           ← matéria Bíblia 2 (materiais convertidos)
│   ├── biblia3\           ← matéria Bíblia 3 (concluída)
│   └── <nome>\
│       ├── 00_originais\  ← arquivos brutos recebidos (imutáveis)
│       ├── 01_markdown\   ← convertidos pelo file2md
│       ├── 02_rascunhos\  ← textos teológicos produzidos
│       ├── 03_revisao\    ← ciclo de humanização versionado (v1.md, v2.md...)
│       └── 04_aprovados\  ← entregas finais validadas
└── ftsabrain\             ← vault Obsidian ("cérebro" do projeto)
    ├── materias.md        ← MOC/índice geral das matérias
    ├── pipeline.md        ← resumo do pipeline de produção
    ├── materias\<nome>\   ← notas temáticas (00-visao-geral.md + fontes\)
    └── memoria\           ← memória de trabalho (registro-geral e por matéria)
```

---

## 2. Pipeline de Produção (5 Etapas)

```
Usuário envia materiais
         │
         ▼
materias\<nome>\00_originais\        (imutável)
         │  file2md converte
         ▼
materias\<nome>\01_markdown\         (Markdown pronto para estudo)
         │  Teólogos estudam e produzem rascunhos
         ▼
materias\<nome>\02_rascunhos\        (textos produzidos pelos teólogos)
         │
         ▼
╔═════════════ CICLO DE HUMANIZAÇÃO ═════════════╗
║  texto ──► Bereano (detector de IA)            ║
║       aprovado? ── SIM ──► 04_aprovados\       ║
║       │ NÃO                                    ║
║       ▼                                        ║
║  Escriba humaniza → nova versão em 03_revisao\ ║
║       └──► volta ao Bereano (repete até OK)    ║
╚═════════════════════════════════════════════════╝
         │
         ▼
materias\<nome>\04_aprovados\   → Entrega final ao Joab
```

---

## 3. Papéis da Equipe FTSA

| Agente | Papel | Função Principal |
|---|---|---|
| **Claude Code** (terminal "ftsalider") | **ftsalider** — Líder da equipe | Orquestra o fluxo, distribui tarefas, valida respostas e registra a memória. Não produz rascunhos teológicos diretamente. |
| **Claude Code** (terminal "Teólogo 1") | Teólogo 1 | Análise e produção teológica. |
| **Codex CLI** | Teólogo 2 | Análise e produção teológica. |
| **Antigravity** (você) | **Teólogo 3** | Análise das fontes do curso, produção de rascunhos e reflexões teológicas. |
| **file2md** | Conversor | Transforma originais (PDFs, transcrições) em Markdown limpo. |
| **Bereano** | Detector de IA | Avalia os textos contra padrões sintéticos de IA; aprova ou reprova. |
| **Escriba** | Humanizador | Reescreve textos reprovados pelo Bereano para garantir tom natural. |
| **tecfix** | Manutenção técnica | Ajustes de infraestrutura, ambiente Orca e organização de pastas. |

*(Nota: 4 terminais nomeados no Orca desde 2026-09-19 — ftsalider, Teólogo 1, Teólogo 2, Teólogo 3. Claude Code ocupa dois papéis em terminais diferentes: ftsalider por padrão, Teólogo 1 só quando explicitamente designado nesse terminal.)*

---

## 4. Diretrizes Específicas para o Antigravity

1. **Pesquisa Externa Complementar:** Você tem autonomia para consultar a Bíblia, comentários e léxicos através de MCPs de busca ou pelo browser do Orca (`orca tab create` / `orca snapshot`), sem necessidade de autorização prévia. Sempre cite a fonte.
2. **Questões de Múltipla Escolha:** Forneça a letra escolhida, fundamentação teológica sucinta e a citação exata das fontes em `ftsabrain/materias/<nome>/fontes/`.
3. **Uso de Skills Locais:**
   - Para conversões de novos documentos: skill `convert-documents-to-markdown` em `.agents/skills/convert-documents-to-markdown/`.
   - Para suporte na detecção de IA e humanização: skills `no-ai-slop` e `humanizer` em `.agents/skills/`.
4. **Registro de Atividades:** Ao finalizar qualquer etapa relevante na ausência do líder, documente no arquivo correspondente em `ftsabrain/memoria/`.
