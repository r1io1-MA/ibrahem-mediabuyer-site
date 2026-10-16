
# Side menu (drawer) shared by every page. New articles appear automatically from ARTICLES.
from cases import CASES
from content import ARTICLES
from tools_reg import TOOLS

L = {
 'en': {'menu': 'Menu', 'close': 'Close menu', 'home': 'Home', 'port': 'Portfolio', 'about': 'About me', 'proof': 'Proof from the ad accounts',
        'check': 'Free 60-second check', 'contact': 'Contact', 'cases': 'Case studies', 'tools': 'Free tools', 'guides': 'Guides',
        'all': 'All cases, tools & guides', 'audit': 'Book the free 25-min audit', 'lang': 'العربية'},
 'ar': {'menu': 'القائمة', 'close': 'إغلاق القائمة', 'home': 'الرئيسية', 'port': 'البورتفوليو', 'about': 'نبذة عني', 'proof': 'إثباتات من الحسابات الإعلانية',
        'check': 'فحص مجاني في 60 ثانية', 'contact': 'تواصل معي', 'cases': 'دراسات الحالة', 'tools': 'أدوات مجانية', 'guides': 'المقالات',
        'all': 'كل دراسات الحالة والأدوات والمقالات', 'audit': 'احجز المراجعة المجانية (25 دقيقة)', 'lang': 'English'},
}
SHORT = {'en': {'edtech-251-percent-of-target': ('<bdi>251%</bdi> of target', 'EdTech'), 'ecommerce-882-orders': ('<bdi>882 / 500</bdi> orders', 'E-commerce'), 'b2b-snapchat-leads': ('<bdi>70%</bdi> of leads closed', 'B2B')},
         'ar': {'edtech-251-percent-of-target': ('<bdi>251%</bdi> من المستهدف', 'تعليم'), 'ecommerce-882-orders': ('<bdi>882 / 500</bdi> طلب', 'تجارة إلكترونية'), 'b2b-snapchat-leads': ('إغلاق <bdi>70%</bdi> من العملاء', 'B2B')}}

def links(lang, cur_path, wa_url, alt_url):
    l = L[lang]; ar = lang == 'ar'; pre = '/ar' if ar else ''; home = pre + '/'
    def a(href, txt, cls=''):
        on = ' aria-current="page"' if href == cur_path else ''
        return f'<a class="dw-a{cls}" href="{href}"{on}>{txt}</a>'
    h = (f'<div class="dw-g"><span class="dw-h">{l["port"]}</span>'
         + a(home, l['home']) + a(home + '#about', l['about']) + a(home + '#proof', l['proof'])
         + a(home + '#check', l['check']) + a(home + '#contact', l['contact']) + '</div>')
    h += (f'<div class="dw-g"><span class="dw-h">{l["cases"]}</span>'
          + ''.join(a(f'{pre}/cases/{c["slug"]}/', f'<span>{SHORT[lang][c["slug"]][0]}</span><small>{SHORT[lang][c["slug"]][1]}</small>') for c in CASES) + '</div>')
    h += (f'<div class="dw-g"><span class="dw-h">{l["tools"]}</span>' + ''.join(a(f'{pre}/tools/{tl["slug"]}/', tl['T'][lang]['title']) for tl in TOOLS) + '</div>')
    h += (f'<div class="dw-g"><span class="dw-h">{l["guides"]}</span>'
          + ''.join(a(f'{pre}/articles/{x["slug"]}/', x[lang]['title']) for x in ARTICLES if lang in x) + '</div>')
    h += a(f'{pre}/resources/', l['all'] + (' ←' if ar else ' →'), ' dw-all')
    h += (f'<div class="dw-foot"><a class="dw-cta" href="{wa_url}" target="_blank" rel="noopener">{l["audit"]}</a>'
          f'<a class="dw-lang" href="{alt_url}">{l["lang"]}</a></div>')
    return h

CSS = '''<style>
.dw-btn{width:40px;height:40px;border-radius:12px;border:1px solid #242838;background:#10121a;color:#f2f3f8;display:inline-grid;place-items:center;cursor:pointer;flex:0 0 auto;padding:0}
.dw-btn:hover{border-color:#8d9bff}
.dw-btn svg{width:18px;height:18px}
.dw-ov{position:fixed;inset:0;background:rgba(3,4,8,.62);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px);opacity:0;pointer-events:none;transition:opacity .25s;z-index:90}
.dw{position:fixed;top:0;bottom:0;width:min(350px,88vw);background:#0c0e15;border-inline-end:1px solid #242838;z-index:91;display:flex;flex-direction:column;transition:transform .3s cubic-bezier(.2,.8,.2,1);font-family:"Schibsted Grotesk","IBM Plex Sans Arabic",system-ui,sans-serif;color:#f2f3f8}
.dw[dir="rtl"]{font-family:"IBM Plex Sans Arabic",system-ui,sans-serif}
.dw[hidden]{display:none}
.dw.left{left:0;transform:translateX(-102%)}
.dw.right{right:0;transform:translateX(102%);border-inline-end:0;border-inline-start:1px solid #242838}
.dw-open .dw{transform:none}
.dw-open .dw-ov{opacity:1;pointer-events:auto}
.dw-top{display:flex;align-items:center;justify-content:space-between;padding:16px 18px;border-bottom:1px solid #242838}
.dw-top b{display:flex;align-items:center;gap:10px;font-family:"Archivo","IBM Plex Sans Arabic",sans-serif;font-size:15px}
.dw-top img{width:28px;height:28px;border-radius:8px}
.dw-x{width:36px;height:36px;border-radius:10px;border:1px solid #242838;background:transparent;color:#9097ab;cursor:pointer;font-size:20px;line-height:1}
.dw-x:hover{color:#f2f3f8;border-color:#9097ab}
.dw-body{flex:1;overflow-y:auto;padding:8px 10px 18px;overscroll-behavior:contain}
.dw-g{display:grid;padding:12px 0 8px;border-bottom:1px solid #1a1d29}
.dw-h{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6f7690;padding:4px 10px 6px}
.dw[dir="rtl"] .dw-h{font-family:"IBM Plex Sans Arabic",sans-serif;letter-spacing:0;font-size:12.5px}
.dw-a{display:grid;gap:1px;padding:9px 10px;border-radius:10px;color:#d9dce6;text-decoration:none;font-size:15px;line-height:1.4}
.dw bdi{unicode-bidi:isolate;direction:ltr}
.dw-a small{color:#7d8399;font-size:12.5px}
.dw-a:hover{background:#151824;color:#fff}
.dw-a[aria-current]{background:#171a2a;color:#fff;box-shadow:inset 3px 0 0 #8d9bff}
.dw[dir="rtl"] .dw-a[aria-current]{box-shadow:inset -3px 0 0 #8d9bff}
.dw-art{font-family:"IBM Plex Sans Arabic",sans-serif;font-size:14.5px}
.dw-art span{display:block;text-align:start}
.dw[dir="ltr"] .dw-art span{text-align:right}
.dw-all{margin-top:10px;color:#8d9bff;font-size:14.5px}
.dw-foot{display:grid;gap:8px;padding:14px 4px 0}
.dw-cta{display:block;text-align:center;background:#8d9bff;color:#0b0c14;border-radius:999px;padding:11px 14px;font-weight:600;text-decoration:none;font-size:14.5px}
.dw-lang{display:block;text-align:center;border:1px solid #242838;border-radius:999px;padding:9px 14px;color:#d9dce6;text-decoration:none;font-size:14px}
.dw-lang:hover{border-color:#9097ab}
html.dw-lock,html.dw-lock body{overflow:hidden}
@media (prefers-reduced-motion:reduce){.dw,.dw-ov{transition:none}}
</style>'''

BTN = {'en': '<button class="dw-btn" type="button" aria-label="Menu" aria-expanded="false" data-dw-open><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h10"/></svg></button>',
       'ar': '<button class="dw-btn" type="button" aria-label="القائمة" aria-expanded="false" data-dw-open><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M10 17h10"/></svg></button>'}

JS = '''<script>
(function(){var ov=document.querySelector('.dw-ov'),dws=[].slice.call(document.querySelectorAll('.dw')),last=null;
function cur(){var l=document.documentElement.lang==='ar'?'ar':'en';return dws.filter(function(d){return d.dataset.l===l})[0]||dws[0]}
function open(){var d=cur();dws.forEach(function(x){x.hidden=x!==d});last=document.activeElement;document.documentElement.classList.add('dw-open','dw-lock');
 document.querySelectorAll('[data-dw-open]').forEach(function(b){b.setAttribute('aria-expanded','true')});setTimeout(function(){var x=d.querySelector('.dw-x');x&&x.focus()},60)}
function close(){document.documentElement.classList.remove('dw-open','dw-lock');document.querySelectorAll('[data-dw-open]').forEach(function(b){b.setAttribute('aria-expanded','false')});if(last&&last.focus)last.focus()}
document.querySelectorAll('[data-dw-open]').forEach(function(b){b.addEventListener('click',open)});
ov.addEventListener('click',close);dws.forEach(function(d){d.querySelector('.dw-x').addEventListener('click',close);
 d.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){if(a.getAttribute('href').indexOf('#')>-1)close()})})});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.documentElement.classList.contains('dw-open'))close()});
})();
</script>'''

def panel(lang, cur_path, wa_url, alt_url, side):
    l = L[lang]
    return (f'<aside class="dw {side}" id="dw-{lang}" dir="{"rtl" if lang=="ar" else "ltr"}" lang="{lang}" data-l="{lang}" aria-label="{l["menu"]}">'
            f'<div class="dw-top"><b><img src="/assets/logo.svg" alt="">{"إبراهيم محمد" if lang=="ar" else "Ibrahem Muhamed"}</b>'
            f'<button class="dw-x" type="button" aria-label="{l["close"]}">×</button></div>'
            f'<nav class="dw-body">{links(lang, cur_path, wa_url, alt_url)}</nav></aside>')

def drawer(langs, cur_path, wa_urls, alt_urls, side):
    """langs: list of languages to render (homepage renders both for its in-page toggle)."""
    return CSS + '<div class="dw-ov" aria-hidden="true"></div>' + ''.join(panel(lg, cur_path[lg], wa_urls[lg], alt_urls[lg], side[lg]) for lg in langs) + JS
