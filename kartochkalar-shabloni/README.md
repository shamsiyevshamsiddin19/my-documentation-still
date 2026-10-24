# Yordamchi so'zlar kartochkalari shabloni

O'zbekcha gapni rus tiliga og'zaki tarjima qilish mashqi uchun ikki tomonlama,
qayta ishlatiladigan kartochka shabloni. A4 qog'ozga **orqa-oldi** chop etiladi
va **3 ta to'g'ri chiziq bo'ylab** qirqiladi. Tayyor PDFda faqat
kartochkalarning o'zi bor; chop etish va tahrirlash bo'yicha barcha ma'lumotlar
shu README'da.

- A4 varaq aniq **6 ga bo'linadi**: har biri **105 × 99 mm**
- Kartochkalar bir-biriga tegib turadi — oraliq yo'lak **yo'q**
- Old tomon — o'zbekcha gap · Orqa tomon — ruscha tarjima + grammatik izoh

## Qirqish

```
   ┌───────────┬───────────┐
   │     01    │     02    │
   ├───────────┼───────────┤   ← gorizontal qirqish (99 mm)
   │     03    │     04    │
   ├───────────┼───────────┤   ← gorizontal qirqish (198 mm)
   │     05    │     06    │
   └───────────┴───────────┘
               ↑
         vertikal qirqish (105 mm)
```

**Jami 3 ta qirqish:** 1 vertikal + 2 gorizontal. Chiziqlar varaqning bir
chetidan ikkinchi chetigacha uzluksiz — lineyka qo'yib bir marta kesasiz.
Varaqning tashqi cheti kartochkaning o'z cheti, uni qirqish shart emas.

Butun siyoh kartochka chetidan **6 mm ichkarida**. Shuning uchun:

- printer qog'oz chetini chop eta olmasa ham (odatda ~5 mm) matn kesilmaydi;
- duplexda 1–2 mm siljish bo'lsa ham bilinmaydi;
- qirqishda biroz adashsangiz ham faqat oq joy kesiladi.

## Dizayn

"JWT va httpOnly Cookies" taqdimoti uslubida: qora sarlavha tasmasi, qizil
raqam yorlig'i, oq tana, qizil urg'u.

```
OLD TOMON                        ORQA TOMON
┌──────────────────────┐         ┌──────────────────────┐
│[01]  O'ZBEKCHA       │ qora    │       PREDLOG   [01] │
├──────────────────────┤         ├──────────────────────┤
│                      │         │  Из-за дождя́ мы      │
│  Yomg'ir sababli     │         │  оста́лись до́ма.      │
│  biz uyda qoldik.    │         ├──────────────────────┤
│                      │         │ из-за + Род. п. — …  │ ochiq fon
└──────────────────────┘         └──────────────────────┘
```

Orqa tomondagi raqam yorlig'i **o'ngda** — kartochka ag'darilganda u old
tomondagi yorliq bilan bir burchakka tushadi.

Ranglar: qora `#1F1F1F`, qizil `#D92229`, ochiq fon `#F7F7F5`.
Shriftlar: matn — Noto Sans, tasmadagi yorliqlar — Montserrat.

## Chop etish

1. `Kartochkalar_shabloni.pdf` ni oching.
2. Printerda **ikki tomonlama (duplex)** rejimini yoqing.
3. Ag'darish turi: **uzun chet bo'ylab** (long edge) — odatiy sozlama.
4. Masshtab: **100% / "Actual size"**. "Fit to page", "Shrink to fit" yoki
   "Scale to printable area" ni **albatta o'chiring** — aks holda varaq
   kichrayadi, 105/99 mm o'lchov buziladi va qirqish chiziqlari siljiydi.
5. Avval **bitta varaq** chiqarib tekshiring: 01-kartochkaning orqasida
   01-gapning tarjimasi turibdimi?

> Eslatma: ko'p printerlar qog'oz chetining ~5 mm ini chop eta olmaydi,
> shuning uchun qirqish chiziqlari varaq chetigacha yetib bormasligi mumkin.
> Bu muammo emas — ko'rinib turgan qismiga lineyka qo'yib davom ettiring.

Agar orqa tomon noto'g'ri tushsa — printeringiz qisqa chet bo'ylab
ag'daradi. `build.py` da:

```python
AGDARISH = "qisqa"
```

qilib qo'ying va qaytadan yig'ing.

## Nega ustunlar almashtirilgan?

Qog'ozning orqasiga chop etilganda sahifa **gorizontal ko'zguga** aylanadi.
Shuning uchun orqa varaqda kataklar teskari tartibda chiqariladi:

```
OLD  TOMON        ORQA TOMON (faylda)      QIRQILGANDAN KEYIN
01 | 02            02 | 01                  01 ning orqasida 01
03 | 04     →      04 | 03          →       03 ning orqasida 03
05 | 06            06 | 05                  ...
```

Buni `build.py` dagi `kozgu()` funksiyasi bajaradi.

## Quvur

```bash
npm run build           # data.py -> index.html -> Kartochkalar_shabloni.pdf
```

Talablar: Python 3.10+, Node.js 18+ hamda Google Chrome yoki Chromium.
Qo'shimcha Python yoki Node kutubxonasi kerak emas.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `data.py` | **Gaplar shu yerda.** Yangi gap qo'shish uchun faqat shuni tahrirlash kerak |
| `build.py` | Kartochka to'rini yig'adi, ko'zgu tartibini hisoblaydi |
| `style.css` | Maket va dizayn: A4, katak o'lchami, ranglar, qirqish chiziqlari |
| `index.html` | Yig'iladigan fayl — **qo'lda tahrirlanmaydi** |
| `fonts/` | Noto Sans (urg'u belgisi uchun sinovdan o'tgan) |
| `package.json` | Bitta buyruq bilan PDF yig'ish skripti |
| `Kartochkalar_shabloni.pdf` | Tekshirilgan, chop etishga tayyor namuna |

## Qoidalar

- **Shrift:** Noto Sans. Inter ishlatilmaydi — u `U+0301` urg'u belgisini
  keyingi harf ustiga tushiradi.
- **Urg'u:** ruscha ko'p bo'g'inli so'zlarda `U+0301` (`дождя́`). `ё` da
  qo'yilmaydi — u o'zi doim urg'uli.
- **Belgilash:** `**qalin**` — ajratiladigan qism, `` `atama` `` — izohdagi
  ruscha atama.
- **Yordamchi so'z turi:** har bir yozuvning 4-elementi — `PREDLOG`,
  `BOG'LOVCHI`, `YUKLAMA` yoki `KIRISH SO'Z`. U orqa tomondagi tasmada
  chiqadi.
- **Chetlar har tomondan teng (8 mm)** — duplexda old va orqa tomon aniq
  ustma-ust tushishi uchun. Buni o'zgartirmang.

## Holat

**72 kartochka · 12 varaq · 24 PDF sahifa · bo'sh katak yo'q.**

Gaplar turi bo'yicha guruhlangan — bir turni ketma-ket mashq qilish mumkin:

| Kartochka | Turi | Soni |
|:--|:--|--:|
| 01–24 | PREDLOG | 24 |
| 25–44 | BOG'LOVCHI | 20 |
| 45–58 | YUKLAMA | 14 |
| 59–72 | KIRISH SO'Z | 14 |

### Qamrab olingan yordamchi so'zlar

**Predloglar (24)**
`к` `от` `из` `для` `ради` `без` `из-за` `благодаря` `во время` `в течение`
`до` `после` `перед` `через` `сквозь` `среди` `около` `кроме` `вместо` `о/об`
`по` `с` `за` `при`

**Bog'lovchilar (20)**
`потому что` `так как` `поэтому` `хотя` `несмотря на то что` `зато` `если`
`если бы` `чтобы` (+infinitiv va +o'tgan zamon) `как только` `пока` `пока не`
`прежде чем` `в то время как` `с тех пор как` `чем … тем` `что` `ни … ни`
`как будто`

**Yuklamalar (14)**
`даже` `именно` `же` `-то` `разве` `неужели` `лишь` `только` `вот` `ли`
`ещё/уже` `бы` `не … а` `-нибудь`

**Kirish so'zlar (14)**
`по-моему` `тем не менее` `кстати` `ведь` `к сожалению` `вряд ли` `во-первых`
`во-вторых` `конечно` `может быть` `наверное` `значит` `кажется` `например`
`наоборот` `в общем` `главное` `честно говоря`

### Grammatik qamrov

O'tgan, hozirgi va kelasi zamon · buyruq mayli · shart mayli (`бы`) ·
СВ va НСВ juftliklari · qo'sh inkor (`никто́ … не`, `ни … ни`) · qiyosiy daraja ·
barcha olti kelishik.

### Yangi gap qo'shish

`data.py` ga yozing — tur konstantalari `P`, `B`, `Y`, `K`. Gaplar soni
**6 ga karrali** bo'lsin, aks holda oxirgi varaqda bo'sh katak qoladi.
