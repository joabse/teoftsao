# -*- coding: utf-8 -*-
from pathlib import Path
import re
p = Path(r"01_markdown\adicionais\06-Witherington_Evangelhos.md")
t = p.read_text(encoding="utf-8")
for o, n in [
    ("que também encontramos nele. ## MATEUS", "que também encontramos nele.\n\n## MATEUS"),
    ("Jerusalém.‘ A estrutura", "Jerusalém.⁷ A estrutura"),
    ("‘10 V. minha discussão", "10 V. minha discussão"),
]:
    assert o in t, o
    t = t.replace(o, n)
t = re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"
p.write_text(t, encoding="utf-8")
print("ok", len(t.splitlines()), "linhas,", len(t.encode("utf-8")), "bytes")
