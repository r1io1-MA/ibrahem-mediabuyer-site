
import json
SLUG = 'roi-calculator'

T = {
 'en': {
  'meta_title': 'Ad campaign ROI calculator: real profit after ads and fees | Ibrahem Muhamed',
  'desc': 'Free ROI calculator for paid ads: enter ad spend, management and creative costs, revenue and margin to see real profit, ROI, ROAS and the revenue you need to break even.',
  'kicker': 'Free tool',
  'title': 'Ad campaign ROI calculator',
  'card': 'Real profit after ad spend, fees and product costs, not just ROAS.',
  'lead': 'ROAS tells you how much revenue the ads brought in. ROI tells you whether you actually made money once product costs, ad spend and fees are paid. Enter one month and see both.',
  'f': [('spend', 'Ad spend', 'Total across all platforms for the period', 'SAR', 20000),
        ('fees', 'Management, creative & tools', 'Agency or freelancer fee, content, software', 'SAR', 6000),
        ('rev', 'Revenue from ads', 'Excluding VAT. Use store revenue if you can', 'SAR', 90000),
        ('margin', 'Gross margin', 'What is left after product, shipping and payment fees', '%', 40)],
  'big': 'ROI', 'profit': 'Net profit after ads & fees', 'roas': 'ROAS', 'be_rev': 'Revenue needed to break even', 'be_roas': 'Break-even ROAS (fees included)',
  'v_loss': 'This campaign is losing money once all costs are counted, even if the ROAS looks fine. Check the margin, cut weak campaigns, or raise the order value before adding budget.',
  'v_thin': 'Profitable, but thin. Small changes in costs or a weaker week can push it into a loss. Improve margin or conversion before you scale.',
  'v_ok': 'Healthy return. This is the point where adding budget carefully usually makes sense.',
  'cta': 'Send me these numbers',
  'wa': 'Hi Ibrahem, I used your ROI calculator. Spend {s} SAR, revenue {r} SAR, ROI {roi}. Can we talk about my account?',
  'how_h': 'How it is calculated',
  'how': '<p><strong>Gross profit</strong> = revenue × gross margin.</p><p><strong>Net profit</strong> = gross profit − ad spend − management, creative and tools.</p><p><strong>ROI</strong> = net profit ÷ (ad spend + management, creative and tools).</p><p><strong>Revenue to break even</strong> = (ad spend + other costs) ÷ gross margin.</p>',
  'faq': [('What is the difference between ROI and ROAS?', 'ROAS is revenue divided by ad spend. ROI is profit divided by everything you paid. A 4x ROAS can still lose money if your margin is 20%, which is why ROI is the number that decides whether to scale.'),
          ('Which margin should I use?', 'The share of each sale left after product cost, shipping and payment fees, before ads. If a SAR 100 order costs you SAR 45 in goods, SAR 12 in shipping and SAR 3 in fees, your gross margin is 40%.'),
          ('Should management and creative costs be included?', 'Yes. They are part of what it costs to get the sales. Leaving them out makes the campaign look better than it is.'),
          ('What if customers buy again later?', 'This calculator looks at one period. If you have strong repeat purchases, a first-month ROI near zero can still be a good deal. Compare it with how much a customer spends with you over a year.')],
 },
 'ar': {
  'meta_title': 'حاسبة العائد على الاستثمار (ROI) للحملات الإعلانية | إبراهيم محمد',
  'desc': 'حاسبة ROI مجانية للإعلانات الممولة: أدخل الإنفاق الإعلاني وتكلفة الإدارة والمحتوى والإيراد وهامش الربح، واعرف ربحك الحقيقي والعائد على الاستثمار والإيراد المطلوب للتعادل.',
  'kicker': 'أداة مجانية',
  'title': 'حاسبة العائد على الاستثمار (ROI)',
  'card': 'ربحك الحقيقي بعد الإعلانات والرسوم وتكلفة المنتج، وليس ROAS فقط.',
  'lead': 'الـROAS يخبرك بكم جلبت الإعلانات من إيراد، أما الـROI فيخبرك هل ربحت فعلًا بعد دفع تكلفة المنتج والإعلانات والرسوم. أدخل أرقام شهر واحد وشاهد الاثنين.',
  'f': [('spend', 'الإنفاق الإعلاني', 'الإجمالي على كل المنصات خلال الفترة', 'ر.س', 20000),
        ('fees', 'الإدارة والمحتوى والأدوات', 'أتعاب الوكالة أو المستقل، والمحتوى، والبرامج', 'ر.س', 6000),
        ('rev', 'الإيراد من الإعلانات', 'بدون الضريبة، ويُفضل استخدام إيراد المتجر', 'ر.س', 90000),
        ('margin', 'هامش الربح الإجمالي', 'ما يتبقى بعد المنتج والشحن ورسوم الدفع', '%', 40)],
  'big': 'العائد على الاستثمار', 'profit': 'صافي الربح بعد الإعلانات والرسوم', 'roas': 'ROAS', 'be_rev': 'الإيراد المطلوب للتعادل', 'be_roas': 'ROAS التعادل (شامل الرسوم)',
  'v_loss': 'الحملة خاسرة بعد احتساب كل التكاليف حتى لو بدا الـROAS جيدًا. راجع الهامش، وأوقف الحملات الضعيفة، أو ارفع قيمة الطلب قبل زيادة الميزانية.',
  'v_thin': 'رابحة لكن بهامش ضيق، وأي تغيير بسيط في التكاليف أو أسبوع ضعيف قد يحولها إلى خسارة. حسّن الهامش أو معدل التحويل قبل التوسع.',
  'v_ok': 'عائد صحي، وهنا غالبًا يكون رفع الميزانية بحذر قرارًا منطقيًا.',
  'cta': 'أرسل لي هذه الأرقام',
  'wa': 'مرحبًا إبراهيم، استخدمت حاسبة ROI. الإنفاق {s} ريال، والإيراد {r} ريال، والعائد على الاستثمار {roi}. أرغب في مناقشة حسابي.',
  'how_h': 'طريقة الحساب',
  'how': '<p><strong>الربح الإجمالي</strong> = الإيراد × هامش الربح الإجمالي.</p><p><strong>صافي الربح</strong> = الربح الإجمالي − الإنفاق الإعلاني − تكلفة الإدارة والمحتوى والأدوات.</p><p><strong>العائد على الاستثمار</strong> = صافي الربح ÷ (الإنفاق الإعلاني + تكلفة الإدارة والمحتوى والأدوات).</p><p><strong>الإيراد المطلوب للتعادل</strong> = (الإنفاق الإعلاني + التكاليف الأخرى) ÷ هامش الربح الإجمالي.</p>',
  'faq': [('ما الفرق بين ROI وROAS؟', 'ROAS هو الإيراد مقسومًا على الإنفاق الإعلاني، وROI هو الربح مقسومًا على كل ما دفعته. قد يكون الـROAS أربعة أضعاف ومع ذلك تخسر إذا كان هامشك 20%، لذلك فالـROI هو الرقم الذي يحدد قرار التوسع.'),
          ('أي هامش ربح أستخدم؟', 'النسبة المتبقية من كل عملية بيع بعد تكلفة المنتج والشحن ورسوم الدفع وقبل الإعلانات. فإذا كان الطلب بـ100 ريال ويكلفك 45 ريالًا بضاعة و12 شحنًا و3 رسومًا، فهامشك الإجمالي 40%.'),
          ('هل أحسب تكلفة الإدارة والمحتوى؟', 'نعم، فهي جزء من تكلفة الحصول على المبيعات، واستبعادها يجعل الحملة تبدو أفضل من حقيقتها.'),
          ('وماذا لو عاد العملاء للشراء لاحقًا؟', 'هذه الحاسبة تنظر إلى فترة واحدة. إذا كان تكرار الشراء عندك قويًا، فقد يكون عائد قريب من الصفر في الشهر الأول صفقة جيدة. قارنه بما ينفقه العميل معك خلال سنة.')],
 },
}

def body(lang):
    t = T[lang]
    fields = ''.join(
        f'<label for="{k}">{lab}<small>{hint}</small><span class="inp"><input id="{k}" type="number" inputmode="decimal" min="0" step="any" value="{dv}"><span>{unit}</span></span></label>'
        for k, lab, hint, unit, dv in t['f'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq'])
    js_t = {k: t[k] for k in ['v_loss', 'v_thin', 'v_ok', 'wa']}
    cur = 'SAR' if lang == 'en' else 'ر.س'
    return f'''
<div class="calc">
  <form id="calc" onsubmit="return false">{fields}</form>
  <div class="out" aria-live="polite">
    <span class="label">{t['big']}</span>
    <div class="big mono" id="o-roi">–</div>
    <div class="row"><span>{t['profit']}</span><b id="o-p">–</b></div>
    <div class="row"><span>{t['roas']}</span><b id="o-roas">–</b></div>
    <div class="row"><span>{t['be_rev']}</span><b id="o-ber">–</b></div>
    <div class="row"><span>{t['be_roas']}</span><b id="o-beroas">–</b></div>
    <p class="verdict" id="o-v"></p>
    <a class="btn primary" id="o-wa" href="https://wa.me/966530570632" target="_blank" rel="noopener">{t['cta']} {'←' if lang=='ar' else '→'}</a>
  </div>
</div>
<div class="prose narrow"><h2>{t['how_h']}</h2>{t['how']}<h2>{'Questions' if lang=='en' else 'أسئلة شائعة'}</h2></div>
<div class="faq narrow">{faq}</div>
<script>
(function(){{var T={json.dumps(js_t, ensure_ascii=False)},cur="{cur}";
function g(id){{var v=parseFloat(document.getElementById(id).value);return isFinite(v)?v:0}}
function f(n){{return n.toLocaleString('en-US',{{maximumFractionDigits:0}})}}
function set(id,v){{document.getElementById(id).textContent=v}}
function run(){{var s=g('spend'),fe=g('fees'),r=g('rev'),m=g('margin')/100,cost=s+fe,v=document.getElementById('o-v');v.classList.remove('warn');
 if(cost<=0){{['o-roi','o-p','o-roas','o-ber','o-beroas'].forEach(function(i){{set(i,'–')}});v.textContent='';return}}
 var p=r*m-cost,roi=p/cost*100;
 set('o-roi',(roi>0?'+':'')+roi.toFixed(0)+'%');set('o-p',f(p)+' '+cur);
 set('o-roas',s>0?(r/s).toFixed(2)+'x':'–');
 if(m>0){{set('o-ber',f(cost/m)+' '+cur);set('o-beroas',s>0?(cost/m/s).toFixed(2)+'x':'–')}}else{{set('o-ber','–');set('o-beroas','–')}}
 if(roi<0){{v.textContent=T.v_loss;v.classList.add('warn')}}else v.textContent=roi<50?T.v_thin:T.v_ok;
 var msg=T.wa.replace('{{s}}',f(s)).replace('{{r}}',f(r)).replace('{{roi}}',roi.toFixed(0)+'%');
 document.getElementById('o-wa').href='https://wa.me/966530570632?text='+encodeURIComponent(msg);}}
document.getElementById('calc').addEventListener('input',run);run();}})();
</script>'''
