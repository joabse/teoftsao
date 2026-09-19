# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md").read_text(encoding="utf-8")
for pat in ["inclusive no primeiro", "implicações políticas", "Em todo caso", "## João"]:
    i = t.find(pat)
    print("=" * 15, pat, "->", i)
    if i >= 0:
        print(repr(t[max(0, i - 60):i + 120]))
    print()
