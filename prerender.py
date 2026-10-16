"""Pre-renders the Arabic homepage at build time.

The homepage switches language in the browser using the I18N_AR dictionary. Search engines read the
raw HTML first, so for /ar/ we apply the same dictionary here, in Python, and keep the original English
in a data-en attribute so the in-page EN toggle still works.
"""
import re, json, copy
from bs4 import BeautifulSoup

def _attached(el, root):
    p = el
    while p is not None:
        if p is root:
            return True
        p = p.parent
    return False

def _key(el):
    c = copy.copy(el)
    for x in c.select('.cur'):
        x.string = x.get('data-usd', '')
    return re.sub(r'\s+', ' ', c.get_text()).strip()

def prerender_ar(body_html):
    cand = re.search(r"var CAND='([^']*)'", body_html).group(1)
    m = re.search(r'var I18N_AR=(\{.*?\});\n', body_html, re.S)
    d = json.loads(m.group(1))
    soup = BeautifulSoup(body_html, 'html.parser')
    done = 0
    for el in soup.select(cand):
        if not _attached(el, soup) or 'cur' in (el.get('class') or []):
            continue
        t = d.get(_key(el))
        if t is None:
            continue
        el['data-en'] = el.decode_contents()
        el.clear()
        el.append(BeautifulSoup(t, 'html.parser'))
        done += 1
    return str(soup), done

# JS run on /ar/ instead of the normal language bootstrap: adopt the pre-rendered Arabic, then run
# setLang('ar') for its side effects (buttons, WhatsApp links, currency, quiz text).
AR_BOOT = ("document.querySelectorAll('[data-en]').forEach(function(el){el.__en=el.getAttribute('data-en');"
           "el.removeAttribute('data-en')});setLang('ar');")
