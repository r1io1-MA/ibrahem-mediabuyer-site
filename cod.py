
import json
SLUG = 'cod-roas-calculator'

T = {
 'en': {
  'meta_title': 'COD ROAS calculator for Saudi stores | Ibrahem Muhamed',
  'desc': 'Free calculator: turn the ROAS your ad platform reports into the real ROAS after refused cash-on-delivery orders and failed-delivery shipping costs.',
  'kicker': 'Free tool',
  'title': 'Cash on delivery ROAS calculator',
  'card': 'Platform ROAS vs the real return after refused COD orders.',
  'lead': 'Ad platforms count a purchase at checkout. With cash on delivery, part of those orders never get paid. Enter your numbers and see the ROAS you actually earn.',
  'f': [('roas', 'ROAS shown in the ad platform', 'Snapchat, TikTok, Meta or Google', 'x', 4),
        ('aov', 'Average order value', 'Excluding VAT', 'SAR', 250),
        ('cod', 'Orders paid cash on delivery', 'Share of all orders', '%', 70),
        ('del', 'COD orders successfully delivered', 'From your courier report', '%', 75),
        ('fail', 'Cost of one failed delivery', 'Shipping out and back, per refused order', 'SAR', 30)],
  'big': 'Real ROAS', 'share': 'Revenue you actually collect', 'net': 'Real ROAS after failed-delivery costs',
  'lost': 'Orders lost per 100 placed', 'gap': 'Gap vs the platform number',
  'v_bad': 'The platform is overstating your return by a wide margin. Confirm orders before shipping and reward prepaying before you add budget.',
  'v_mid': 'A noticeable gap. Judge campaigns on this number, not the platform one, and track refusals by city and by ad.',
  'v_ok': 'Small gap. Your delivery rate is healthy, so the platform number is close to reality.',
  'cta': 'Send me these numbers',
  'wa': 'Hi Ibrahem, I used your COD calculator. Platform ROAS {p}, real ROAS {r}. Can we talk about my account?',
  'how_h': 'How it is calculated',
  'how': '<p><strong>Revenue collected</strong> = prepaid share + (COD share × delivery rate).</p><p><strong>Real ROAS</strong> = platform ROAS × revenue collected.</p><p><strong>After failed deliveries</strong>: ad spend per order = order value ÷ platform ROAS; the shipping cost of refused orders is taken off the revenue before dividing by that spend.</p><p>Read the full guide: <a href="/articles/cod-true-roas/">Cash on delivery is lying to your ROAS</a>.</p>',
  'faq': [('Where do I find my delivery rate?', 'In your courier or shipping-aggregator report: delivered COD orders divided by all COD orders shipped, over the last 60 to 90 days.'),
          ('Should I include orders cancelled before shipping?', 'Yes, if the ad platform counted them as purchases. They are part of the gap between what the platform reports and what you collect.'),
          ('What is a good delivery rate?', 'It depends on product, city and how you confirm orders, so compare against your own history rather than a general benchmark. What matters is that the real ROAS stays above your break-even ROAS.')],
 },
 'ar': {
  'meta_title': 'حاسبة ROAS الدفع عند الاستلام | إبراهيم محمد',
  'desc': 'حاسبة مجانية تحوّل الـROAS الذي تعرضه المنصة الإعلانية إلى العائد الحقيقي بعد الطلبات المرفوضة في الدفع عند الاستلام وتكلفة الشحن الفاشل.',
  'kicker': 'أداة مجانية',
  'title': 'حاسبة ROAS الدفع عند الاستلام',
  'card': 'عائد المنصة مقابل العائد الحقيقي بعد الطلبات المرفوضة.',
  'lead': 'المنصات تحسب الشراء لحظة الطلب، ومع الدفع عند الاستلام جزء من هذه الطلبات لا يُدفع أبدًا. أدخل أرقامك واعرف العائد الذي تحققه فعلًا.',
  'f': [('roas', 'الـROAS في المنصة الإعلانية', 'سناب شات أو تيك توك أو ميتا أو جوجل', 'x', 4),
        ('aov', 'متوسط قيمة الطلب', 'بدون الضريبة', 'ر.س', 250),
        ('cod', 'الطلبات بالدفع عند الاستلام', 'نسبة من كل الطلبات', '%', 70),
        ('del', 'طلبات الاستلام التي سُلّمت بنجاح', 'من تقرير شركة الشحن', '%', 75),
        ('fail', 'تكلفة الطلب المرفوض', 'شحن الذهاب والعودة للطلب الواحد', 'ر.س', 30)],
  'big': 'الـROAS الحقيقي', 'share': 'نسبة الإيراد الذي تحصّله فعلًا', 'net': 'الـROAS الحقيقي بعد تكلفة الشحن الفاشل',
  'lost': 'طلبات تضيع من كل 100 طلب', 'gap': 'الفرق عن رقم المنصة',
  'v_bad': 'المنصة تبالغ في عائدك بفارق كبير. أكّد الطلبات قبل الشحن وشجّع الدفع المسبق قبل أن تزيد الميزانية.',
  'v_mid': 'فارق ملحوظ. احكم على الحملات بهذا الرقم لا برقم المنصة، وتابع الرفض حسب المدينة والإعلان.',
  'v_ok': 'فارق بسيط. نسبة التسليم عندك جيدة، فرقم المنصة قريب من الواقع.',
  'cta': 'أرسل لي هذه الأرقام',
  'wa': 'مرحبًا إبراهيم، استخدمت حاسبة الدفع عند الاستلام. ROAS المنصة {p} والعائد الحقيقي {r}. أرغب في مناقشة حسابي.',
  'how_h': 'طريقة الحساب',
  'how': '<p><strong>الإيراد المحصّل</strong> = نسبة الدفع المسبق + (نسبة الدفع عند الاستلام × نسبة التسليم).</p><p><strong>الـROAS الحقيقي</strong> = ROAS المنصة × الإيراد المحصّل.</p><p><strong>بعد الشحن الفاشل</strong>: الإنفاق الإعلاني لكل طلب = قيمة الطلب ÷ ROAS المنصة، وتُخصم تكلفة شحن الطلبات المرفوضة من الإيراد قبل القسمة على هذا الإنفاق.</p><p>اقرأ الدليل كاملًا: <a href="/ar/articles/cod-true-roas/">الدفع عند الاستلام يخدعك</a>.</p>',
  'faq': [('من أين أعرف نسبة التسليم؟', 'من تقرير شركة الشحن أو منصة الشحن: طلبات الاستلام التي سُلّمت ÷ كل طلبات الاستلام التي شُحنت، خلال آخر 60 إلى 90 يومًا.'),
          ('هل أحسب الطلبات الملغاة قبل الشحن؟', 'نعم إذا كانت المنصة الإعلانية قد حسبتها كعمليات شراء، فهي جزء من الفرق بين ما تعرضه المنصة وما تحصّله.'),
          ('ما نسبة التسليم الجيدة؟', 'تختلف حسب المنتج والمدينة وطريقة تأكيد الطلب، لذا قارن بتاريخك أنت لا برقم عام. المهم أن يبقى الـROAS الحقيقي أعلى من ROAS التعادل.')],
 },
}

def body(lang):
    t = T[lang]; ar = lang == 'ar'
    fields = ''.join(
        f'<label for="{k}">{lab}<small>{hint}</small><span class="inp"><input id="{k}" type="number" inputmode="decimal" min="0" step="any" value="{dv}"><span>{unit}</span></span></label>'
        for k, lab, hint, unit, dv in t['f'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq'])
    js_t = {k: t[k] for k in ['v_bad', 'v_mid', 'v_ok', 'wa']}
    return f'''
<div class="calc">
  <form id="calc" onsubmit="return false">{fields}</form>
  <div class="out" aria-live="polite">
    <span class="label">{t['big']}</span>
    <div class="big mono" id="o-r">–</div>
    <div class="row"><span>{t['share']}</span><b id="o-s">–</b></div>
    <div class="row"><span>{t['net']}</span><b id="o-n">–</b></div>
    <div class="row"><span>{t['lost']}</span><b id="o-l">–</b></div>
    <div class="row"><span>{t['gap']}</span><b id="o-g">–</b></div>
    <p class="verdict" id="o-v"></p>
    <a class="btn primary" id="o-wa" href="https://wa.me/966530570632" target="_blank" rel="noopener">{t['cta']} {'←' if ar else '→'}</a>
  </div>
</div>
<div class="prose narrow"><h2>{t['how_h']}</h2>{t['how']}<h2>{'أسئلة شائعة' if ar else 'Questions'}</h2></div>
<div class="faq narrow">{faq}</div>
<script>
(function(){{var T={json.dumps(js_t, ensure_ascii=False)};
function g(id){{var v=parseFloat(document.getElementById(id).value);return isFinite(v)?v:0}}
function set(id,v){{document.getElementById(id).textContent=v}}
function run(){{var p=g('roas'),a=g('aov'),c=Math.min(100,g('cod'))/100,d=Math.min(100,g('del'))/100,fc=g('fail'),v=document.getElementById('o-v');v.classList.remove('warn');
 if(p<=0||a<=0){{['o-r','o-s','o-n','o-l','o-g'].forEach(function(i){{set(i,'–')}});v.textContent='';return}}
 var share=(1-c)+c*d,real=p*share,spend=a/p,net=(a*share-c*(1-d)*fc)/spend,lost=c*(1-d)*100,gap=(1-net/p)*100;
 set('o-r',real.toFixed(2)+'x');set('o-s',(share*100).toFixed(1)+'%');set('o-n',net.toFixed(2)+'x');set('o-l',lost.toFixed(1));set('o-g','-'+gap.toFixed(0)+'%');
 if(gap>=20){{v.textContent=T.v_bad;v.classList.add('warn')}}else v.textContent=gap>=8?T.v_mid:T.v_ok;
 document.getElementById('o-wa').href='https://wa.me/966530570632?text='+encodeURIComponent(T.wa.replace('{{p}}',p.toFixed(2)+'x').replace('{{r}}',net.toFixed(2)+'x'));}}
document.getElementById('calc').addEventListener('input',run);run();}})();
</script>'''
