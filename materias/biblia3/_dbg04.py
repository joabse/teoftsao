# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(r"01_markdown\adicionais\04-Alter_NTLiterGrecoRomana.md").read_text(encoding="utf-8")
for pat in ["Visto que muitos antes", "4 T", "62-63", "Essa posi", "Epistol", "398a11", "de língua grega, do Império"]:
    i = t.find(pat)
    print("=" * 20, pat, "->", i)
    if i >= 0:
        seg = t[max(0, i - 80):i + 420]
        print(repr(seg))
    print()
