"""Site settings (content/settings.json, editable from /admin → Settings) and the tracking snippets built from them.

Every ID is optional. Empty IDs add nothing to the pages.
Lead events fire on WhatsApp / email / phone clicks and on the contact form:
  GA4: generate_lead · Meta: Lead · Snapchat: SIGN_UP · TikTok: Contact
"""
import os, json, html
ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(ROOT, 'content', 'settings.json')
DEFAULTS = {'ga4_id': '', 'meta_pixel_id': '', 'snap_pixel_id': '', 'tiktok_pixel_id': '', 'google_site_verification': ''}

def load():
    d = dict(DEFAULTS)
    if os.path.exists(PATH):
        d.update({k: str(v or '').strip() for k, v in json.load(open(PATH, encoding='utf-8')).items()})
    return d

SETTINGS = load()

def head_tags():
    s = SETTINGS; out = ''
    if s['google_site_verification']:
        out += f'<meta name="google-site-verification" content="{html.escape(s["google_site_verification"])}">'
    if s['ga4_id']:
        g = html.escape(s['ga4_id'])
        out += (f'<script async src="https://www.googletagmanager.com/gtag/js?id={g}"></script>'
                f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{g}');</script>")
    if s['meta_pixel_id']:
        m = html.escape(s['meta_pixel_id'])
        out += ("<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};"
                "if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];"
                f"s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{m}');fbq('track','PageView');</script>")
    if s['snap_pixel_id']:
        p = html.escape(s['snap_pixel_id'])
        out += ("<script>(function(e,t,n){if(e.snaptr)return;var a=e.snaptr=function(){a.handleRequest?a.handleRequest.apply(a,arguments):a.queue.push(arguments)};"
                "a.queue=[];var s='script';var r=t.createElement(s);r.async=!0;r.src=n;var u=t.getElementsByTagName(s)[0];u.parentNode.insertBefore(r,u)})"
                f"(window,document,'https://sc-static.net/scevent.min.js');snaptr('init','{p}');snaptr('track','PAGE_VIEW');</script>")
    if s['tiktok_pixel_id']:
        t = html.escape(s['tiktok_pixel_id'])
        out += ("<script>!function(w,d,t){w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=['page','track','identify','instances','debug','on','off','once','ready','alias','group','enableCookie','disableCookie'];"
                "ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);"
                "ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e};"
                "ttq.load=function(e,n){var i='https://analytics.tiktok.com/i18n/pixel/events.js';ttq._i=ttq._i||{};ttq._i[e]=[];ttq._i[e]._u=i;ttq._t=ttq._t||{};ttq._t[e]=+new Date;ttq._o=ttq._o||{};ttq._o[e]=n||{};"
                "var o=document.createElement('script');o.type='text/javascript';o.async=!0;o.src=i+'?sdkid='+e+'&lib='+t;var a=document.getElementsByTagName('script')[0];a.parentNode.insertBefore(o,a)};"
                f"ttq.load('{t}');ttq.page()}}(window,document,'ttq');</script>")
    if any(s[k] for k in ['ga4_id', 'meta_pixel_id', 'snap_pixel_id', 'tiktok_pixel_id']):
        out += LEAD_JS
    return out

LEAD_JS = """<script>
(function(){function lead(src){try{if(window.gtag)gtag('event','generate_lead',{method:src});if(window.fbq)fbq('track','Lead',{content_name:src});
if(window.snaptr)snaptr('track','SIGN_UP',{description:src});if(window.ttq)ttq.track('Contact',{content_name:src})}catch(e){}}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('wa.me')>-1)lead('whatsapp');else if(h.indexOf('mailto:')===0)lead('email');else if(h.indexOf('tel:')===0)lead('phone')},true);
document.addEventListener('submit',function(e){if(e.target&&e.target.getAttribute('name')==='contact')lead('contact_form')},true);})();
</script>"""
