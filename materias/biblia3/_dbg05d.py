# -*- coding: utf-8 -*-
from pathlib import Path
t = Path(r"01_markdown\adicionais\05-Witherington_Sinoticos.md").read_text(encoding="utf-8")
for pat in ["Uma abreviatura", "Estou sugerindo", "levantamento feito",
            "atuais", "Contra falsas", "O precursor", "Oriente e ocidente",
            "um assunto", "listados de Mateus", "da Paixão que", "observe como",
            "conhece uma", "a execução", "Teófilo", "importância histórica",
            "não era necessário", "no rolo de Qumran", "de Deus.”", "Paixão.”", "ocor"]:
    i = t.find(pat)
    print("=" * 15, pat, "->", i)
    if i >= 0:
        print(repr(t[max(0, i - 90):i + 330]))
    print()
