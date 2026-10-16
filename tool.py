
TOOL_SLUG = 'break-even-roas'

T = {
 'en': {
  'meta_title': 'Break-even ROAS calculator for Saudi e-commerce stores | Ibrahem Muhamed',
  'desc': 'Free calculator: find the minimum ROAS and the maximum cost per order your store can afford on Snapchat, TikTok, Meta or Google before ads start losing money.',
  'kicker': 'Free tool',
  'title': 'Break-even ROAS calculator',
  'card': 'The lowest ROAS your margins can survive, and the most you can pay per order.',
  'lead': 'Enter one order\'s numbers and see the lowest ROAS your ads can run at without losing money, and the ROAS you need to hit your profit goal.',
  'f': [('price', 'Average order value', 'Excluding VAT', 'SAR', 250),
        ('cost', 'Product cost per order', 'What the goods cost you', 'SAR', 90),
        ('ship', 'Shipping & packaging per order', 'Including COD or delivery fees you pay', 'SAR', 25),
        ('fee', 'Payment & platform fees', 'Percent of the order value', '%', 3),
        ('goal', 'Profit you want to keep', 'Percent of the order value, after ads', '%', 10)],
  'be': 'Break-even ROAS', 'be_cpa': 'Max cost per order (break even)', 'margin': 'Profit per order before ads',
  'tg': 'ROAS for your profit goal', 'tg_cpa': 'Max cost per order (with your goal)',
  'v_loss': 'This order loses money before any ads. Fix the price, the product cost or shipping first: no ROAS can save it.',
  'v_goal': 'Your profit goal is larger than the margin. Lower the goal or raise the order value.',
  'v_hi': 'Your margin is thin. Ads need to work very hard here. Bundles, a higher order value or cheaper shipping will help more than any campaign tweak.',
  'v_mid': 'Workable. Most well-run Saudi stores can hold this on their stronger channels, with retargeting and good creative.',
  'v_lo': 'Comfortable margin. You have room to scale and to test new channels.',
  'cta': 'Send me these numbers',
  'wa': 'Hi Ibrahem, I used your break-even calculator. Order value {p} SAR, break-even ROAS {be}, target ROAS {tg}. Can we talk about my account?',
  'how_h': 'How it is calculated',
  'how': '<p><strong>Profit per order before ads</strong> = order value − product cost − shipping − (order value × fees %).</p><p><strong>Break-even ROAS</strong> = order value ÷ profit per order before ads. At this ROAS the ads eat the whole margin and you make zero.</p><p><strong>Target ROAS</strong> = order value ÷ (profit per order − order value × profit goal %).</p>',
  'faq': [('What is break-even ROAS?', 'The return on ad spend at which your ads cost exactly what one order earns you after product, shipping and fees. Below it every sale loses money; above it you start keeping profit.'),
          ('Should I include VAT in the order value?', 'No. Enter the price without the 15% VAT, because VAT is collected for the government and is not your revenue. Ad platforms often report revenue including VAT, which makes ROAS look better than it is.'),
          ('Why does the ad platform show a higher ROAS than my store makes?', 'Each platform credits itself for any sale it touched, so the same order can be counted twice. Check MER as well: total store revenue ÷ total ad spend. If MER is below your break-even ROAS, the account is losing money whatever the dashboards say.'),
          ('What about returns and cancelled orders?', 'If, for example, 10% of orders are returned or cancelled, lower the order value by 10% before you calculate, or add the cost of returns to shipping.')],
 },
 'ar': {
  'meta_title': 'حاسبة ROAS التعادل لمتاجر التجارة الإلكترونية في السعودية | إبراهيم محمد',
  'desc': 'حاسبة مجانية تعرف بها أقل عائد إعلاني (ROAS) وأعلى تكلفة للطلب يتحملها متجرك على سناب شات وتيك توك وميتا وجوجل قبل أن تبدأ الإعلانات بالخسارة.',
  'kicker': 'أداة مجانية',
  'title': 'حاسبة ROAS التعادل',
  'card': 'أقل عائد يتحمله هامش ربحك، وأعلى تكلفة يمكنك دفعها للطلب.',
  'lead': 'أدخل أرقام طلب واحد، وستعرف أقل عائد يمكن أن تعمل عليه إعلاناتك دون خسارة، والعائد الذي تحتاجه لتحقيق الربح الذي تريده.',
  'f': [('price', 'متوسط قيمة الطلب', 'بدون ضريبة القيمة المضافة', 'ر.س', 250),
        ('cost', 'تكلفة المنتج في الطلب', 'ما تدفعه أنت في البضاعة', 'ر.س', 90),
        ('ship', 'الشحن والتغليف للطلب', 'بما فيها رسوم الدفع عند الاستلام إن وُجدت', 'ر.س', 25),
        ('fee', 'رسوم الدفع والمنصة', 'نسبة من قيمة الطلب', '%', 3),
        ('goal', 'الربح الذي تريد الاحتفاظ به', 'نسبة من قيمة الطلب بعد الإعلانات', '%', 10)],
  'be': 'ROAS التعادل', 'be_cpa': 'أعلى تكلفة للطلب (نقطة التعادل)', 'margin': 'ربح الطلب قبل الإعلانات',
  'tg': 'ROAS لتحقيق هدف الربح', 'tg_cpa': 'أعلى تكلفة للطلب (مع هدف الربح)',
  'v_loss': 'هذا الطلب خاسر قبل أي إعلان. راجع السعر أو تكلفة المنتج أو الشحن أولًا، فلا يوجد عائد إعلاني ينقذه.',
  'v_goal': 'هدف الربح أكبر من هامش الطلب. خفّض الهدف أو ارفع قيمة الطلب.',
  'v_hi': 'هامشك ضيق، والإعلانات هنا تحتاج مجهودًا كبيرًا. الباقات ورفع قيمة السلة وتقليل تكلفة الشحن ستفيدك أكثر من أي تعديل في الحملات.',
  'v_mid': 'رقم قابل للتحقيق. أغلب المتاجر السعودية المُدارة جيدًا تحافظ عليه في قنواتها الأقوى مع إعادة الاستهداف ومحتوى إعلاني جيد.',
  'v_lo': 'هامش مريح، ولديك مساحة للتوسع واختبار قنوات جديدة.',
  'cta': 'أرسل لي هذه الأرقام',
  'wa': 'مرحبًا إبراهيم، استخدمت حاسبة التعادل. قيمة الطلب {p} ريال، وROAS التعادل {be}، والمستهدف {tg}. أرغب في مناقشة حسابي.',
  'how_h': 'طريقة الحساب',
  'how': '<p><strong>ربح الطلب قبل الإعلانات</strong> = قيمة الطلب − تكلفة المنتج − الشحن − (قيمة الطلب × نسبة الرسوم).</p><p><strong>ROAS التعادل</strong> = قيمة الطلب ÷ ربح الطلب قبل الإعلانات. عند هذا العائد تستهلك الإعلانات الهامش كله ويكون ربحك صفرًا.</p><p><strong>ROAS المستهدف</strong> = قيمة الطلب ÷ (ربح الطلب − قيمة الطلب × نسبة هدف الربح).</p>',
  'faq': [('ما هو ROAS التعادل؟', 'هو العائد على الإنفاق الإعلاني الذي تتساوى عنده تكلفة الإعلان مع ما يربحه الطلب بعد المنتج والشحن والرسوم. تحته يخسر كل طلب، وفوقه يبدأ الربح.'),
          ('هل أُدخل قيمة الطلب شاملة الضريبة؟', 'لا. أدخل السعر بدون ضريبة القيمة المضافة (15%)، لأن الضريبة تُحصَّل للدولة وليست إيرادًا لك. وكثير من المنصات الإعلانية تعرض الإيراد شاملًا الضريبة، فيبدو العائد أفضل من حقيقته.'),
          ('لماذا تعرض المنصة عائدًا أعلى مما يحققه متجري؟', 'كل منصة تنسب لنفسها أي عملية بيع لمستها، فقد يُحسب الطلب نفسه مرتين. لذلك تابع أيضًا MER: إجمالي إيراد المتجر ÷ إجمالي الإنفاق الإعلاني. وإذا كان MER أقل من ROAS التعادل فالحساب خاسر مهما قالت اللوحات.'),
          ('وماذا عن المرتجعات والطلبات الملغاة؟', 'إذا كانت مثلًا 10% من الطلبات تُرجع أو تُلغى، فاخصم 10% من قيمة الطلب قبل الحساب، أو أضف تكلفة المرتجعات إلى الشحن.')],
 },
}

def body(lang):
    t = T[lang]
    fields = ''.join(
        f'<label for="{k}">{lab}<small>{hint}</small><span class="inp"><input id="{k}" type="number" inputmode="decimal" min="0" step="any" value="{dv}"><span>{unit}</span></span></label>'
        for k, lab, hint, unit, dv in t['f'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq'])
    js_t = {k: t[k] for k in ['v_loss', 'v_goal', 'v_hi', 'v_mid', 'v_lo', 'wa']}
    import json
    return f'''
<div class="calc">
  <form id="calc" onsubmit="return false">{fields}</form>
  <div class="out" aria-live="polite">
    <span class="label">{t['be']}</span>
    <div class="big mono" id="o-be">–</div>
    <div class="row"><span>{t['margin']}</span><b id="o-m">–</b></div>
    <div class="row"><span>{t['be_cpa']}</span><b id="o-bcpa">–</b></div>
    <div class="row"><span>{t['tg']}</span><b id="o-tg">–</b></div>
    <div class="row"><span>{t['tg_cpa']}</span><b id="o-tcpa">–</b></div>
    <p class="verdict" id="o-v"></p>
    <a class="btn primary" id="o-wa" href="https://wa.me/966530570632" target="_blank" rel="noopener">{t['cta']} {'←' if lang=='ar' else '→'}</a>
  </div>
</div>
<div class="prose narrow"><h2>{t['how_h']}</h2>{t['how']}<h2>{'Questions' if lang=='en' else 'أسئلة شائعة'}</h2></div>
<div class="faq narrow">{faq}</div>
<script>
(function(){{var T={json.dumps(js_t, ensure_ascii=False)},cur="{'SAR' if lang=='en' else 'ر.س'}";
function g(id){{var v=parseFloat(document.getElementById(id).value);return isFinite(v)?v:0}}
function f(n){{return n.toLocaleString('en-US',{{maximumFractionDigits:2,minimumFractionDigits:2}})}}
function set(id,v){{document.getElementById(id).textContent=v}}
function run(){{var p=g('price'),c=g('cost'),s=g('ship'),fe=g('fee'),go=g('goal');
 var m=p-c-s-p*fe/100,al=m-p*go/100,v=document.getElementById('o-v');v.classList.remove('warn');
 set('o-m',f(m)+' '+cur);
 if(p<=0||m<=0){{set('o-be','–');set('o-bcpa','–');set('o-tg','–');set('o-tcpa','–');v.textContent=T.v_loss;v.classList.add('warn');return}}
 var be=p/m;set('o-be',be.toFixed(2)+'x');set('o-bcpa',f(m)+' '+cur);
 var tg=null;if(al>0){{tg=p/al;set('o-tg',tg.toFixed(2)+'x');set('o-tcpa',f(al)+' '+cur);}}else{{set('o-tg','–');set('o-tcpa','–');}}
 if(al<=0){{v.textContent=T.v_goal;v.classList.add('warn')}}else v.textContent=be>=4?T.v_hi:be>=2.2?T.v_mid:T.v_lo;
 var msg=T.wa.replace('{{p}}',f(p)).replace('{{be}}',be.toFixed(2)+'x').replace('{{tg}}',tg?tg.toFixed(2)+'x':'–');
 document.getElementById('o-wa').href='https://wa.me/966530570632?text='+encodeURIComponent(msg);}}
document.getElementById('calc').addEventListener('input',run);run();}})();
</script>'''
