"""Builds the whole site into ./site. Netlify runs this on every push (see netlify.toml)."""
import re, json, os, shutil, sys, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from cases import CASES
from tools_reg import TOOLS
from content import ARTICLES
from drawer import drawer, BTN

S = os.path.join(ROOT, 'site'); D = 'https://ibrahem-mediabuyer.com'
TODAY = datetime.date.today().isoformat()   # used for sitemap lastmod
CASES_UPDATED = '2026-10-16'                 # change when you edit a case study
WA = 'https://wa.me/966530570632'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..800&family=Schibsted+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">'

# static files (images, icons, css, /admin) are copied as they are
shutil.rmtree(S, ignore_errors=True)
shutil.copytree(os.path.join(ROOT, 'static'), S)

src = open(os.path.join(ROOT, 'src', 'home.html'), encoding='utf-8').read()
src = re.sub(r'img/([\w-]+)\.jpg', r'img/\1.webp', src)

def arts(lang):
    return [a for a in ARTICLES if lang in a]

# ---------- schema ----------
PERSON = {"@type": "Person", "@id": D + "/#person", "name": "Ibrahem Muhamed", "alternateName": ["Rio", "إبراهيم محمد"],
          "jobTitle": "Senior Performance Marketing & Media Buying Specialist", "url": D + "/", "image": D + "/assets/icon-512.png",
          "email": "mailto:ibrahem.work11@gmail.com", "telephone": "+966530570632",
          "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
          "sameAs": ["https://www.linkedin.com/in/r1io1"],
          "knowsAbout": ["Media buying", "Performance marketing", "Snapchat Ads", "TikTok Ads", "Meta Ads", "Google Ads",
                         "E-commerce marketing", "Salla", "Shopify", "ROAS", "MER", "Conversion tracking", "GA4", "Google Tag Manager"],
          "knowsLanguage": ["ar", "en"]}
WEBSITE = {"@type": "WebSite", "@id": D + "/#website", "url": D + "/", "name": "Ibrahem Muhamed", "alternateName": ["إبراهيم محمد", "Ibrahem Media Buyer"],
           "inLanguage": ["en", "ar"], "publisher": {"@id": D + "/#person"}}
SERVICE = {"@type": "ProfessionalService", "@id": D + "/#service", "name": "Ibrahem Muhamed — Media Buying & Performance Marketing",
           "url": D + "/", "logo": D + "/assets/icon-512.png", "image": D + "/og.jpg", "founder": {"@id": D + "/#person"},
           "telephone": "+966530570632", "email": "ibrahem.work11@gmail.com",
           "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
           "areaServed": [{"@type": "Country", "name": "Saudi Arabia"}, {"@type": "Place", "name": "GCC"}, {"@type": "Country", "name": "Egypt"}],
           "serviceType": ["Media buying", "Paid social advertising", "Google Ads management", "Conversion tracking setup", "Ad account audit"],
           "sameAs": ["https://www.linkedin.com/in/r1io1"],
           "offers": {"@type": "Offer", "name": "Free 25-minute ad account audit", "price": "0", "priceCurrency": "SAR"}}
AUTHOR = {"@type": "Person", "@id": D + "/#person", "name": "Ibrahem Muhamed", "url": D + "/"}

def ld(*objs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(objs)}, ensure_ascii=False) + '</script>'

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": D + u} for i, (n, u) in enumerate(items)]}

def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def head(lang, path, title, desc, alts, og_type='website', extra=''):
    ar = lang == 'ar'
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{D}{u}">' for l, u in alts)
    if alts and any(l == 'en' for l, _ in alts):
        alt += f'<link rel="alternate" hreflang="x-default" href="{D}{dict(alts)["en"]}">'
    return f'''<!doctype html>
<html lang="{lang}" dir="{'rtl' if ar else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Ibrahem Muhamed">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#07080c">
<link rel="canonical" href="{D}{path}">
{alt}
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Ibrahem Muhamed">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{D}{path}">
<meta property="og:image" content="{D}/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{'ar_SA' if ar else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{D}/og.jpg">
{extra}
'''

# ---------- sub-page shell ----------
UI = {
 'en': {'home': '/', 'cases': 'Cases', 'tool': 'Free tools', 'guides': 'Guides', 'audit': 'Free audit',
        'band_h': 'Want numbers like these for your brand?', 'band_p': 'Book a free 25-minute account audit. I look at your tracking, your structure and your numbers, and tell you the first three things I would fix.',
        'band_b': 'Book the free audit', 'band_b2': 'See the full portfolio', 'res': 'Resources', 'all': 'All resources',
        'wa': "Hi Ibrahem, I'd like to book the free 25-minute account audit for my brand.", 'foot': 'Media buying for Saudi and GCC brands · Riyadh',
        'read': 'min read', 'by': 'By Ibrahem Muhamed', 'upd': 'Updated'},
 'ar': {'home': '/ar/', 'cases': 'دراسات الحالة', 'tool': 'الأدوات المجانية', 'guides': 'المقالات', 'audit': 'استشارة مجانية',
        'band_h': 'تريد أرقامًا مثل هذه لعلامتك التجارية؟', 'band_p': 'احجز مراجعة مجانية لحسابك الإعلاني مدتها 25 دقيقة. أراجع التتبع وهيكلة الحملات والأرقام، وأخبرك بأول ثلاثة أشياء سأصلحها.',
        'band_b': 'احجز المراجعة المجانية', 'band_b2': 'شاهد البورتفوليو كاملًا', 'res': 'المصادر', 'all': 'كل المصادر',
        'wa': 'مرحبًا إبراهيم، أرغب في حجز الاستشارة المجانية (25 دقيقة) لحساب علامتي التجارية.', 'foot': 'شراء إعلانات للعلامات السعودية والخليجية · الرياض',
        'read': 'دقائق قراءة', 'by': 'بقلم إبراهيم محمد', 'upd': 'آخر تحديث'},
}

def wa(lang, msg=None):
    from urllib.parse import quote
    return WA + '?text=' + quote(msg or UI[lang]['wa'])

def shell(lang, path, title, desc, alts, main, schema, cur=None, og_type='article', lang_link=None):
    u = UI[lang]; ar = lang == 'ar'
    res = '/ar/resources/' if ar else '/resources/'
    tool = res + '#tools'
    nav = (f'<a href="{res}#cases"{" aria-current=page" if cur=="cases" else ""}>{u["cases"]}</a>'
           f'<a href="{tool}"{" aria-current=page" if cur=="tool" else ""}>{u["tool"]}</a>'
           f'<a href="{res}#articles"{" aria-current=page" if cur=="guides" else ""}>{u["guides"]}</a>')
    if lang_link is None:
        lang_link = dict(alts).get('en' if ar else 'ar', '/' if ar else '/ar/')
    lang_lab = 'EN' if ar else 'ع'
    return head(lang, path, title, desc, alts, og_type, FONTS + '<link rel="stylesheet" href="/assets/site.css">' + ld(*schema)) + f'''</head>
<body>
<header class="sh"><div class="w">
  {BTN[lang]}
  <a class="logo" href="{u['home']}"><img src="/assets/logo.svg" alt="" width="30" height="30"><span>Ibrahem Muhamed</span></a>
  <nav aria-label="Main">{nav}</nav>
  <a class="lang" href="{lang_link}" hreflang="{'en' if ar else 'ar'}">{lang_lab}</a>
  <a class="btn primary small" href="{wa(lang)}" target="_blank" rel="noopener">{u['audit']}</a>
</div></header>
<main>{main}</main>
<section class="band"><div class="w">
  <div><h2>{u['band_h']}</h2><p>{u['band_p']}</p></div>
  <div class="acts"><a class="btn primary" href="{wa(lang)}" target="_blank" rel="noopener">{u['band_b']} {'←' if ar else '→'}</a><a class="btn" href="{u['home']}">{u['band_b2']}</a></div>
</div></section>
<footer class="sf"><div class="w">
  <span>© 2026 Ibrahem Muhamed · {u['foot']}</span>
  <nav><a href="{u['home']}">{'الرئيسية' if ar else 'Home'}</a><a href="{res}">{u['res']}</a><a href="https://www.linkedin.com/in/r1io1" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:ibrahem.work11@gmail.com">Email</a></nav>
</div></footer>
{drawer([lang], {lang: path}, {lang: wa(lang)}, {lang: lang_link}, {lang: 'right' if ar else 'left'})}
</body>
</html>
'''

def write(path, html):
    fp = S + path + ('index.html' if path.endswith('/') else '')
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w').write(html)

SITEMAP = []  # (path, alts)

def crumbs_html(items):
    return '<nav class="crumbs w" aria-label="Breadcrumb">' + ' <span>/</span> '.join(
        (f'<a href="{u}">{n}</a>' if i < len(items) - 1 else f'<span aria-current="page">{n}</span>') for i, (n, u) in enumerate(items)) + '</nav>'

# ---------- case pages ----------
for i, c in enumerate(CASES):
    alts = [('en', f'/cases/{c["slug"]}/'), ('ar', f'/ar/cases/{c["slug"]}/')]
    for lang in ['en', 'ar']:
        t = c[lang]; ar = lang == 'ar'; path = dict(alts)[lang]
        home = UI[lang]['home']; res = '/ar/resources/' if ar else '/resources/'
        cr = [('الرئيسية' if ar else 'Home', home), (UI[lang]['cases'], res + '#cases'), (t['title'][:48] + ('…' if len(t['title']) > 48 else ''), path)]
        nxt = CASES[(i + 1) % len(CASES)]
        main = (crumbs_html(cr) +
                f'<div class="w"><header class="ph"><span class="label">{t["kicker"]}</span><h1>{t["title"]}</h1><p class="lead">{t["lead"]}</p>'
                f'<p class="meta-line"><span>{UI[lang]["by"]}</span><span>{UI[lang]["upd"]} <bdi>{CASES_UPDATED}</bdi></span></p></header>'
                + t['body']() +
                f'<div class="next narrow"><a href="{res}#cases">{"→ " if ar else "← "}{UI[lang]["cases"]}</a>'
                f'<a href="{("/ar" if ar else "")}/cases/{nxt["slug"]}/">{nxt[lang]["title"][:60]}… {"←" if ar else "→"}</a></div></div>')
        first_img = re.search(r'/img/[\w-]+\.webp', t['body']()).group(0)
        schema = [{"@type": "Article", "headline": t['title'], "description": t['desc'], "inLanguage": lang, "datePublished": CASES_UPDATED, "dateModified": CASES_UPDATED,
                   "author": AUTHOR, "publisher": AUTHOR, "image": D + first_img,
                   "mainEntityOfPage": D + path, "about": ["Media buying", "Performance marketing", "Case study"]},
                  crumbs_ld(cr)]
        write(path, shell(lang, path, t['meta_title'], t['desc'], alts, main, schema, cur='cases'))
    SITEMAP.append(alts)

# ---------- tool pages ----------
for tl in TOOLS:
    alts = [('en', f'/tools/{tl["slug"]}/'), ('ar', f'/ar/tools/{tl["slug"]}/')]
    for lang in ['en', 'ar']:
        t = tl['T'][lang]; ar = lang == 'ar'; path = dict(alts)[lang]
        res = '/ar/resources/' if ar else '/resources/'
        cr = [('الرئيسية' if ar else 'Home', UI[lang]['home']), (UI[lang]['tool'], res + '#tools'), (t['title'], path)]
        others = [o for o in TOOLS if o is not tl]
        more = '<div class="cards" style="grid-template-columns:repeat(2,minmax(0,1fr))">' + ''.join(
            f'<a class="card" href="{("/ar" if ar else "")}/tools/{o["slug"]}/"><span class="k">{o["T"][lang]["kicker"]}</span><h3>{o["T"][lang]["title"]}</h3><p>{o["T"][lang]["card"]}</p></a>' for o in others) + '</div>'
        main = (crumbs_html(cr) + f'<div class="w"><header class="ph"><span class="label">{t["kicker"]}</span><h1>{t["title"]}</h1><p class="lead">{t["lead"]}</p></header>'
                + tl['body'](lang) + f'<div class="hub-sec narrow"><h2>{"أدوات أخرى" if ar else "More free tools"}</h2>{more}</div></div>')
        schema = [{"@type": "WebApplication", "name": t['title'], "description": t['desc'], "url": D + path, "inLanguage": lang,
                   "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "isAccessibleForFree": True,
                   "offers": {"@type": "Offer", "price": "0", "priceCurrency": "SAR"}, "author": AUTHOR},
                  faq_ld(t['faq']), crumbs_ld(cr)]
        write(path, shell(lang, path, t['meta_title'], t['desc'], alts, main, schema, cur='tool', og_type='website'))
    SITEMAP.append(alts)

# ---------- articles (EN + AR) ----------
for i, a in enumerate(ARTICLES):
    alts = [(l, (('/ar' if l == 'ar' else '') + f'/articles/{a["slug"]}/')) for l in ['en', 'ar'] if l in a]
    for lang in [l for l, _ in alts]:
        ar = lang == 'ar'; t = a[lang]; path = dict(alts)[lang]; pre = '/ar' if ar else ''
        res = pre + '/resources/'
        cr = [('الرئيسية' if ar else 'Home', UI[lang]['home']), (UI[lang]['guides'], res + '#articles'), (t['title'][:44] + '…', path)]
        faq = ''.join(f'<details><summary>{q}</summary><p>{x}</p></details>' for q, x in t['faq'])
        others = [o for o in arts(lang) if o is not a][:4]
        kk = 'مقال' if ar else 'Guide'
        more = '<div class="cards" style="grid-template-columns:repeat(2,minmax(0,1fr))">' + ''.join(
            f'<a class="card" href="{pre}/articles/{o["slug"]}/"><span class="k">{kk}</span><h3>{o[lang]["title"]}</h3><p>{o[lang]["card"]}</p></a>' for o in others) + '</div>'
        byline = f'{UI["ar"]["by"]}، ميديا باير في الرياض' if ar else 'By Ibrahem Muhamed, media buyer in Riyadh'
        if not others: more = ''
        main = (crumbs_html(cr) + f'<div class="w"><article><header class="ph narrow"><span class="label">{kk} · <bdi>{a["read"]}</bdi> {UI[lang]["read"]}</span><h1>{t["title"]}</h1>'
                f'<p class="meta-line"><span>{byline}</span><span>{UI[lang]["upd"]} <bdi>{a["date"]}</bdi></span></p></header>'
                f'<div class="prose narrow">{t["body"]}{("<h2>" + ("أسئلة شائعة" if ar else "Questions") + "</h2>") if faq else ""}</div><div class="faq narrow">{faq}</div></article>'
                + (f'<div class="hub-sec narrow"><h2>{"مقالات أخرى" if ar else "More guides"}</h2>{more}</div>' if more else '') + '</div>')
        schema = [{"@type": "Article", "headline": t['title'], "description": t['desc'], "inLanguage": lang, "datePublished": a['date'], "dateModified": a['date'],
                   "author": AUTHOR, "publisher": AUTHOR, "image": D + "/og.jpg", "mainEntityOfPage": D + path}] + \
                  ([faq_ld(t['faq'])] if t['faq'] else []) + [crumbs_ld(cr)]
        write(path, shell(lang, path, t['meta_title'], t['desc'], alts, main, schema, cur='guides', lang_link=dict(alts).get('ar' if not ar else 'en', '/ar/' if not ar else '/')))
    SITEMAP.append(alts)

# ---------- resources hubs ----------
def case_cards(lang):
    ar = lang == 'ar'
    return '<div class="cards">' + ''.join(
        f'<a class="card" href="{("/ar" if ar else "")}/cases/{c["slug"]}/"><span class="k">{c[lang]["kicker"].split(" · ")[0]}</span><h3>{c[lang]["title"]}</h3><p>{c[lang]["card"]}</p><span class="go">{"اقرأ دراسة الحالة ←" if ar else "Read the case →"}</span></a>'
        for c in CASES) + '</div>'
def article_cards(lang):
    ar = lang == 'ar'; pre = '/ar' if ar else ''
    return '<div class="cards">' + ''.join(
        f'<a class="card" href="{pre}/articles/{a["slug"]}/"><span class="k">{"مقال" if ar else "Guide"} · <bdi>{a["read"]}</bdi> {"دقائق" if ar else "min"}</span><h3>{a[lang]["title"]}</h3><p>{a[lang]["card"]}</p><span class="go">{"اقرأ المقال ←" if ar else "Read the guide →"}</span></a>'
        for a in arts(lang)) + '</div>'
def tool_cards(lang):
    ar = lang == 'ar'; pre = '/ar' if ar else ''
    return '<div class="cards">' + ''.join(
        f'<a class="card" href="{pre}/tools/{tl["slug"]}/"><span class="k">{tl["T"][lang]["kicker"]}</span><h3>{tl["T"][lang]["title"]}</h3><p>{tl["T"][lang]["card"]}</p><span class="go">{"افتح الحاسبة ←" if ar else "Open the calculator →"}</span></a>'
        for tl in TOOLS) + '</div>'
alts = [('en', '/resources/'), ('ar', '/ar/resources/')]
for lang in ['en', 'ar']:
    ar = lang == 'ar'; path = dict(alts)[lang]
    title = 'دراسات حالة وأدوات ومقالات في الإعلانات الممولة | إبراهيم محمد' if ar else 'Case studies, tools and guides on paid media | Ibrahem Muhamed'
    desc = ('دراسات حالة بأرقام حقيقية من الحسابات الإعلانية، وحاسبات مجانية لـROAS التعادل والعائد على الاستثمار، ومقالات لأصحاب المتاجر في السعودية عن سناب شات وتيك توك وميتا وجوجل.' if ar else
            'Case studies with real ad-account numbers, free break-even ROAS and ROI calculators, and guides for Saudi store owners on Snapchat, TikTok, Meta and Google.')
    cr = [('الرئيسية' if ar else 'Home', UI[lang]['home']), (UI[lang]['res'], path)]
    tool_card = tool_cards(lang)
    main = (crumbs_html(cr) + f'<div class="w"><header class="ph"><span class="label">{UI[lang]["res"]}</span><h1>{"دراسات حالة، أدوات، ومقالات" if ar else "Cases, tools & guides"}</h1><p class="lead">{desc}</p></header>'
            f'<section class="hub-sec" id="cases"><h2>{UI[lang]["cases"]}</h2>{case_cards(lang)}</section>'
            f'<section class="hub-sec" id="tools"><h2>{"الأدوات" if ar else "Tools"}</h2>{tool_card}</section>'
            f'<section class="hub-sec" id="articles"><h2>{"المقالات" if ar else "Guides"}</h2>{article_cards(lang)}</section></div>')
    schema = [{"@type": "CollectionPage", "name": title, "description": desc, "url": D + path, "inLanguage": lang, "author": AUTHOR}, crumbs_ld(cr)]
    write(path, shell(lang, path, title, desc, alts, main, schema, og_type='website'))
SITEMAP.append(alts)

# ---------- homepage ----------
i = src.index('<div class="progress"')
head_part = src[:i]; body = src[i:]
head_part = re.sub(r'<title>.*?</title>\s*', '', head_part); head_part = re.sub(r'<meta name="claude:[^>]*>\s*', '', head_part)

RES_CSS = '''<style>
.hdr-left .bt{display:none}
.top nav{gap:14px}
.res>.wrap{padding-block:88px;display:grid;gap:26px;border-top:1px solid var(--line)}
.res-head{display:grid;gap:10px;max-width:680px}
.res-head h2{font-size:clamp(28px,4vw,40px)}
.res-head p{color:var(--muted)}
.res-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.res-grid.five{grid-template-columns:repeat(5,minmax(0,1fr))}
.res-grid.five .res-card{padding:15px}
.res-grid.five .res-card h3{font-size:15.5px}
.res-grid.five .res-card p{display:none}
.res>.wrap{padding-block:64px}
.res-card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px;display:grid;gap:8px;align-content:start;text-decoration:none;color:var(--fg);transition:border-color .2s,transform .2s}
.res-card:hover{border-color:var(--yellow);transform:translateY(-2px)}
.res-card .k{font-family:var(--f-mono);font-size:11.5px;color:var(--yellow);letter-spacing:.08em;text-transform:uppercase}
.res-card[lang="ar"] .k,:root[lang="ar"] .res-card .k{font-family:"IBM Plex Sans Arabic",sans-serif;letter-spacing:0;font-size:12.5px}
.res-card[lang="ar"]{font-family:"IBM Plex Sans Arabic",sans-serif}
.res-card h3{font-size:18px;line-height:1.3}
.res-card[lang="ar"] h3{font-family:"IBM Plex Sans Arabic",sans-serif;letter-spacing:0;line-height:1.45}
.res-card p{font-size:14px;color:var(--muted);line-height:1.55}
.res-card .go{font-size:13.5px;margin-top:2px}
.case-link{display:inline-flex;gap:8px;align-items:center;font-size:14.5px;color:var(--fg);text-decoration:none;border-bottom:1px solid var(--yellow);padding-bottom:2px;justify-self:start}
.case-link:hover{color:var(--yellow)}
.results>.wrap{padding-block:80px;display:grid;gap:28px;border-top:1px solid var(--line)}
.rc-head{display:grid;gap:10px;max-width:680px}
.rc-head h2{font-size:clamp(28px,4vw,40px)}
.rc-head p{color:var(--muted)}
.rc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.rc{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:20px;display:grid;gap:14px;align-content:start;grid-template-rows:auto auto 1fr auto auto}
.rc .tagline{display:flex;gap:10px;flex-wrap:wrap}
.rc .big{font-family:var(--f-display);font-weight:800;font-size:clamp(44px,5vw,58px);line-height:1;display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.rc .big .cu{background:linear-gradient(transparent 62%,var(--hl) 62%);padding:0 3px}
.rc .big small{font-size:14px;color:var(--muted);font-weight:500;font-family:var(--f-body)}
.rc h3{font-size:17px;line-height:1.4;font-weight:600}
.rc .kpis{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.rc .kpi .v{font-size:19px}
.rc .kpi .k{font-size:12.5px}
.case-go{justify-self:start}
@media (max-width:900px){.rc-grid{grid-template-columns:1fr}.rc{grid-template-rows:none}}
@media (max-width:620px){
 .services,.steps5,.rc-grid{display:flex !important;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;padding-bottom:6px;margin-inline:-16px;padding-inline:16px;scrollbar-width:none}
 .services::-webkit-scrollbar,.steps5::-webkit-scrollbar,.rc-grid::-webkit-scrollbar{display:none}
 .services>.svc,.steps5>li{flex:0 0 78%;scroll-snap-align:start}
 .rc-grid>.rc{flex:0 0 86%;scroll-snap-align:start}
 .me,.me-card{max-height:200px}
 .me-card{aspect-ratio:auto !important;height:200px}
}
@media (max-width:1000px){.res-grid,.res-grid.five{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.res-grid,.res-grid.five{grid-template-columns:1fr}}
</style>'''

short = {'edtech-251-percent-of-target': ('Case 01 · EdTech', '251% of the monthly revenue target'),
         'ecommerce-882-orders': ('Case 02 · E-commerce', '882 orders against a 500 target'),
         'b2b-snapchat-leads': ('Case 03 · B2B', '70% of leads closed, SAR 260K revenue')}
cards1 = ''.join(f'<a class="res-card" href="cases/{c["slug"]}/"><span class="k">{short[c["slug"]][0]}</span><h3>{short[c["slug"]][1]}</h3><p>{c["en"]["card"]}</p><span class="go">Read the case →</span></a>' for c in CASES)
cards2 = ''.join(f'<a class="res-card" href="tools/{tl["slug"]}/"><span class="k">Free tool</span><h3>{tl["T"]["en"]["title"]}</h3><p>{tl["T"]["en"]["card"]}</p><span class="go">Open the calculator →</span></a>' for tl in TOOLS)
cards3_ar = ''.join(f'<a class="res-card" href="articles/{a["slug"]}/"><span class="k">مقال · <bdi dir="ltr">{a["read"]}</bdi> دقائق</span><h3>{a["ar"]["title"]}</h3><span class="go">اقرأ المقال ←</span></a>' for a in arts('ar')[:3])
cards3 = ''.join(f'<a class="res-card" href="articles/{a["slug"]}/"><span class="k">Guide · {a["read"]} min</span><h3>{a["en"]["title"]}</h3><span class="go">Read the guide →</span></a>' for a in arts('en')[:3])
RES = f'''<section class="res" id="resources">
  <div class="wrap">
    <div class="res-head"><span class="label">Tools &amp; guides</span><h2>Free tools and guides</h2><p>Calculators for your margins and profit, and practical guides for store owners.</p></div>
    <div class="res-grid five">{cards2}{cards3}</div>
    <a class="btn" href="resources/" style="justify-self:start">All resources <i>→</i></a>
  </div>
</section>
'''
body = body.replace('<section class="check" id="check">', RES + '<section class="check" id="check">', 1)
# compact case sections: headline, target bar and KPIs only; the full story lives on the case page
def block(sec, cls):
    i = sec.index(f'\n    <div class="{cls}"'); j = sec.index('\n    </div>', i)
    # walk forward until the 4-space-indented closing tag balances
    depth = 0; k = i
    for m in re.finditer(r'<div\b|</div>', sec[i:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return sec[i:i + m.end()]
    raise ValueError(cls)
PICK = {'edtech': [1, 2], 'fragrance': [0, 1], 'leads': [0, 1]}
cards = ''
first = None
for sid, c in zip(['edtech', 'fragrance', 'leads'], CASES):
    a = body.index(f'<section class="case" id="{sid}">'); e = body.index('</section>', a) + len('</section>')
    sec = body[a:e]
    tags = ''.join(re.findall(r'<span class="tag[^"]*">.*?</span>', sec)[:2])
    title = re.search(r'<h2>(.*?)</h2>', sec).group(1)
    big = re.search(r'<div class="big mono">(.*?)</div>', sec).group(1)
    kp = block(sec, 'kpis'); items = re.findall(r'<div class="kpi">.*?</span></div>', kp, re.S)
    k2 = ''.join(items[i] for i in PICK[sid])
    cards += (f'<article class="rc" id="{"rc-" + sid if sid == "edtech" else sid}"><div class="tagline">{tags}</div>'
              f'<div class="big mono">{big}</div><h3>{title}</h3><div class="kpis">{k2}</div>'
              f'<a class="btn case-go" href="cases/{c["slug"]}/">Read the full case <i>→</i></a></article>')
    if first is None:
        first = (a, e); body = body[:a] + '@@RESULTS@@' + body[e:]
    else:
        body = body[:a] + body[e:]
RESULTS = f'''<section class="results" id="edtech">
  <div class="wrap">
    <div class="rc-head"><span class="label">Results</span><h2>Three accounts, judged on revenue</h2><p>The headline numbers. Each case has its own page with the full story, the channel breakdown and the screenshots.</p></div>
    <div class="rc-grid">{cards}</div>
  </div>
</section>'''
body = body.replace('@@RESULTS@@', RESULTS)

# translations + selectors
m = re.search(r'var I18N_AR=(\{.*?\});\n', body, re.S); dct = json.loads(m.group(1))
dct.update({
 'Cases, tools & guides': 'دراسات حالة، أدوات، ومقالات',
 'Go deeper before we talk': 'تعرّف على شغلي أكثر قبل أن نتحدث',
 'Every case on its own page, free calculators for your margins and profit, and practical guides for store owners.': 'كل دراسة حالة في صفحة مستقلة، وحاسبات مجانية لهامش ربحك وأرباحك، ومقالات عملية لأصحاب المتاجر.',
 'Read the guide →': 'اقرأ المقال ←',
 'Tools & guides': 'أدوات ومقالات', 'Free tools and guides': 'أدوات ومقالات مجانية',
 'Calculators for your margins and profit, and practical guides for store owners.': 'حاسبات لهامش ربحك وأرباحك، ومقالات عملية لأصحاب المتاجر.',
 'Read the full case →': 'اقرأ دراسة الحالة كاملة <i>←</i>',
 'Three accounts, judged on revenue': 'ثلاثة حسابات، والحكم فيها للمبيعات',
 'The headline numbers. Each case has its own page with the full story, the channel breakdown and the screenshots.': 'أهم الأرقام فقط، ولكل دراسة حالة صفحة مستقلة فيها القصة كاملة وتفصيل القنوات واللقطات.',
 'Case 01 · EdTech': 'دراسة حالة <bdi dir="ltr">01</bdi> · تعليم', 'Case 02 · E-commerce': 'دراسة حالة <bdi dir="ltr">02</bdi> · تجارة إلكترونية', 'Case 03 · B2B': 'دراسة حالة <bdi dir="ltr">03</bdi> · B2B',
 '251% of the monthly revenue target': 'تحقيق <bdi dir="ltr">251%</bdi> من المستهدف الشهري',
 '882 orders against a 500 target': '<bdi dir="ltr">882</bdi> طلبًا مقابل مستهدف <bdi dir="ltr">500</bdi>',
 '70% of leads closed, SAR 260K revenue': 'إغلاق <bdi dir="ltr">70%</bdi> من العملاء و<bdi dir="ltr">260</bdi> ألف ريال',
 'Read the case →': 'اقرأ دراسة الحالة ←', 'Free tool': 'أداة مجانية', 'Break-even ROAS calculator': 'حاسبة ROAS التعادل',
 'The lowest ROAS your margins can survive, in 30 seconds.': 'أقل عائد يتحمله هامش ربحك، في <bdi dir="ltr">30</bdi> ثانية.',
 'Open the calculator →': 'افتح الحاسبة ←', 'All resources →': 'كل المصادر <i>←</i>',
 'Open this case as a full page →': 'افتح دراسة الحالة في صفحة مستقلة <i>←</i>',
})
for c in CASES:
    dct[c['en']['card']] = c['ar']['card']
for tl in TOOLS:
    dct[tl['T']['en']['title']] = tl['T']['ar']['title']; dct[tl['T']['en']['card']] = tl['T']['ar']['card']
for a in [x for x in ARTICLES if 'en' in x and 'ar' in x]:
    dct[a['en']['title']] = a['ar']['title']
    dct[f"Guide · {a['read']} min"] = f'مقال · <bdi dir="ltr">{a["read"]}</bdi> دقائق'
body = body[:m.start(1)] + json.dumps(dct, ensure_ascii=False) + body[m.end(1):]
body = body.replace("var CAND='", "var CAND='.case-go,.rc h3,.rc .big small,.rc-head h2,.rc-head p,.res-head .label,.res-head h2,.res-head p,.res-card:not([lang]) .k,.res-card:not([lang]) h3,.res-card:not([lang]) p,.res-card:not([lang]) .go,.case-link,", 1)

body = re.sub(r'(<div class="brand">.*?</div>)', lambda m: '<div class="hdr-left" style="display:flex;align-items:center;gap:12px">' + BTN['en'] + m.group(1) + '</div>', body, count=1, flags=re.S)
HOME_DW = drawer(['en', 'ar'], {'en': '/', 'ar': '/ar/'}, {'en': wa('en'), 'ar': wa('ar')}, {'en': '/ar/', 'ar': '/'}, {'en': 'left', 'ar': 'left'})
body = body + HOME_DW
LANG_INIT = "(function(){var l=null;try{l=localStorage.getItem('lang')}catch(e){}\n    if(!l&&(navigator.language||'').toLowerCase().indexOf('ar')===0)l='ar';\n    if(l==='ar')setLang('ar');})();"
assert LANG_INIT in body
home_ld = ld(PERSON, WEBSITE, SERVICE)
H = {'en': ('Ibrahem Muhamed — Media Buyer · Paid media judged on revenue',
            'I run paid media on Snapchat, TikTok, Meta and Google for Saudi brands. The results here come straight from the ad accounts. Your first account audit is free, 25 minutes.'),
     'ar': ('إبراهيم محمد — ميديا باير | إعلانات تُقاس بالمبيعات',
            'أدير إعلانات سناب شات وتيك توك وميتا وجوجل لعلامات سعودية، والنتائج هنا من الحسابات الإعلانية نفسها. أول مراجعة لحسابك مجانية، 25 دقيقة.')}
home_alts = [('en', '/'), ('ar', '/ar/')]
en_body = body.replace(LANG_INIT, "(function(){var l=null;try{l=localStorage.getItem('lang')}catch(e){}\n    if(l==='ar')setLang('ar');})();")
open(f'{S}/index.html', 'w').write(head('en', '/', *H['en'], home_alts, 'profile', home_ld) + head_part + RES_CSS + '</head>\n<body>\n' + en_body + '\n</body>\n</html>\n')
os.makedirs(f'{S}/ar', exist_ok=True)
ar_body = body.replace(cards3, cards3_ar).replace('img/', '../img/').replace(LANG_INIT, "setLang('ar');")
open(f'{S}/ar/index.html', 'w').write(head('ar', '/ar/', *H['ar'], home_alts, 'profile', home_ld) + head_part.replace('img/', '../img/') + RES_CSS + '</head>\n<body>\n' + ar_body + '\n</body>\n</html>\n')
SITEMAP.insert(0, home_alts)

# ---------- robots, sitemap, llms.txt ----------
open(f'{S}/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {D}/sitemap.xml\n')
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for alts in SITEMAP:
    links = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{D}{u}"/>' for l, u in alts) if len(alts) > 1 else ''
    if len(alts) > 1 and 'en' in dict(alts): links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{D}{dict(alts)["en"]}"/>'
    for l, u in alts:
        sm.append(f'  <url><loc>{D}{u}</loc><lastmod>{TODAY}</lastmod>{links}</url>')
sm.append('</urlset>')
open(f'{S}/sitemap.xml', 'w').write('\n'.join(sm) + '\n')

llms = f'''# Ibrahem Muhamed (إبراهيم محمد)

> Senior performance marketing and media buying specialist based in Riyadh, Saudi Arabia. Also known as Rio. 6+ years running paid media on Snapchat, TikTok, Meta and Google Ads for e-commerce, digital-product (EdTech) and B2B lead-generation brands in Saudi Arabia, the GCC and Egypt. Has worked with 15+ Saudi brands. Offers a free 25-minute ad account audit.

## Key facts
- Location: Riyadh, Saudi Arabia. Works in Arabic and English.
- Platforms: Snapchat Ads, TikTok Ads, Meta Ads (Facebook and Instagram), Google Ads. Store platforms: Salla, Shopify.
- Tracking: GA4, Google Tag Manager, Snapchat and Meta pixels, UTM attribution.
- Certifications: Meta Certified Digital Marketing Associate, Google Ads.
- Approach: judges paid media on store revenue against target and MER (store revenue ÷ total ad spend), not on platform-reported ROAS alone.
- Contact: WhatsApp +966 53 057 0632 · ibrahem.work11@gmail.com · LinkedIn https://www.linkedin.com/in/r1io1

## Selected results (client names withheld under NDA)
- EdTech / online English courses, KSA: 251% of a SAR 444,000 monthly revenue target; 4.49x Snapchat ROAS on $66.2K spend; TikTok ROAS up to 8.58x.
- E-commerce perfume store, KSA: 882 orders against a 500-order target on $11.5K of media; 8.6x MER; 12.38x Instagram campaign ROAS.
- B2B lead generation on Snapchat, KSA: 636 leads at $1.73, 70% closed in the CRM, SAR 260K revenue from $1.1K media.

## Pages
- [Portfolio (English)]({D}/)
- [Portfolio (Arabic)]({D}/ar/)
''' + ''.join(f'- [Case study: {c["en"]["title"]}]({D}/cases/{c["slug"]}/)\n' for c in CASES) + \
''.join(f'- [{tl["T"]["en"]["title"]}]({D}/tools/{tl["slug"]}/)\n' for tl in TOOLS) + \
''.join(f'- [Guide: {a["en"]["title"]}]({D}/articles/{a["slug"]}/)\n' for a in arts('en')) + \
''.join(f'- [دليل: {a["ar"]["title"]}]({D}/ar/articles/{a["slug"]}/)\n' for a in arts('ar'))
open(f'{S}/llms.txt', 'w').write(llms)
print('pages:', sum(len(a) for a in SITEMAP))
