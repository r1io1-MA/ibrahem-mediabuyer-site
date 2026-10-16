"""Draws the original cover illustrations and share (OG) images.

Run locally (needs Playwright + Chromium):  python3 tools_dev/covers.py
Outputs:  static/img/covers/<topic>.webp   (16:9 covers, no text)
          static/og/<page-key>.jpg          (1200x630 share images with the page title)
Netlify does not run this; the generated files are committed.
"""
import os, sys, json, base64, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.environ.get('FONT_DIR', '')

P, L, W, D, A = '#8d9bff', '#c9cfff', '#f2f3f8', '#0b0d16', '#ffcf8a'   # periwinkle, lavender, white, ink, warm accent

def bars(x, y, hs, w=34, gap=16, c=P):
    out = ''
    for i, h in enumerate(hs):
        out += f'<rect x="{x+i*(w+gap)}" y="{y-h}" width="{w}" height="{h}" rx="8" fill="{c if i < len(hs)-1 else W}" opacity="{0.55+0.45*i/len(hs):.2f}"/>'
    return out

MOTIFS = {
 # graduation cap over an open laptop, rising bars
 'edtech': f'''
  <rect x="300" y="250" width="420" height="250" rx="22" fill="#151a2e" stroke="{P}" stroke-width="3"/>
  <rect x="330" y="280" width="360" height="190" rx="10" fill="#0f1322"/>
  {bars(360, 450, [50, 85, 120, 165])}
  <path d="M250 515 h520 l-40 30 h-440 z" fill="{L}"/>
  <path d="M510 120 l170 60 -170 60 -170 -60 z" fill="{W}"/>
  <path d="M420 200 v55 q90 45 180 0 v-55 l-90 32 z" fill="{P}"/>
  <path d="M680 180 v80" stroke="{A}" stroke-width="6" stroke-linecap="round"/><circle cx="680" cy="268" r="11" fill="{A}"/>''',
 # shopping bag + perfume bottle + rising line
 'ecommerce': f'''
  <path d="M300 250 h250 l25 270 h-300 z" fill="{P}"/>
  <path d="M370 250 v-35 a55 55 0 0 1 110 0 v35" fill="none" stroke="{W}" stroke-width="12" stroke-linecap="round"/>
  <rect x="595" y="300" width="140" height="220" rx="34" fill="{L}"/>
  <rect x="640" y="250" width="50" height="55" rx="10" fill="{W}"/><rect x="630" y="232" width="70" height="26" rx="8" fill="{A}"/>
  <rect x="620" y="380" width="90" height="56" rx="12" fill="{D}" opacity=".25"/>
  <path d="M250 170 L360 140 L450 160 L560 95 L700 70" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M700 70 l-34 2 m34 -2 l-10 32" stroke="{A}" stroke-width="8" stroke-linecap="round"/>''',
 # funnel with dots -> check badge
 'b2b': f'''
  <path d="M260 140 h360 l-130 170 v140 l-100 50 v-190 z" fill="{P}"/>
  {''.join(f'<circle cx="{300+i*45}" cy="{110 - (i%2)*22}" r="13" fill="{W if i%3 else A}"/>' for i in range(8))}
  <circle cx="440" cy="240" r="10" fill="{W}"/><circle cx="440" cy="300" r="10" fill="{W}"/>
  <circle cx="680" cy="420" r="85" fill="{L}"/>
  <path d="M640 420 l28 30 l55 -62" fill="none" stroke="{D}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M520 470 q60 0 90 -30" fill="none" stroke="{W}" stroke-width="6" stroke-dasharray="4 14" stroke-linecap="round"/>''',
 # crescent, lanterns, calendar, price tag going up
 'seasonal': f'''
  <circle cx="330" cy="170" r="80" fill="{A}"/><circle cx="365" cy="150" r="75" fill="#0f1322"/>
  <path d="M520 60 v70 M640 60 v40" stroke="{L}" stroke-width="3"/>
  <path d="M495 130 h50 l12 30 -12 70 h-50 l-12 -70 z" fill="{P}"/><rect x="505" y="160" width="30" height="45" rx="6" fill="{A}" opacity=".9"/>
  <path d="M618 100 h44 l10 26 -10 60 h-44 l-10 -60 z" fill="{L}"/><rect x="628" y="128" width="24" height="38" rx="5" fill="{A}" opacity=".8"/>
  <rect x="290" y="300" width="260" height="220" rx="20" fill="{W}"/><rect x="290" y="300" width="260" height="58" rx="20" fill="{P}"/><rect x="290" y="335" width="260" height="23" fill="{P}"/>
  {''.join(f'<rect x="{318+(i%5)*44}" y="{378+(i//5)*42}" width="30" height="28" rx="6" fill="{P if i in (7,12) else "#d9dcf0"}"/>' for i in range(15))}
  <path d="M600 470 l90 -90 h70 v70 l-90 90 z" fill="{A}"/><circle cx="735" cy="405" r="11" fill="#0f1322"/>
  <path d="M650 320 v-80 m0 0 l-25 25 m25 -25 l25 25" stroke="{W}" stroke-width="9" stroke-linecap="round"/>''',
 # two phones split
 'platforms': f'''
  <rect x="290" y="90" width="200" height="400" rx="34" fill="{A}"/><rect x="305" y="120" width="170" height="340" rx="18" fill="#141827"/>
  <circle cx="390" cy="230" r="44" fill="{W}"/><rect x="335" y="300" width="110" height="14" rx="7" fill="{W}" opacity=".7"/><rect x="350" y="328" width="80" height="14" rx="7" fill="{W}" opacity=".45"/>
  <rect x="540" y="130" width="200" height="400" rx="34" fill="{P}"/><rect x="555" y="160" width="170" height="340" rx="18" fill="#141827"/>
  <path d="M615 260 l60 35 -60 35 z" fill="{W}"/><rect x="585" y="380" width="110" height="14" rx="7" fill="{L}"/><rect x="600" y="408" width="80" height="14" rx="7" fill="{L}" opacity=".6"/>
  <path d="M515 70 v470" stroke="{W}" stroke-width="3" stroke-dasharray="6 12" opacity=".5"/>''',
 # magnifier over dashboard
 'audit': f'''
  <rect x="270" y="140" width="420" height="300" rx="24" fill="#151a2e" stroke="{L}" stroke-width="3"/>
  {bars(310, 400, [70, 120, 90, 170, 140], w=40, gap=22)}
  <rect x="310" y="175" width="140" height="16" rx="8" fill="{L}" opacity=".7"/>
  <circle cx="630" cy="380" r="95" fill="none" stroke="{W}" stroke-width="22"/>
  <circle cx="630" cy="380" r="84" fill="{P}" opacity=".18"/>
  <path d="M700 450 l85 85" stroke="{W}" stroke-width="30" stroke-linecap="round"/>
  <path d="M592 380 l26 28 l52 -58" fill="none" stroke="{A}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>''',
 # parcel + cash + return arrow
 'cod': f'''
  <path d="M290 230 l170 -70 170 70 v210 l-170 70 -170 -70 z" fill="{P}"/>
  <path d="M290 230 l170 70 170 -70 M460 300 v210" fill="none" stroke="{D}" stroke-opacity=".35" stroke-width="6"/>
  <path d="M370 195 l170 70 v60" fill="none" stroke="{W}" stroke-width="16" stroke-opacity=".85"/>
  <rect x="610" y="150" width="190" height="110" rx="14" fill="{A}" transform="rotate(-10 705 205)"/>
  <circle cx="705" cy="205" r="30" fill="#0f1322" opacity=".25"/>
  <path d="M760 360 a110 110 0 1 1 -60 -95" fill="none" stroke="{W}" stroke-width="10" stroke-linecap="round" stroke-dasharray="2 18"/>
  <path d="M700 268 l-35 -8 m35 8 l-12 34" stroke="{W}" stroke-width="10" stroke-linecap="round"/>''',
 # throttle/gauge + stairs
 'scaling': f'''
  {''.join(f'<rect x="{270+i*80}" y="{460-i*60}" width="80" height="{60+i*60}" rx="6" fill="{P}" opacity="{0.45+i*0.13:.2f}"/>' for i in range(5))}
  <path d="M290 420 L370 360 L450 300 L530 240 L610 180 L700 120" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="700" cy="120" r="16" fill="{A}"/>
  <path d="M600 520 a120 120 0 0 1 240 0" fill="none" stroke="{L}" stroke-width="22" stroke-linecap="round"/>
  <path d="M720 520 l55 -70" stroke="{W}" stroke-width="10" stroke-linecap="round"/><circle cx="720" cy="520" r="16" fill="{W}"/>''',
 # CRM card -> coins
 'deal': f'''
  <rect x="270" y="150" width="300" height="340" rx="24" fill="{W}"/>
  <circle cx="330" cy="215" r="30" fill="{P}"/><rect x="380" y="200" width="150" height="14" rx="7" fill="#c9cde0"/><rect x="380" y="224" width="100" height="12" rx="6" fill="#dfe2ef"/>
  {''.join(f'<rect x="300" y="{280+i*46}" width="240" height="30" rx="8" fill="{P if i==2 else "#e8eaf5"}"/>' for i in range(4))}
  {''.join(f'<ellipse cx="700" cy="{470-i*26}" rx="80" ry="22" fill="{A if i%2 else "#f5c56e"}"/>' for i in range(6))}
  <path d="M590 300 h60 m0 0 l-20 -18 m20 18 l-20 18" stroke="{L}" stroke-width="9" stroke-linecap="round"/>''',
 # calculator
 'tools': f'''
  <rect x="330" y="90" width="300" height="430" rx="34" fill="{L}"/>
  <rect x="360" y="125" width="240" height="90" rx="14" fill="#141827"/><rect x="470" y="160" width="105" height="26" rx="6" fill="{A}"/>
  {''.join(f'<rect x="{362+(i%4)*60}" y="{240+(i//4)*62}" width="48" height="48" rx="12" fill="{P if i%4==3 else W}"/>' for i in range(16))}
  <path d="M680 200 L740 150 L790 175 L860 100" fill="none" stroke="{A}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>''',
}

def scene(motif, w=1280, h=720, dx=0, dy=0, scale=1.0, glow=(0.7, 0.35)):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<defs>
 <radialGradient id="g1" cx="{glow[0]}" cy="{glow[1]}" r=".6"><stop offset="0" stop-color="{P}" stop-opacity=".45"/><stop offset="1" stop-color="{P}" stop-opacity="0"/></radialGradient>
 <radialGradient id="g2" cx=".15" cy=".95" r=".5"><stop offset="0" stop-color="{A}" stop-opacity=".18"/><stop offset="1" stop-color="{A}" stop-opacity="0"/></radialGradient>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>
</defs>
<rect width="{w}" height="{h}" fill="#0b0d16"/><rect width="{w}" height="{h}" fill="url(#grid)"/>
<rect width="{w}" height="{h}" fill="url(#g1)"/><rect width="{w}" height="{h}" fill="url(#g2)"/>
<g transform="translate({dx} {dy}) scale({scale})">{motif}</g>
</svg>'''

def font_css():
    if not FONT_DIR: return ''
    out = ''
    for fam, f, wt in [('Plex Arabic', 'ibm-plex-sans-arabic-arabic-700-normal.woff2', 700), ('Plex Arabic', 'ibm-plex-sans-arabic-latin-700-normal.woff2', 700),
                       ('Plex Arabic', 'ibm-plex-sans-arabic-arabic-400-normal.woff2', 400), ('Archivo', 'archivo-latin-800-normal.woff2', 800), ('Archivo', 'archivo-latin-700-normal.woff2', 700)]:
        p = os.path.join(FONT_DIR, f)
        if os.path.exists(p):
            b = base64.b64encode(open(p, 'rb').read()).decode()
            out += f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b}) format('woff2');font-weight:{wt}}}"
    return out

def og_html(topic, title, kicker, lang):
    ar = lang == 'ar'
    art = scene(MOTIFS[topic], 1280, 720, dx=(-190 if ar else 470), dy=70, scale=0.82)
    fam = "'Plex Arabic','Archivo',sans-serif" if ar else "'Archivo','Plex Arabic',sans-serif"
    logo = open(os.path.join(ROOT, 'static', 'assets', 'logo.svg')).read().replace('<svg ', '<svg width="56" height="56" ')
    return f'''<html><head><meta charset="utf-8"><style>{font_css()}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#0b0d16}}
.art{{position:absolute;inset:0}} .art svg{{width:1200px;height:auto;position:absolute;top:-45px;left:0}}
.fade{{position:absolute;inset:0;background:linear-gradient({'270deg' if ar else '90deg'},#0b0d16 34%,rgba(11,13,22,.75) 55%,rgba(11,13,22,0) 80%)}}
.t{{position:absolute;top:70px;{'right' if ar else 'left'}:70px;width:560px;direction:{'rtl' if ar else 'ltr'};font-family:{fam};color:#f2f3f8}}
.k{{font-size:24px;color:#8d9bff;font-weight:700;margin-bottom:22px;letter-spacing:{0 if ar else '.06em'};text-transform:{'none' if ar else 'uppercase'}}}
h1{{margin:0;font-size:{52 if len(title) < 70 else 44}px;line-height:{1.35 if ar else 1.12};font-weight:{700 if ar else 800};letter-spacing:{0 if ar else '-.02em'}}}
.by{{position:absolute;bottom:56px;{'right' if ar else 'left'}:70px;display:flex;align-items:center;gap:16px;direction:{'rtl' if ar else 'ltr'};font-family:{fam};color:#c9cfff;font-size:24px;font-weight:700}}
.by span{{color:#8f95ad;font-weight:400;font-size:20px}}
</style></head><body><div class="art">{art}</div><div class="fade"></div>
<div class="t"><div class="k">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1></div>
<div class="by">{logo}<div>{'إبراهيم محمد' if ar else 'Ibrahem Muhamed'}<br><span>ibrahem-mediabuyer.com</span></div></div></body></html>'''

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    os.makedirs(os.path.join(ROOT, 'static', 'img', 'covers'), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'static', 'og'), exist_ok=True)
    jobs = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        for topic, m in MOTIFS.items():
            pg.set_content(f'<html><body style="margin:0">{scene(m, dx=150, dy=40, scale=1.0)}</body></html>')
            png = os.path.join(ROOT, 'static', 'img', 'covers', topic + '.png')
            pg.screenshot(path=png)
            from PIL import Image
            Image.open(png).convert('RGB').save(png[:-4] + '.webp', 'WEBP', quality=82, method=6); os.remove(png)
        pg2 = b.new_page(viewport={'width': 1200, 'height': 630})
        for j in jobs:
            pg2.set_content(og_html(j['topic'], j['title'], j['kicker'], j['lang']))
            pg2.wait_for_timeout(150)
            png = os.path.join(ROOT, 'static', 'og', j['key'] + '.png')
            pg2.screenshot(path=png)
            from PIL import Image
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', 'JPEG', quality=86); os.remove(png)
        print('covers:', len(MOTIFS), 'og:', len(jobs))
