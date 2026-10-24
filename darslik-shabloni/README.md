# Darslik shabloni

Shamsiyev uslubidagi A4 PDF darsligi uchun toza, qayta ishlatiladigan boshlang'ich qolip.

U quyidagilarni bir xil uslubda yaratadi:

- yuqori chapdagi qizil `shamsiyev` logotip bloki;
- o'ngdagi mavzu nomi va sahifa raqami;
- serif asosiy matn hamda sans-serif navigatsiya elementlari;
- pastdagi `shamsiyev.uz` footer;
- bitta mutlaqo bo'sh A4 darslik sahifasi.

PDFning o'zida qo'llanma yoki texnik izoh yo'q. U faqat tayyor, bo'sh sahifa
qolipi; ushbu README esa undan foydalanish uchun yagona yo'riqnomadir.

## Ishga tushirish

1. Python 3.10 yoki yangirog'ini o'rnating.
2. Kerakli kutubxonani o'rnating: `python -m pip install -r requirements.txt`.
3. PDF yarating:

   ```bash
   python generate_template.py --title "Rus tili: yangi mavzu" --output Darslik_shabloni.pdf
   ```

`Darslik_shabloni.pdf` shu buyruq bilan yaratilgan tekshirilgan namunadir. U
bitta bo'sh sahifadan iborat.

## Moslashtirish

`--title` orqali sahifa headeridagi mavzu nomi belgilanadi. Brend yozuvi va footer qiymatlari esa `generate_template.py` faylining yuqori qismidagi `BRAND_NAME` hamda `FOOTER_TEXT` konstantalarida turadi.

Keyingi to'liq darsliklar uchun qoida quyidagicha: avval Markdown yoki mavzu matni tayyorlanadi, keyin shu vizual tizim bilan PDFga chiqariladi. Tavsiya etiladigan pedagogik ketma-ketlik: kirish va maqsad → sxema/jadval → qoida → ikki tilli misol → `Xato / To'g'ri` → mashq → javoblar → xulosa.
