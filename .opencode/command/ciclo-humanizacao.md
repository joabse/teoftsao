---
description: Executa o ciclo de humanização FTSA (Bereano → Escriba) sobre um rascunho, repetindo até aprovação, e o move para 04_aprovados.
---

Execute o **ciclo de humanização FTSA** sobre o texto: $ARGUMENTS

Etapas (repita até aprovação):

1. **Bereano:** envie o texto atual ao subagente `bereano` (via task) pedindo veredito no formato obrigatório.
2. **Se APROVADO:** finalize o ciclo — informe quantas versões foram necessárias e vá ao passo 4.
3. **Se REPROVADO:** envie o texto + veredito ao subagente `escriba` (via task) para humanizar e gravar a próxima versão numerada em `materias/<materia>/03_revisao/` (nunca sobrescrever versão anterior). Volte ao passo 1 usando o arquivo recém-gerado. Limite prático: se após 4 versões o Bereano continuar reprovando, pare e reporte os pontos persistentes ao usuário.
4. **Aprovação:** mova a versão aprovada para `materias/<materia>/04_aprovados/` (padrão de nome já usado na pasta) e registre a entrada no registro de memória da matéria (`ftsabrain/memoria/materias/<materia>/registro.md`) com data, agentes atuantes, resultado e caminhos.
5. Nunca altere arquivos em `00_originais/`; nunca grave texto não aprovado em `04_aprovados/`.
