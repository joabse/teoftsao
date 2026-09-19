---
tipo: moc
atualizado_em: 2026-09-12
tags:
  - moc
---

# 📚 Matérias — MOC

> Map of Content: índice geral das matérias do projeto FTSA. Este vault (`ftsabrain`) é o **cérebro do projeto** — todo conhecimento extraído dos materiais fica aqui, consultado pelos teólogos (Claude Code, Codex CLI, Antigravity, gbooklm). Fluxo e papéis: [[pipeline]].

## Matérias

| Matéria | Nota principal | Status |
|---|---|---|
| Bíblia 2 | [[materias/biblia2/00-visao-geral\|Bíblia 2]] | Materiais convertidos |
| Bíblia 3 | [[materias/biblia3/00-visao-geral\|Bíblia 3]] | Estrutura criada |
| _TEMPLATE | [[materias/_TEMPLATE/00-visao-geral\|Modelo de matéria]] | Modelo (copiar; não usar como matéria real) |

## Memória de trabalho

Toda etapa concluída do projeto é registrada na memória (log por matéria):

- Registro geral do projeto (montagem, manutenção, estrutura): [[memoria/00-registro-geral|Registro Geral]]
- Registro da matéria Bíblia 2: [[memoria/materias/biblia2/registro|Registro Bíblia 2]]
- Registro da matéria Bíblia 3: [[memoria/materias/biblia3/registro|Registro Bíblia 3]]
- Modelo de registro para novas matérias: [[memoria/materias/_TEMPLATE/registro|Modelo de registro]]
- Nova matéria = criar também `memoria\materias\<nome>\registro.md` (copiar o modelo).

## Como registrar nova matéria

1. Copie a pasta `materias\_TEMPLATE\` dentro deste vault renomeando para o nome da disciplina (minúsculas, hífens).
2. Preencha o frontmatter e o título do `00-visao-geral.md` copiado.
3. Adicione a linha na tabela acima com link `[[materias/<nome>/00-visao-geral|Nome da Matéria]]`.
4. Não esqueça da pasta de trabalho correspondente em `..\materias\<nome>\` (copiar `_TEMPLATE` de lá — ver README).

## Notas rápidas

- Conhecimento de fontes vai em `materias\<nome>\fontes\` (uma nota por tema/fonte).
- Atualizar `atualizado_em` no frontmatter ao editar notas.
- Pipeline de produção e ciclo de humanização: [[pipeline]].
