# -*- coding: utf-8 -*-
"""Checa U+FFFD e acentuação real no arquivo 05."""
from pathlib import Path
t = Path(r"01_markdown\adicionais\05-Witherington_Sinoticos.md").read_text(encoding="utf-8")
print("U+FFFD count:", t.count("\ufffd"))
print("'ção' count:", t.count("ção"))
print("'não' count:", t.count("não"))
print("'á' count:", t.count("á"), "| 'é':", t.count("é"), "| 'ô':", t.count("ô"))
i = t.find("mission")
print(repr(t[i - 30:i + 30]))
i = t.find("EXERC")
print(repr(t[i:i + 60]))
