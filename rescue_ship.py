from flask import Flask, render_template_string, redirect, url_for, request, Response
import base64
import os

app = Flask(__name__)

# تصویر پس‌زمینه فقط برای صفحه خوش‌آمدگویی، داخل همین فایل
BACKGROUND_IMAGE = base64.b64decode("""
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
""")

LANGUAGES = {
    "fa": "فارسی",
    "en": "English",
    "ar": "العربية",
    "fr": "Français",
    "tr": "Türkçe"
}

TRANSLATIONS = {
    "fa": {
        "language": "انتخاب زبان",
        "enter": "ورود به سایت",
        "categories": "بخش‌های سایت",
        "select": "برای ورود به هر بخش کلیک کنید",
        "items": "محتویات این بخش",
        "back": "بازگشت",
        "open": "مشاهده محتوا",
        "empty": "هنوز محتوایی برای این قسمت ثبت نشده است.",
        "more": "نمایش موارد بیشتر",
        "footer": "RESCUE SHIP · BEYOND THE UNKNOWN",
        "names": [
            "پیش‌نویس",
            "توضیح در مورد تغییر فراکتال",
            "تغییر فراکتال ۱ تا ۱۴",
            "جلسات آنلاین از ۱ تا ...",
            "پرسش و پاسخ ها",
            "مراقبه های صوتی",
            "مراقبه های تصویری",
            "مراقبه های کوانتومی"
        ]
    },
    "en": {
        "language": "Language",
        "enter": "ENTER THE SITE",
        "categories": "SITE SECTIONS",
        "select": "Click on a section to explore",
        "items": "SECTION CONTENT",
        "back": "Back",
        "open": "View content",
        "empty": "No content has been added yet.",
        "more": "Show more",
        "footer": "RESCUE SHIP · BEYOND THE UNKNOWN",
        "names": [
            "Drafts",
            "Fractal Change Explanation",
            "Fractal Changes 1 to 14",
            "Online Sessions 1 to ...",
            "Questions and Answers",
            "Audio Meditations",
            "Visual Meditations",
            "Quantum Meditations"
        ]
    },
    "ar": {
        "language": "اللغة",
        "enter": "دخول الموقع",
        "categories": "أقسام الموقع",
        "select": "اضغط على القسم لاستكشافه",
        "items": "محتويات القسم",
        "back": "رجوع",
        "open": "عرض المحتوى",
        "empty": "لم تتم إضافة المحتوى بعد.",
        "more": "عرض المزيد",
        "footer": "RESCUE SHIP · BEYOND THE UNKNOWN",
        "names": [
            "المسودات",
            "شرح التغيير الكسيري",
            "التغييرات الكسرية من 1 إلى 14",
            "الجلسات عبر الإنترنت من 1 إلى ...",
            "الأسئلة والأجوبة",
            "التأملات الصوتية",
            "التأملات المرئية",
            "التأملات الكمية"
        ]
    },
    "fr": {
        "language": "Langue",
        "enter": "ENTRER SUR LE SITE",
        "categories": "SECTIONS DU SITE",
        "select": "Cliquez sur une section",
        "items": "CONTENU DE LA SECTION",
        "back": "Retour",
        "open": "Voir le contenu",
        "empty": "Aucun contenu n'a encore été ajouté.",
        "more": "Afficher plus",
        "footer": "RESCUE SHIP · BEYOND THE UNKNOWN",
        "names": [
            "Brouillons",
            "Explication du changement fractal",
            "Changements fractals de 1 à 14",
            "Sessions en ligne de 1 à ...",
            "Questions et réponses",
            "Méditations audio",
            "Méditations visuelles",
            "Méditations quantiques"
        ]
    },
    "tr": {
        "language": "Dil",
        "enter": "SİTEYE GİR",
        "categories": "SİTE BÖLÜMLERİ",
        "select": "Keşfetmek için bir bölüm seçin",
        "items": "BÖLÜM İÇERİĞİ",
        "back": "Geri",
        "open": "İçeriği görüntüle",
        "empty": "Henüz içerik eklenmedi.",
        "more": "Daha fazla göster",
        "footer": "RESCUE SHIP · BEYOND THE UNKNOWN",
        "names": [
            "Taslaklar",
            "Fraktal Değişimin Açıklaması",
            "1'den 14'e Fraktal Değişimleri",
            "1'den İtibaren Çevrimiçi Oturumlar",
            "Sorular ve Cevaplar",
            "Sesli Meditasyonlar",
            "Görsel Meditasyonlar",
            "Kuantum Meditasyonları"
        ]
    }
}

CATEGORIES = [
    ("draft", "✧", 12),
    ("fractal_info", "◇", 1),
    ("fractal", "◈", 14),
    ("sessions", "◎", 20),
    ("qa", "❖", 20),
    ("audio", "♫", 12),
    ("visual", "▣", 12),
    ("quantum", "✺", 12)
]

ITEM_NAMES = {
    "fa": [
        "پیش‌نویس", "توضیح تغییر فراکتال", "تغییر فراکتال",
        "جلسه آنلاین", "پرسش و پاسخ", "مراقبه صوتی",
        "مراقبه تصویری", "مراقبه کوانتومی"
    ],
    "en": [
        "Draft", "Fractal Change Explanation", "Fractal Change",
        "Online Session", "Question and Answer", "Audio Meditation",
        "Visual Meditation", "Quantum Meditation"
    ],
    "ar": [
        "مسودة", "شرح التغيير الكسيري", "التغيير الكسيري",
        "جلسة عبر الإنترنت", "سؤال وجواب", "تأمل صوتي",
        "تأمل مرئي", "تأمل كمي"
    ],
    "fr": [
        "Brouillon", "Explication fractale", "Changement fractal",
        "Session en ligne", "Question et réponse", "Méditation audio",
        "Méditation visuelle", "Méditation quantique"
    ],
    "tr": [
        "Taslak", "Fraktal Değişim Açıklaması", "Fraktal Değişim",
        "Çevrimiçi Oturum", "Soru ve Cevap", "Sesli Meditasyon",
        "Görsel Meditasyon", "Kuantum Meditasyonu"
    ]
}


def valid_lang(lang):
    return lang if lang in LANGUAGES else "fa"


def get_category(cat_id):
    for index, cat in enumerate(CATEGORIES):
        if cat[0] == cat_id:
            return cat, index
    return None, None


def get_items(cat_id, lang, count=20):
    category, index = get_category(cat_id)

    if category is None:
        return []

    total = category[2]

    if cat_id == "sessions":
        total = max(20, count)

    base_name = ITEM_NAMES[lang][index]

    return [
        {
            "index": i,
            "title": base_name if cat_id == "fractal_info"
                     else f"{base_name} {i}"
        }
        for i in range(1, total + 1)
    ]


HTML = r"""
<!DOCTYPE html>
<html lang="{{ lang }}"
dir="{{ 'rtl' if lang in ['fa','ar'] else 'ltr' }}">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RESCUE SHIP</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;700;900&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    background:
        radial-gradient(ellipse at 50% 40%, #35205b 0%, transparent 55%),
        linear-gradient(135deg, #090713, #160d29, #090713);
    color: white;
    font-family: 'Vazirmatn', sans-serif;
    overflow-x: hidden;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
        radial-gradient(2px 2px at 20% 30%, #d6baff, transparent),
        radial-gradient(2px 2px at 70% 20%, white, transparent),
        radial-gradient(2px 2px at 40% 80%, #d9b45b, transparent),
        radial-gradient(2px 2px at 90% 70%, white, transparent);
    background-size: 230px 230px;
    opacity: .5;
    z-index: 0;
}

/* تصویر سفینه فقط در پس‌زمینه صفحه فهرست‌ها */
/* ستاره‌های چشمک‌زن فقط در صفحه ورود */
.welcome-stars {
    position: fixed;
    inset: 0;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}

.welcome-stars i {
    position: absolute;
    display: block;
    width: var(--star-size, 2px);
    height: var(--star-size, 2px);
    border-radius: 50%;
    background: var(--star-color, #e8d39b);
    box-shadow: 0 0 5px 1px var(--star-color, #e8d39b),
                0 0 12px 2px var(--star-color, #e8d39b);
    opacity: .2;
    animation: starTwinkle var(--twinkle-time, 3s) ease-in-out var(--twinkle-delay, 0s) infinite;
    will-change: opacity, transform;
}

@keyframes starTwinkle {
    0%, 100% { opacity: .18; transform: scale(.65); filter: brightness(.75); }
    45% { opacity: 1; transform: scale(1.35); filter: brightness(1.7); }
    65% { opacity: .45; transform: scale(.9); filter: brightness(1); }
}

body.dashboard-page::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background-image:
        linear-gradient(rgba(8, 5, 22, .48), rgba(8, 5, 22, .48)),
        url("/welcome-background.jpg");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
    opacity: .55;
}

/* ارتباط با استاد - فقط صفحه خوش‌آمدگویی */
.welcome-contact {
    position: fixed;
    top: 22px;
    left: 24px;
    z-index: 150;
    direction: rtl;
    text-align: right;
    padding: 11px 15px;
    border: 1px solid rgba(231,196,119,.55);
    border-radius: 12px;
    background: rgba(12,8,25,.72);
    backdrop-filter: blur(10px);
    box-shadow: 0 0 18px rgba(190,150,255,.12);
}
.welcome-contact-title {
    color: #f0d99c;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 5px;
}
.welcome-contact a {
    color: #d6baff;
    font-size: 13px;
    text-decoration: none;
    direction: ltr;
    display: inline-block;
    transition: color .2s, text-shadow .2s;
}
.welcome-contact a:hover {
    color: #fff;
    text-shadow: 0 0 10px #b98cff;
}
@media (max-width: 600px) {
    .welcome-contact { top: 12px; left: 12px; padding: 8px 10px; }
    .welcome-contact-title { font-size: 12px; }
    .welcome-contact a { font-size: 11px; }
}

/* HEADER */

header {
    position: relative;
    z-index: 100;
    min-height: 82px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    direction: ltr !important;
    padding: 12px 6%;
    border-bottom: 1px solid #d2af642e;
    background: rgba(10,7,20,.75);
    backdrop-filter: blur(15px);
}

.logo {
    direction: ltr !important;
    color: #e7c477;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 3px;
    text-decoration: none;
    text-shadow: 0 0 20px #e1b96455;
}

/* FIXED LANGUAGE MENU */

.language {
    position: fixed !important;
    top: 14px !important;
    right: 20px !important;
    left: auto !important;
    z-index: 99999 !important;
    direction: ltr !important;
    text-align: right;
}

.lang-btn {
    background: linear-gradient(135deg,#30204c,#171020);
    border: 1px solid #b99a57;
    color: #f1d99e;
    padding: 11px 20px;
    border-radius: 9px;
    cursor: pointer;
    font-family: inherit;
    white-space: nowrap;
    box-shadow: 0 5px 20px #0005;
}

.lang-btn:hover {
    box-shadow: 0 0 20px #d5b76b66;
    background: #44305e;
}

.dropdown {
    position: absolute !important;
    top: 50px !important;
    right: 0 !important;
    left: auto !important;
    width: 170px;
    background: #170f27;
    border: 1px solid #b99a57;
    border-radius: 12px;
    overflow: hidden;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: .3s;
    box-shadow: 0 10px 35px #0009;
    text-align: right;
    direction: ltr !important;
}

.dropdown.show {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.dropdown a {
    display: block;
    padding: 12px 17px;
    color: #ddd2ef;
    text-decoration: none;
    transition: .2s;
    text-align: right;
}

.dropdown a:hover {
    background: #493267;
    color: #f3d58b;
}

/* MAIN */

main {
    position: relative;
    z-index: 1;
    width: 100%;
    min-height: calc(100vh - 82px);
    padding: 55px 7% 100px;
    animation: appear .6s ease;
}

.center {
    min-height: calc(100vh - 200px);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.welcome {
    max-width: 850px;
    width: 100%;
}

.welcome h1 {
    margin-bottom: 12px;
}

.persian-title {
    color: #f0d99c;
    font-size: clamp(23px, 4vw, 36px);
    font-weight: 700;
    margin: 0 0 34px;
    text-shadow: 0 0 18px rgba(218, 184, 111, .42);
}

.welcome-header,
.welcome-footer {
    display: none !important;
}

.symbol {
    width: 115px;
    height: 115px;
    border: 1px solid #c4a45f;
    border-radius: 50%;
    margin: 0 auto 35px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    color: #e3c276;
    box-shadow: 0 0 35px #a17bd044;
    animation: floating 4s infinite;
}

h1 {
    font-size: clamp(35px, 7vw, 75px);
    font-weight: 900;
    letter-spacing: 4px;
    background: linear-gradient(120deg,#fff,#d7b765,#c7c5d3,#f4df9e);
    -webkit-background-clip: text;
    color: transparent;
}

.subtitle {
    color: #c9a8f1;
    letter-spacing: 4px;
    margin-top: 18px;
    font-size: 13px;
}

.line {
    width: 110px;
    height: 2px;
    background: linear-gradient(90deg,transparent,#d7b765,transparent);
    margin: 30px auto;
}

.description {
    color: #c9c1d8;
    font-size: 17px;
    margin-bottom: 35px;
}

.gold-btn {
    display: inline-block;
    padding: 15px 38px;
    background: linear-gradient(120deg,#a98745,#e5cd8a,#a98745);
    color: #170e25;
    border: none;
    border-radius: 7px;
    text-decoration: none;
    font-family: inherit;
    font-weight: 900;
    cursor: pointer;
    transition: .3s;
    box-shadow: 0 0 25px #c7a45c33;
}

.gold-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 35px #d5b76b77;
}

.page-title {
    text-align: center;
    margin: 10px 0 12px;
    font-size: clamp(25px, 4vw, 42px);
    color: #e8ce91;
    font-weight: 900;
}

.page-subtitle {
    text-align: center;
    color: #b9a9d0;
    margin-bottom: 45px;
    font-size: 14px;
}

/* CARDS */

.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
    max-width: 1050px;
    margin: auto;
}

.card {
    min-height: 150px;
    background: linear-gradient(145deg,rgba(67,43,96,.55),rgba(20,14,35,.88));
    border: 1px solid rgba(196,164,95,.35);
    border-radius: 15px;
    text-decoration: none;
    color: white;
    padding: 22px;
    display: flex;
    align-items: center;
    gap: 18px;
    transition: .3s;
    position: relative;
    overflow: hidden;
    animation: cardIn .5s both;
}

.card:hover {
    transform: translateY(-5px);
    border-color: #e0bf72;
    box-shadow: 0 10px 35px #0005, 0 0 20px #c7a45c22;
    background: linear-gradient(145deg,#50336d,#211532);
}

.card-icon {
    width: 60px;
    height: 60px;
    min-width: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #b99a57;
    border-radius: 13px;
    color: #e7c477;
    font-size: 29px;
    background: #bd9c4a12;
}

.card-text {
    position: relative;
    z-index: 1;
    text-align: start;
}

.card-text h3 {
    font-size: 15px;
    line-height: 1.9;
    color: #f1e8fa;
}

.card-text p {
    color: #b9a7ce;
    font-size: 12px;
    margin-top: 5px;
}

.arrow {
    margin-inline-start: auto;
    color: #d6b66d;
    font-size: 23px;
}

/* دکمه بازگشت به صفحه خوش‌آمدگویی، فقط در صفحه فهرست‌ها */
.dashboard-home-btn {
    position: absolute;
    top: 98px;
    left: 24px;
    z-index: 120;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 15px;
    color: #e5ca8c;
    text-decoration: none;
    border: 1px solid #9f844c;
    border-radius: 8px;
    background: rgba(18, 12, 31, .82);
    backdrop-filter: blur(8px);
    font-size: 13px;
    transition: .3s;
}
.dashboard-home-btn:hover {
    background: #493267;
    box-shadow: 0 0 16px rgba(214,182,109,.2);
}
@media(max-width:650px) {
    .dashboard-home-btn { top: 90px; left: 12px; padding: 8px 11px; font-size: 11px; }
}

/* بهینه‌سازی نمایش و جابه‌جایی صفحات در گوشی */
@media (max-width: 768px) {
    main { animation: none; }
    .card { animation: none; transition: border-color .15s, background-color .15s; }
    header, .welcome-contact, .dashboard-home-btn { backdrop-filter: none; -webkit-backdrop-filter: none; }
    .card:hover, .gold-btn:hover { transform: none; }
    body.dashboard-page::after { background-size: cover; }
}

.back-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    color: #e5ca8c;
    border: 1px solid #9f844c;
    border-radius: 8px;
    padding: 9px 18px;
    margin-bottom: 30px;
    transition: .3s;
    font-size: 13px;
}

.back-btn:hover {
    background: #493267;
}

.detail-box {
    max-width: 800px;
    min-height: 300px;
    margin: 40px auto;
    padding: 45px 25px;
    border: 1px solid #b99a57;
    background: linear-gradient(145deg,#33204d,#140e23);
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 15px 50px #0005;
}

.detail-icon {
    font-size: 48px;
    color: #e7c477;
    margin-bottom: 20px;
}

.detail-box h2 {
    color: #e7c477;
    margin-bottom: 25px;
    font-size: 25px;
}

.detail-content {
    padding: 25px;
    background: #ffffff08;
    border: 1px solid #ffffff12;
    border-radius: 12px;
    color: #d0c3e1;
    line-height: 2.2;
}

.more-box {
    text-align: center;
    margin: 35px auto;
}

footer {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 20px;
    color: #776b8c;
    font-size: 11px;
    letter-spacing: 2px;
}

@keyframes floating {
    0%,100% {transform:translateY(0);}
    50% {transform:translateY(-12px);}
}

@keyframes appear {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

@keyframes cardIn {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

@media(max-width:650px) {
    header {padding:12px 4%;}
    .logo {font-size:16px; letter-spacing:1px;}
    .language {right:12px !important; top:12px !important;}
    .lang-btn {padding:9px 12px;}
    main {padding:35px 5% 70px;}
    .grid {gap:12px;}
    .card {
        min-height:145px;
        padding:13px;
        gap:10px;
        flex-direction:column;
        text-align:center;
    }
    .card-icon {
        width:48px;
        height:48px;
        min-width:48px;
        font-size:23px;
    }
    .card-text {text-align:center;}
    .card-text h3 {font-size:12px;}
    .card-text p {font-size:10px;}
    .arrow {display:none;}
}

</style>
</head>

<body class="{{ 'dashboard-page' if page == 'dashboard' else ('welcome-page' if page == 'welcome' else '') }}">

{% if page == 'welcome' %}
<div class="welcome-stars" aria-hidden="true"></div>
<div class="welcome-contact">
    <div class="welcome-contact-title">ارتباط با استاد</div>
    <a href="https://t.me/Adachaeichei" target="_blank" rel="noopener noreferrer">@Adachaeichei</a>
</div>
{% endif %}

<header class="{{ 'welcome-header' if page == 'welcome' else '' }}">
    <a class="logo" href="{{ url_for('home', lang=lang) }}">
        RESCUE SHIP
    </a>
</header>

<!-- زبان خارج از هدر و مستقل از RTL/LTR -->
<div class="language">

    <button class="lang-btn" onclick="toggleMenu()">
        ☰ {{ t.language }} ▾
    </button>

    <div class="dropdown" id="dropdown">
        {% for code, name in languages.items() %}
            <a href="{{ url_for('change_language',
                lang=code,
                page=page,
                cat=cat_id,
                item=item_index,
                count=count) }}">
                {{ name }}
            </a>
        {% endfor %}
    </div>

</div>

<main>

{% if page == "welcome" %}

    <div class="center">
        <div class="welcome">
            <h1>RESCUE SHIP</h1>
            <div class="persian-title">کشتی نجات</div>

            <a href="{{ url_for('dashboard', lang=lang) }}" class="gold-btn">
                {{ t.enter }}
            </a>
        </div>
    </div>

{% elif page == "dashboard" %}

    <a class="dashboard-home-btn" href="{{ url_for('home', lang=lang) }}">
        ← {{ t.back }}
    </a>

    <h1 class="page-title">{{ t.categories }}</h1>
    <p class="page-subtitle">{{ t.select }}</p>

    <div class="grid">

        {% for c in categories %}
        <a class="card" href="{{ url_for('category_page', lang=lang, cat_id=c[0]) }}">

            <div class="card-icon">{{ c[1] }}</div>

            <div class="card-text">
                <h3>{{ t.names[loop.index0] }}</h3>
                <p>{{ c[2] }}</p>
            </div>

            <div class="arrow">‹</div>
        </a>
        {% endfor %}

    </div>

{% elif page == "category" %}

    <a class="back-btn" href="{{ url_for('dashboard', lang=lang) }}">
        ← {{ t.back }}
    </a>

    <h1 class="page-title">{{ t.names[category_index] }}</h1>
    <p class="page-subtitle">{{ t.items }}</p>

    <div class="grid">

        {% for item in items %}
        <a class="card" href="{{ url_for('item_page', lang=lang, cat_id=cat_id, item_index=item.index) }}">

            <div class="card-icon">{{ category[1] }}</div>

            <div class="card-text">
                <h3>{{ item.title }}</h3>
                <p>{{ t.open }}</p>
            </div>

            <div class="arrow">‹</div>

        </a>
        {% endfor %}

    </div>

    {% if cat_id == 'sessions' %}
    <div class="more-box">
        <a class="gold-btn"
           href="{{ url_for('category_page', lang=lang, cat_id=cat_id, count=count+20) }}">
            {{ t.more }} +
        </a>
    </div>
    {% endif %}

{% elif page == "detail" %}

    <a class="back-btn"
       href="{{ url_for('category_page', lang=lang, cat_id=cat_id) }}">
        ← {{ t.back }}
    </a>

    <div class="detail-box">
        <div class="detail-icon">{{ category[1] }}</div>
        <h2>{{ item.title }}</h2>
        <div class="line"></div>

        <div class="detail-content">
            {{ t.empty }}
        </div>
    </div>

{% endif %}

</main>

<footer class="{{ 'welcome-footer' if page == 'welcome' else '' }}">{{ t.footer }}</footer>

<script>
function toggleMenu() {
    document.getElementById("dropdown").classList.toggle("show");
}

document.addEventListener("click", function(e) {
    if (!e.target.closest(".language")) {
        document.getElementById("dropdown").classList.remove("show");
    }
});

// پیش‌بارگذاری مقصد لینک‌های داخلی هنگام لمس/کلیک؛ تا صفحه بعد زودتر آماده شود.
(() => {
    const prefetched = new Set();
    function prefetchInternalLink(event) {
        const link = event.target.closest('a[href]');
        if (!link || link.target === '_blank' || link.hasAttribute('download')) return;
        const url = new URL(link.href, window.location.href);
        if (url.origin !== window.location.origin || prefetched.has(url.href)) return;
        prefetched.add(url.href);
        const hint = document.createElement('link');
        hint.rel = 'prefetch';
        hint.href = url.href;
        document.head.appendChild(hint);
    }
    document.addEventListener('pointerover', prefetchInternalLink, {passive: true});
    document.addEventListener('touchstart', prefetchInternalLink, {passive: true});
    document.addEventListener('pointerdown', prefetchInternalLink, {passive: true});
})();
</script>

<script>
// ستاره‌ها فقط در صفحه خوش‌آمدگویی ساخته می‌شوند و رنگ و زمان چشمک‌زدنشان تصادفی است.
(() => {
    const layer = document.querySelector('.welcome-stars');
    if (!layer) return;

    const colors = ['#f3d27c', '#bd91ff', '#e8e8f2']; // طلایی، بنفش، نقره‌ای
    for (let i = 0; i < 78; i++) {
        const star = document.createElement('i');
        const color = colors[Math.floor(Math.random() * colors.length)];
        const size = (Math.random() * 2.1 + 1).toFixed(2);
        const duration = (2.1 + Math.random() * 4.8).toFixed(2);
        const delay = (-Math.random() * 6).toFixed(2);

        star.style.left = (Math.random() * 100).toFixed(2) + '%';
        star.style.top = (Math.random() * 100).toFixed(2) + '%';
        star.style.setProperty('--star-color', color);
        star.style.setProperty('--star-size', size + 'px');
        star.style.setProperty('--twinkle-time', duration + 's');
        star.style.setProperty('--twinkle-delay', delay + 's');
        layer.appendChild(star);
    }
})();
</script>

</body>
</html>
"""


@app.route("/welcome-background.jpg")
def welcome_background():
    return Response(BACKGROUND_IMAGE, mimetype="image/jpeg", headers={"Cache-Control": "public, max-age=86400"})


@app.route("/")
def root():
    return redirect(url_for("home", lang="fa"))


@app.route("/<lang>")
def home(lang):
    lang = valid_lang(lang)

    return render_template_string(
        HTML,
        lang=lang,
        t=TRANSLATIONS[lang],
        languages=LANGUAGES,
        page="welcome",
        cat_id="",
        item_index=1,
        count=20
    )


@app.route("/<lang>/site")
def dashboard(lang):
    lang = valid_lang(lang)

    return render_template_string(
        HTML,
        lang=lang,
        t=TRANSLATIONS[lang],
        languages=LANGUAGES,
        page="dashboard",
        categories=CATEGORIES,
        cat_id="",
        item_index=1,
        count=20
    )


@app.route("/<lang>/category/<cat_id>")
def category_page(lang, cat_id):
    lang = valid_lang(lang)

    category, category_index = get_category(cat_id)

    if category is None:
        return redirect(url_for("dashboard", lang=lang))

    count = request.args.get("count", 20, type=int)
    count = max(20, min(count, 500))

    return render_template_string(
        HTML,
        lang=lang,
        t=TRANSLATIONS[lang],
        languages=LANGUAGES,
        page="category",
        categories=CATEGORIES,
        category=category,
        category_index=category_index,
        cat_id=cat_id,
        items=get_items(cat_id, lang, count),
        item_index=1,
        count=count
    )


@app.route("/<lang>/item/<cat_id>/<int:item_index>")
def item_page(lang, cat_id, item_index):
    lang = valid_lang(lang)

    category, category_index = get_category(cat_id)

    if category is None or item_index < 1:
        return redirect(url_for("dashboard", lang=lang))

    items = get_items(cat_id, lang, max(20, item_index))

    if item_index > len(items):
        return redirect(url_for("category_page", lang=lang, cat_id=cat_id))

    return render_template_string(
        HTML,
        lang=lang,
        t=TRANSLATIONS[lang],
        languages=LANGUAGES,
        page="detail",
        category=category,
        category_index=category_index,
        cat_id=cat_id,
        item=items[item_index - 1],
        item_index=item_index,
        count=20
    )


@app.route("/change-language/<lang>")
def change_language(lang):
    lang = valid_lang(lang)

    page = request.args.get("page", "welcome")
    cat = request.args.get("cat", "")
    item = request.args.get("item", "1", type=int)
    count = request.args.get("count", "20", type=int)

    if page == "dashboard":
        return redirect(url_for("dashboard", lang=lang))

    category, _ = get_category(cat)

    if page == "category" and category:
        return redirect(url_for(
            "category_page",
            lang=lang,
            cat_id=cat,
            count=count
        ))

    if page == "detail" and category and item >= 1:
        return redirect(url_for(
            "item_page",
            lang=lang,
            cat_id=cat,
            item_index=item
        ))

    return redirect(url_for("home", lang=lang))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5055)), debug=False)

