# -*- coding: utf-8 -*-
"""Yordamchi so'zlar kartochkalari uchun gaplar.

Har bir yozuv: (o'zbekcha, ruscha, izoh, tur)
  **qalin**  — kartochkada ajratib ko'rsatiladigan qism
  `atama`    — izohdagi ruscha atama
  tur        — PREDLOG | BOG'LOVCHI | YUKLAMA | KIRISH SO'Z (orqa tasmada chiqadi)

Ruscha so'zlarda urg'u U+0301 (combining acute) bilan qo'yiladi.
`ё` da urg'u qo'yilmaydi — u o'zi doim urg'uli.

Gaplar turi bo'yicha guruhlangan, shuning uchun bir turni ketma-ket mashq
qilish mumkin. Gaplar soni 6 ga karrali bo'lsin — shunda varaq to'liq to'ladi.
"""

SARLAVHA = "Rus tili — yordamchi so'zlar"

P, B, Y, K = "PREDLOG", "BOG'LOVCHI", "YUKLAMA", "KIRISH SO'Z"

GAPLAR = [

    # ═══════════════ PREDLOGLAR (1–24) ═══════════════
    ("Kechqurun **buvimnikiga** boramiz.",
     "Ве́чером мы пойдём **к** ба́бушке.",
     "`к` + Дат. п. — kimgadir tomon yo'nalish: `к врачу́`, `к дру́гу`", P),

    ("Men bu xabarni **ukamdan** eshitdim.",
     "Я узна́л э́ту но́вость **от** бра́та.",
     "`от` + Род. п. — manba. Shaxsdan — `от`, joydan — `из`", P),

    ("U **Samarqanddan** qaytdi.",
     "Он верну́лся **из** Самарка́нда.",
     "`из` + Род. п. — ichkaridan chiqish; `в` ning teskarisi", P),

    ("Bu sovg'ani **sen uchun** oldim.",
     "Я купи́л э́тот пода́рок **для** тебя́.",
     "`для` + Род. п. — kimga atalgan; `ради` dan farqli, qurbonlik ma'nosi yo'q", P),

    ("U oilasi **uchun** hamma narsaga tayyor.",
     "Он гото́в сде́лать всё **ра́ди** семьи́.",
     "`ради` + Род. п. — maqsad va manfaat («kim/nima haqqi»)", P),

    ("**Sensiz** boshlamaymiz.",
     "**Без** тебя́ мы не начнём.",
     "`без` + Род. п. — yo'qlik; `с` ning teskarisi", P),

    ("Yomg'ir **sababli** biz uyda qoldik.",
     "**Из-за** дождя́ мы оста́лись до́ма.",
     "`из-за` + Род. п. — salbiy sabab («yomon natija»)", P),

    ("Do'stimning yordami **tufayli** men imtihondan o'tdim.",
     "**Благодаря́** по́мощи дру́га я сдал экза́мен.",
     "`благодаря` + Дат. п. — ijobiy sabab; `из-за` ning antonimi", P),

    ("Dars **davomida** telefonni o'chirib qo'ying.",
     "**Во вре́мя** уро́ка вы́ключите телефо́н.",
     "`во время` + Род. п. — bir vaqtda sodir bo'lish; buyruq mayli", P),

    ("Men bu ishni bir hafta **ichida** tugataman.",
     "Я зако́нчу э́ту рабо́ту **в тече́ние** неде́ли.",
     "`в течение` + Род. п. — butun muddat davomiyligi; kelasi zamon СВ", P),

    ("**Kechgacha** hammasini ulgurishimiz kerak.",
     "Нам на́до всё успе́ть **до** ве́чера.",
     "`до` + Род. п. — vaqt chegarasi («-gacha»); `после` ning teskarisi", P),

    ("**Ishdan keyin** basseynga boraman.",
     "**По́сле** рабо́ты я хожу́ в бассе́йн.",
     "`после` + Род. п. — keyin; НСВ — odatiy, takrorlanuvchi ish", P),

    ("**Uchrashuvdan oldin** biroz hayajonlandim.",
     "**Пе́ред** встре́чей я немно́го волнова́лся.",
     "`перед` + Твор. п. — darhol oldin; `до` dan ko'ra yaqinroq vaqt", P),

    ("**Yarim soatdan keyin** qaytaman.",
     "Я верну́сь **че́рез** полчаса́.",
     "`через` + Вин. п. — qancha vaqtdan keyin; `сквозь` dan farqli, to'siq yo'q", P),

    ("Quyosh nuri parda **orasidan** xonaga tushardi.",
     "Со́лнечный свет проника́л в ко́мнату **сквозь** што́ры.",
     "`сквозь` + Вин. п. — to'siq ichidan o'tish; НСВ, davomli o'tgan zamon", P),

    ("**Tanishlarim orasida** hech kim bu haqda bilmaydi.",
     "**Среди́** мои́х знако́мых никто́ об э́том не зна́ет.",
     "`среди` + Род. п. — guruh ichida; qo'sh inkor: `никто́ … не`", P),

    ("Bu yerda **bir soatcha** kutdim.",
     "Я ждал здесь **о́коло** ча́са.",
     "`около` + Род. п. — taxminiy miqdor yoki yaqinlik («-cha», «yonida»)", P),

    ("**Mendan boshqa** hech kim kelmadi.",
     "**Кро́ме** меня́ никто́ не пришёл.",
     "`кроме` + Род. п. — istisno; ko'pincha inkor bilan birga keladi", P),

    ("**Dam olish o'rniga** u yana ishladi.",
     "**Вме́сто** о́тдыха он сно́ва рабо́тал.",
     "`вместо` + Род. п. — o'rniga, almashtirish", P),

    ("Biz kecha **kelajak rejalar haqida** gaplashdik.",
     "Вчера́ мы говори́ли **о** бу́дущих пла́нах.",
     "`о` + Предл. п. — mavzu («haqida»); unli oldidan `об`", P),

    ("U har kuni **qirg'oq bo'ylab** yuguradi.",
     "Он ка́ждый день бе́гает **по** на́бережной.",
     "`по` + Дат. п. — sirt bo'ylab harakat; НСВ, takrorlanuvchi", P),

    ("**Do'stim bilan** kinoga bordim.",
     "Я ходи́л в кино́ **с** дру́гом.",
     "`с` + Твор. п. — birgalik. `с` + Род. п. esa «-dan»: `со стола́`", P),

    ("U **stol ortida** o'tirib yozardi.",
     "Он сиде́л **за** столо́м и писа́л.",
     "`за` + Твор. п. — joylashuv (ortida); `за` + Вин. п. — yo'nalish yoki evaz", P),

    ("**Bolalar oldida** bunday gapirmang.",
     "**При** де́тях так не говори́те.",
     "`при` + Предл. п. — kimningdir huzurida; buyruq mayli inkor bilan", P),

    # ═══════════════ BOG'LOVCHILAR (25–44) ═══════════════
    ("Men bormadim, **chunki** o'zimni yomon his qildim.",
     "Я не пошёл, **потому́ что** пло́хо себя́ чу́вствовал.",
     "`потому что` — sabab bog'lovchisi; gap o'rtasida keladi, boshida emas", B),

    ("Men kech qoldim, **chunki** avtobus kelmadi.",
     "Я опозда́л, **так как** авто́бус не пришёл.",
     "`так как` — sabab; `потому что` dan farqli, gap boshida ham kela oladi", B),

    ("Yomg'ir yog'ayotgan edi, **shuning uchun** taksi chaqirdik.",
     "Шёл дождь, **поэ́тому** мы вы́звали такси́.",
     "`поэтому` — natija bog'lovchisi; `потому что` ning teskarisi", B),

    ("U juda charchagan **bo'lsa-da**, ishni **baribir** tugatdi.",
     "**Хотя́** он о́чень уста́л, он **всё-таки** доде́лал рабо́ту.",
     "`хотя` — zidlovchi bog'lovchi; `всё-таки` — «baribir» yuklamasi", B),

    ("Havo sovuq **bo'lganiga qaramay**, biz sayr qilgani chiqdik.",
     "**Несмотря́ на то что** бы́ло хо́лодно, мы пошли́ гуля́ть.",
     "`несмотря на то что` — zidlovchi; predlog shakli `несмотря на` + Вин. п.", B),

    ("Kvartira kichkina, **lekin buning evaziga** markazda.",
     "Кварти́ра ма́ленькая, **зато́** в це́нтре.",
     "`зато` — qoplovchi zidlovchi: kamchilik bor, lekin afzallik ham bor", B),

    ("**Agar** ertaga havo yaxshi bo'lsa, tog'ga chiqamiz.",
     "**Е́сли** за́втра бу́дет хоро́шая пого́да, мы пое́дем в го́ры.",
     "`если` — real shart; ikkala gapda ham kelasi zamon", B),

    ("**Agar** vaqtim **bo'lganida**, albatta kelardim.",
     "**Е́сли бы** у меня́ бы́ло вре́мя, я **бы** обяза́тельно пришёл.",
     "`если бы` + o'tgan zamon + `бы` — shart mayli (amalga oshmagan shart)", B),

    ("Men rus tilida ravon gapirish **uchun** har kuni shug'ullanaman.",
     "Я занима́юсь ка́ждый день, **что́бы** свобо́дно говори́ть по-ру́сски.",
     "`чтобы` + infinitiv — maqsad (ikkala gapda ega bir xil bo'lganda)", B),

    ("Men u **tushunishi uchun** sekin gapirdim.",
     "Я говори́л ме́дленно, **что́бы** он по́нял.",
     "`чтобы` + o'tgan zamon — ega boshqa bo'lganda (`по́нял`, `поймёт` emas)", B),

    ("Ishimni tugatishim **bilanoq** senga qo'ng'iroq qilaman.",
     "**Как то́лько** я зако́нчу рабо́ту, я тебе́ позвоню́.",
     "`как только` — vaqt bog'lovchisi; ikkala gapda kelasi zamon СВ", B),

    ("Men ovqat tayyorlayotgan**imda**, sen dasturxon tuz.",
     "**Пока́** я гото́влю, ты накро́й на стол.",
     "`пока` + НСВ — bir vaqtda davom etuvchi ish", B),

    ("Javob kelma**guncha** kutamiz.",
     "Мы бу́дем ждать, **пока́ не** придёт отве́т.",
     "`пока не` + СВ — chegara («-guncha»); `не` inkor emas, bog'lovchi qismi", B),

    ("Javob berish**dan oldin** yaxshilab o'ylab ko'r.",
     "**Пре́жде чем** отвеча́ть, хорошо́ поду́май.",
     "`прежде чем` + infinitiv — oldinroq bajariladigan ish", B),

    ("Men ishlayapman, **u paytda esa** u dam olyapti.",
     "Я рабо́таю, **в то вре́мя как** он отдыха́ет.",
     "`в то время как` — bir vaqtdalik va zidlanish", B),

    ("Toshkentga ko'chganim**dan beri** uni ko'rmadim.",
     "Я не ви́дел его́, **с тех пор как** перее́хал в Ташке́нт.",
     "`с тех пор как` — boshlanish nuqtasi («-dan beri»)", B),

    ("**Qancha** ko'p shug'ullansang, **shuncha** tez o'rganasan.",
     "**Чем** бо́льше ты занима́ешься, **тем** быстре́е у́чишься.",
     "`чем … тем` — qiyosiy bog'lovchi; har ikki qismda qiyosiy daraja", B),

    ("U kechikishini ayt**di**.",
     "Он сказа́л, **что** опозда́ет.",
     "`что` — tushuntiruvchi bog'lovchi; oldidan doimo vergul qo'yiladi", B),

    ("Menda **na** vaqt, **na** kuch qoldi.",
     "У меня́ не оста́лось **ни** вре́мени, **ни** сил.",
     "`ни … ни` — qo'sh inkor; fe'l oldida `не`, otlar Род. п. da", B),

    ("U **go'yo** hech narsa bo'lmagandek gapirdi.",
     "Он говори́л так, **как бу́дто** ничего́ не случи́лось.",
     "`как будто` — qiyos va shubha bog'lovchisi («go'yo»)", B),

    # ═══════════════ YUKLAMALAR (45–58) ═══════════════
    ("U **hatto** xayrlashmadi ham.",
     "Он **да́же** не попроща́лся.",
     "`даже` — kuchaytiruvchi yuklama; kutilmaganlikni ta'kidlaydi", Y),

    ("**Aynan** shuni aytmoqchi edim.",
     "**И́менно** э́то я и хоте́л сказа́ть.",
     "`именно` — aniqlovchi yuklama; bu yerdagi `и` ham kuchaytiruvchi", Y),

    ("**Axir** men senga aytgan edim-ku!",
     "Я **же** тебе́ говори́л!",
     "`же` — ta'kidlovchi yuklama; ta'kidlanayotgan so'zdan keyin turadi", Y),

    ("**Men-ku** buni bilardim, lekin indamadim.",
     "Я**-то** э́то знал, но промолча́л.",
     "`-то` — ajratuvchi yuklama, defis bilan; `кто-то` dagi `-то` dan farqli", Y),

    ("**Nahotki** u hali kelmagan bo'lsa?",
     "**Ра́зве** он ещё не пришёл?",
     "`разве` — shubha savoli; `неужели` dan yumshoqroq", Y),

    ("**Nahotki** sen buni bilmasang?",
     "**Неуже́ли** ты э́того не зна́ешь?",
     "`неужели` — hayrat savoli; `разве` ga yaqin, hissiyoti kuchliroq", Y),

    ("Menga **faqatgina** bir daqiqa kerak.",
     "Мне ну́жна **лишь** одна́ мину́та.",
     "`лишь` — cheklovchi yuklama; `только` ning kitobiyroq shakli", Y),

    ("Men **faqat** so'ramoqchi edim.",
     "Я **то́лько** хоте́л спроси́ть.",
     "`только` — cheklovchi yuklama; `как только` dagi `только` bilan adashtirmang", Y),

    ("**Mana** men nimani nazarda tutgan edim.",
     "**Вот** что я име́л в виду́.",
     "`вот` — ko'rsatuvchi yuklama; `вот что`, `вот почему` birikmalari", Y),

    ("U kelishini bil**maymiz**.",
     "Мы не зна́ем, придёт **ли** он.",
     "`ли` — bilvosita savol yuklamasi; so'roq so'zi bo'lmaganda ishlatiladi", Y),

    ("U **hali** uxlayapti, men esa **allaqachon** ishdaman.",
     "Он **ещё** спит, а я **уже́** на рабо́те.",
     "`ещё` — hali davom etmoqda; `уже` — allaqachon sodir bo'ldi", Y),

    ("Hozir bir piyola choy **ichgim kelardi**.",
     "Я **бы** сейча́с вы́пил ча́шку ча́я.",
     "`бы` + o'tgan zamon — yumshoq istak yoki taklif", Y),

    ("Bu **qiyin emas, balki** shunchaki uzoq.",
     "Э́то **не** тру́дно, **а** про́сто до́лго.",
     "`не … а` — to'g'rilovchi zidlanish («emas, balki»)", Y),

    ("Menga **birortasi** qo'ng'iroq qildimi?",
     "Мне кто́**-нибудь** звони́л?",
     "`-нибудь` — noma'lum shaxs/narsa; `-то` esa ma'lum, lekin aytilmagan", Y),

    # ═══════════════ KIRISH SO'ZLAR (59–72) ═══════════════
    ("**Mening fikrimcha**, bu yaxshi reja, **shunga qaramay** yana bir o'ylab ko'raylik.",
     "**По-мо́ему**, э́то хоро́ший план, **тем не ме́нее** дава́й ещё поду́маем.",
     "`по-моему`, `тем не менее` — kirish so'zlar, vergul bilan ajratiladi", K),

    ("**Aytgancha**, u **axir** bizni ogohlantirgan edi-ku.",
     "**Кста́ти**, он **ведь** нас предупрежда́л.",
     "`кстати` — kirish so'z (vergul bilan); `ведь` — yuklama, vergul qo'yilmaydi", K),

    ("**Afsuski**, u bugun kelishi **dargumon**.",
     "**К сожале́нию**, он **вряд ли** придёт сего́дня.",
     "`к сожалению` — kirish so'z; `вряд ли` — shubha yuklamasi, fe'l tasdiq shaklida", K),

    ("**Birinchidan**, bu qimmat, **ikkinchidan**, vaqtimiz yo'q.",
     "**Во-пе́рвых**, э́то до́рого, **во-вторы́х**, у нас нет вре́мени.",
     "`во-первых`, `во-вторых` — tartib kirish so'zlari", K),

    ("**Albatta**, men senga yordam beraman.",
     "**Коне́чно**, я тебе́ помогу́.",
     "`конечно` — ishonch kirish so'zi; talaffuzi [кане́шна]", K),

    ("**Ehtimol**, u shunchaki unutgandir.",
     "**Мо́жет быть**, он про́сто забы́л.",
     "`может быть` — taxmin; `наверное` ga yaqin, ishonch pastroq", K),

    ("U **chamasi** yo'l tirbandligida qolgan.",
     "Он, **наве́рное**, застря́л в про́бке.",
     "`наверное` — taxmin; gap o'rtasida ikki tomondan vergul bilan", K),

    ("**Demak**, biz kelishib oldik.",
     "**Зна́чит**, мы договори́лись.",
     "`значит` — xulosa kirish so'zi", K),

    ("**Menimcha**, biz noto'g'ri burilib ketdik.",
     "**Ка́жется**, мы сверну́ли не туда́.",
     "`кажется` — noaniq taxmin; `мне ка́жется` shaklida ham ishlatiladi", K),

    ("Bir nima o'ylab topaylik — **masalan**, dengizga boraylik.",
     "Дава́й что́-нибудь приду́маем — **наприме́р**, пое́дем на мо́ре.",
     "`например` — misol keltiruvchi kirish so'z", K),

    ("Men xafa bo'lmadim, **aksincha**, xursand bo'ldim.",
     "Я не оби́делся, **наоборо́т**, обра́довался.",
     "`наоборот` — teskari ma'no kiritadi", K),

    ("**Umuman olganda**, hammasi yaxshi o'tdi.",
     "**В о́бщем**, всё прошло́ хорошо́.",
     "`в общем` — umumlashtiruvchi kirish so'z («xullas»)", K),

    ("**Eng muhimi** — taslim bo'lmaslik.",
     "**Гла́вное** — не сдава́ться.",
     "`главное` — asosiyni ajratuvchi kirish so'z; tiredan keyin infinitiv", K),

    ("**Rostini aytsam**, men bunga ishonmayman.",
     "**Че́стно говоря́**, я в э́то не ве́рю.",
     "`честно говоря` — ochiqlik birikmasi; deyarli doim gap boshida", K),
]
