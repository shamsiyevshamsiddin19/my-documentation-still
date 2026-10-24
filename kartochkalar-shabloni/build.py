#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""data.py dagi gaplardan ikki tomonlama kartochkalar uchun index.html yasaydi.

Varaq: 2 ustun x 3 qator = 6 ta kartochka.
Har bir varaq uchun 2 ta PDF sahifasi chiqadi:
  1) old tomon  — o'zbekcha
  2) orqa tomon — ruscha + grammatik izoh

MUHIM: qog'ozning orqasiga chop etilganda sahifa gorizontal ko'zguga aylanadi,
shuning uchun orqa varaqda ustunlar o'rni almashtiriladi. Aks holda 1-kartochkaning
orqasida 2-gapning tarjimasi chiqib qoladi.

  AG'DARISH = "uzun"  -> uzun chet bo'ylab ag'daradigan printer (odatiy)
  AG'DARISH = "qisqa" -> qisqa chet bo'ylab ag'daradigan printer
"""
import html as H
import os
import re

import data

HERE = os.path.dirname(os.path.abspath(__file__))

USTUN = 2
QATOR = 3
BIR_VARAQ = USTUN * QATOR

AGDARISH = "uzun"      # "uzun" yoki "qisqa"


def belgila(matn: str) -> str:
    s = H.escape(matn)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r'<span class="t">\1</span>', s)
    return s


def kozgu(varaq):
    """Orqa tomon uchun kataklar tartibini printer ag'darishiga moslaydi."""
    satrlar = [varaq[r * USTUN:(r + 1) * USTUN] for r in range(QATOR)]
    if AGDARISH == "uzun":
        # chap-o'ng ko'zgu: har bir satr ichida ustunlar teskari
        satrlar = [list(reversed(s)) for s in satrlar]
    else:
        # yuqori-past ko'zgu: satrlar teskari tartibda
        satrlar = list(reversed(satrlar))
    return [k for s in satrlar for k in s]


def katak(element, tomon):
    """element = (raqam, nom, gap, izoh) yoki None (bo'sh katak)."""
    if element is None:
        return '<td class="bosh"></td>'
    raqam, nom, gap, izoh = element

    yorliq = f'<div class="yorliq">{raqam:02d}</div>'
    nomi = f'<div class="nom">{H.escape(nom)}</div>'
    # orqa tomonda yorliq o'ngda — ag'darilganda old tomondagi burchakka tushadi
    tasma = (f'<div class="tasma">{nomi}{yorliq}</div>' if tomon == "orqa"
             else f'<div class="tasma">{yorliq}{nomi}</div>')

    ichi = [tasma, f'<div class="tana"><div class="gap">{belgila(gap)}</div></div>']
    if izoh:
        ichi.append(f'<div class="izoh">{belgila(izoh)}</div>')
    return f'<td><div class="karta {tomon}">{"".join(ichi)}</div></td>'


def jadval(kataklar, tomon):
    satrlar = []
    for r in range(QATOR):
        hujayralar = "".join(
            katak(kataklar[r * USTUN + c], tomon) for c in range(USTUN)
        )
        satrlar.append(f"<tr>{hujayralar}</tr>")
    return (
        '<div class="varaq"><table class="tor">\n  '
        + "\n  ".join(satrlar)
        + "\n</table></div>"
    )


def qur() -> str:
    gaplar = data.GAPLAR
    varaqlar = []

    for boshi in range(0, len(gaplar), BIR_VARAQ):
        bolak = gaplar[boshi:boshi + BIR_VARAQ]
        bolak = bolak + [None] * (BIR_VARAQ - len(bolak))

        old, orqa = [], []
        for i, el in enumerate(bolak):
            n = boshi + i + 1
            old.append(None if el is None else (n, "O'ZBEKCHA", el[0], None))
            orqa.append(None if el is None else (n, el[3], el[1], el[2]))

        varaqlar.append(jadval(old, "old"))
        varaqlar.append(jadval(kozgu(orqa), "orqa"))

    return f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<title>{H.escape(data.SARLAVHA)}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
{chr(10).join(varaqlar)}
</body>
</html>
"""


if __name__ == "__main__":
    n = len(data.GAPLAR)
    varaq = -(-n // BIR_VARAQ)
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(qur())
    print(f"index.html yozildi — {n} ta kartochka, {varaq} varaq "
          f"({varaq * 2} PDF sahifa), ag'darish: {AGDARISH} chet")
    if n % BIR_VARAQ:
        print(f"  oxirgi varaqda {BIR_VARAQ - n % BIR_VARAQ} ta katak bo'sh qoladi")
