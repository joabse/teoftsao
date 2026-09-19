# -*- coding: utf-8 -*-
from pathlib import Path
P = Path(r"01_markdown\adicionais\04-Alter_NTLiterGrecoRomana.md")
t = P.read_text(encoding="utf-8")
fixes = [
    ("nas edicatórias de Lucas", "nas dedicatórias de Lucas"),
    ("conseqiiéncia", "conseqüência"),
    ("Poética.é No Evangelho", "Poética.6 No Evangelho"),
]
for o, n in fixes:
    assert o in t, o
    t = t.replace(o, n)
P.write_text(t, encoding="utf-8")
print("ok -", len(t.splitlines()), "linhas,", len(t.encode('utf-8')), "bytes")
