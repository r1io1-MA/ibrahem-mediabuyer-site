
# Case study content, EN + AR. Figures match the homepage and the screenshots.
def kpis(items):
    return '<div class="kpis">' + ''.join(f'<div><b><bdi>{a}</bdi></b><span>{b}</span></div>' for a, b in items) + '</div>'

def bars(rows, mx):
    out = '<div class="bars">'
    for name, val, label in rows:
        out += f'<div class="r"><span>{name}</span><span class="t"><i style="width:{val/mx*100:.1f}%"></i></span><span class="v"><bdi>{label}</bdi></span></div>'
    return out + '</div>'

def shots(items, lang):
    out = '<div class="shots">'
    for img, cap in items:
        out += f'<figure><a href="/img/{img}.webp" target="_blank" rel="noopener"><img src="/img/{img}.webp" alt="{cap}" loading="lazy" width="1600" height="900"></a><figcaption>{cap}</figcaption></figure>'
    nda = ('Names and dates are hidden under client NDAs. Figures are unedited.' if lang == 'en'
           else 'الأسماء والتواريخ مخفية التزامًا باتفاقيات السرية مع العملاء، والأرقام كما هي دون تعديل.')
    return out + f'</div><p class="nda">🔒 {nda}</p>'

CASES = [
 {
  'slug': 'edtech-251-percent-of-target',
  'en': {
   'kicker': 'Case 01 · EdTech · digital product · KSA',
   'card': 'SAR 1.1M delivered against a SAR 444K monthly target, Snapchat-led.',
   'title': '251% of the monthly revenue target for an online English-learning brand',
   'meta_title': 'EdTech case study: 251% of revenue target | Ibrahem Muhamed',
   'desc': 'How a Snapchat-led plan delivered about SAR 1.1M against a SAR 444K monthly target for an online English-learning brand in KSA, at 4.49x ROAS on $66.2K.',
   'lead': 'Online English courses for Saudi families and adults, sold through a web checkout. The month stacked two seasons, back-to-school and Saudi National Day, against a revenue target of SAR 444,000.',
   'body': lambda: (
     kpis([('251%', 'of the monthly revenue target'), ('4.49x', 'Snapchat purchase ROAS on $66.2K spend'),
           ('2,862', 'purchases from Snapchat in one month'), ('$23.1', 'cost per purchase')]) +
     '<div class="prose narrow">'
     '<h2>The starting point</h2>'
     '<p>When I took the account, Snapchat was returning <strong>1.88x</strong> and TikTok <strong>1.69x</strong>. Half of all revenue sat under "Direct" in analytics because of UTM gaps, so nobody could say which channel was actually selling. Scaling on that data would have meant scaling blind.</p>'
     '<h2>What I did</h2><ol class="steps">'
     '<li><b>Fixed attribution before raising spend.</b>Rebuilt UTMs for every channel and every creator link, so revenue landed on the channel that earned it.</li>'
     '<li><b>Split the month into two jobs.</b>The first half sold a "catch-up" angle to parents after the first school tests. The second half used National Day for reach, then converted that audience with retargeting.</li>'
     '<li><b>Tested 33 creators as ad inventory.</b>One creator per ad set beside a standard-creative ad set, on ad-set budgets, so winners showed within days and losers were cut early.</li>'
     '<li><b>Cleaned the audience map.</b>Prospecting, lookalike and retargeting audiences that do not overlap, with purchasers excluded, so ad sets stopped bidding against each other.</li>'
     '<li><b>Automated the lead side.</b>Snapchat lead forms feed a shared sheet and alert the call-center team in real time, with ads scheduled to call-center hours.</li></ol>'
     '<h2>ROAS by channel, before and after</h2>' +
     bars([('Snapchat · start', 1.88, '1.88x'), ('Snapchat · month 2', 3.34, '3.34x'), ('Snapchat · peak', 6.1, '6.1x'),
           ('TikTok · start', 1.69, '1.69x'), ('TikTok · restructure', 5.28, '5.28x'), ('TikTok · launch', 8.58, '8.58x')], 8.6) +
     '<p>On TikTok, monthly spend went from $10.5K to $22.3K (2.1x more) while ROAS rose from 4.47x to 4.82x and purchases doubled from 552 to 1,111.</p>'
     '<h2>Reading Google honestly</h2>'
     '<p>The Google account showed a blended <strong>10.5x</strong>. That number was inflated by brand searches that would have converted anyway: <strong>74%</strong> of reported value came from one brand-protection campaign on 16% of spend. With brand removed, non-brand ROAS was <strong>3.2x</strong>, and budgets were set on that number. I reported the two separately so management could see what Google actually acquired.</p>'
     '<div class="callout">The lesson that carries to any account: decide on the number that would disappear if you switched the ads off, not on the number the platform is happy to report.</div>'
     '<h2>Screenshots from the ad accounts</h2></div>' +
     shots([('edtech-snapchat-scale', 'Snapchat: 4.49x ROAS on $66.2K in one month'),
            ('edtech-tiktok-peak', 'TikTok: 4.82x ROAS, 1,111 purchases'),
            ('edtech-tiktok-september', 'TikTok: 8.58x ROAS in the first 3 days of the season'),
            ('edtech-google-brand-protection', 'Google: brand protection reported separately')], 'en'))
  },
  'ar': {
   'kicker': 'دراسة حالة 01 · تعليم إلكتروني · منتج رقمي · السعودية',
   'card': 'نحو 1.1 مليون ريال مقابل مستهدف شهري 444 ألف ريال، بقيادة سناب شات.',
   'title': 'تحقيق 251% من المستهدف الشهري لمنصة تعليم إنجليزي عبر الإنترنت',
   'meta_title': 'دراسة حالة: 251% من المستهدف لمنصة تعليمية | إبراهيم محمد',
   'desc': 'كيف حققت خطة يقودها سناب شات نحو 1.1 مليون ريال مقابل مستهدف شهري 444 ألف ريال لمنصة تعليم إنجليزي في السعودية، بعائد 4.49x على إنفاق 66.2 ألف دولار.',
   'lead': 'دورات إنجليزي عبر الإنترنت للأسر والبالغين في السعودية، تُباع من خلال صفحة دفع على الموقع. جمع الشهر موسمين معًا: العودة إلى المدارس واليوم الوطني، والمستهدف 444,000 ريال.',
   'body': lambda: (
     kpis([('251%', 'من المستهدف الشهري للإيرادات'), ('4.49x', 'عائد سناب شات على إنفاق 66.2 ألف دولار'),
           ('2,862', 'عملية شراء من سناب شات خلال شهر'), ('$23.1', 'تكلفة عملية الشراء')]) +
     '<div class="prose narrow">'
     '<h2>نقطة البداية</h2>'
     '<p>عند استلام الحساب كان عائد سناب شات <strong><bdi>1.88x</bdi></strong> وتيك توك <strong><bdi>1.69x</bdi></strong>. وكان نصف الإيرادات يظهر تحت بند "مباشر" في التحليلات بسبب ثغرات في روابط UTM، فلم يكن أحد يعرف أي قناة تبيع فعلًا. ورفع الميزانية على هذه البيانات كان يعني التوسع دون رؤية.</p>'
     '<h2>ما الذي فعلته</h2><ol class="steps">'
     '<li><b>أصلحت قياس المصادر قبل رفع الإنفاق.</b>أعدت بناء روابط UTM لكل قناة ولكل رابط صانع محتوى، لتُنسب الإيرادات إلى القناة التي حققتها.</li>'
     '<li><b>قسّمت الشهر إلى مهمتين.</b>النصف الأول خاطب أولياء الأمور بفكرة "تعويض المستوى" بعد أول اختبارات مدرسية، والنصف الثاني استثمر اليوم الوطني للوصول ثم حوّل هذا الجمهور إلى مشترين بإعادة الاستهداف.</li>'
     '<li><b>اختبرت 33 صانع محتوى كمخزون إعلاني.</b>صانع محتوى واحد في كل مجموعة إعلانية بجانب مجموعة بالإعلانات المعتادة، بميزانية على مستوى المجموعة، فظهر الرابحون خلال أيام وأُوقف الخاسرون مبكرًا.</li>'
     '<li><b>رتّبت خريطة الجماهير.</b>جماهير استكشاف ومشابهة وإعادة استهداف لا تتداخل، مع استبعاد من اشتروا، حتى تتوقف المجموعات عن المزايدة ضد بعضها.</li>'
     '<li><b>أتمتة جانب العملاء المحتملين.</b>نماذج سناب شات تُرسل البيانات إلى جدول مشترك وتنبّه فريق الاتصال فورًا، مع جدولة الإعلانات على ساعات عمل الفريق.</li></ol>'
     '<h2>العائد حسب القناة قبل وبعد</h2>' +
     bars([('سناب · البداية', 1.88, '1.88x'), ('سناب · الشهر الثاني', 3.34, '3.34x'), ('سناب · الذروة', 6.1, '6.1x'),
           ('تيك توك · البداية', 1.69, '1.69x'), ('تيك توك · بعد الهيكلة', 5.28, '5.28x'), ('تيك توك · الإطلاق', 8.58, '8.58x')], 8.6) +
     '<p>في تيك توك ارتفع الإنفاق الشهري من <bdi>$10.5K</bdi> إلى <bdi>$22.3K</bdi> (أكثر بـ<bdi>2.1</bdi> مرة)، وفي الوقت نفسه ارتفع العائد من <bdi>4.47x</bdi> إلى <bdi>4.82x</bdi> وتضاعفت المشتريات من <bdi>552</bdi> إلى <bdi>1,111</bdi>.</p>'
     '<h2>قراءة جوجل بأمانة</h2>'
     '<p>أظهر حساب جوجل عائدًا إجماليًا <strong><bdi>10.5x</bdi></strong>، لكنه رقم مضخّم بعمليات بحث عن اسم العلامة كانت ستتحول إلى شراء في كل الأحوال: <strong><bdi>74%</bdi></strong> من القيمة المسجلة جاءت من حملة حماية اسم العلامة على <bdi>16%</bdi> فقط من الإنفاق. وبعد استبعادها كان العائد الحقيقي <strong><bdi>3.2x</bdi></strong>، وعلى هذا الرقم حُددت الميزانيات. وعرضت الرقمين منفصلين حتى ترى الإدارة ما جلبه جوجل فعلًا.</p>'
     '<div class="callout">الدرس الذي ينطبق على أي حساب: اتخذ قرارك على الرقم الذي سيختفي لو أوقفت الإعلانات، لا على الرقم الذي تحب المنصة أن تعرضه.</div>'
     '<h2>لقطات من الحسابات الإعلانية</h2></div>' +
     shots([('edtech-snapchat-scale', 'سناب شات: عائد 4.49x على إنفاق 66.2 ألف دولار خلال شهر'),
            ('edtech-tiktok-peak', 'تيك توك: عائد 4.82x و1,111 عملية شراء'),
            ('edtech-tiktok-september', 'تيك توك: عائد 8.58x في أول 3 أيام من الموسم'),
            ('edtech-google-brand-protection', 'جوجل: حملة حماية اسم العلامة معروضة منفصلة')], 'ar'))
  }
 },
 {
  'slug': 'ecommerce-882-orders',
  'en': {
   'kicker': 'Case 02 · Fragrance · e-commerce · KSA',
   'card': '882 orders against a 500-order target on $11.5K of paid media.',
   'title': '882 orders against a 500-order target, on $11.5K of paid media',
   'meta_title': 'E-commerce case study: 882 orders vs 500 | Ibrahem Muhamed',
   'desc': 'A Saudi perfume store hit 882 orders against a 500 target with 8.6x MER. Tracking rebuilt first, Snapchat for volume, one Instagram campaign at 12.38x ROAS.',
   'lead': 'A Saudi perfume store. I rebuilt tracking from scratch (GTM, GA4, Snapchat and Meta pixels) before buying media, so every platform number could be checked against the store\'s own orders.',
   'body': lambda: (
     kpis([('176%', 'of the monthly order target (882 / 500)'), ('8.6x', 'MER: store revenue ÷ total paid spend'),
           ('6.63x', 'Snapchat ROAS · 591 purchases'), ('12.38x', 'Instagram campaign ROAS · 125 purchases')]) +
     '<div class="prose narrow">'
     '<h2>Why tracking came first</h2>'
     '<p>The store was still running a dead Universal Analytics setup, so there was no reliable way to compare what the ad platforms claimed with what the store actually sold. I replaced it with GA4 and clean purchase events on both ad platforms before spending, and the 500-order target was set and tracked inside the store dashboard.</p>'
     '<h2>What I did</h2><ol class="steps">'
     '<li><b>Rebuilt tracking before spending.</b>GTM, GA4, and purchase events on the Snapchat and Meta pixels, checked against store orders.</li>'
     '<li><b>Made Snapchat the volume channel.</b>4.77M impressions at about $2.2 CPM, returning 6.63x on $10.4K.</li>'
     '<li><b>Kept Meta narrow.</b>One always-on Instagram sales campaign on a small budget returned 12.38x at $9.4 per purchase.</li>'
     '<li><b>Reported on store orders, not platform claims.</b>MER (store revenue ÷ all paid spend) was the headline number, not any single platform\'s ROAS.</li></ol>'
     '<h2>Where the month\'s revenue came from</h2>' +
     bars([('Snapchat', 68.7, '$68.7K'), ('Meta', 14.6, '$14.6K'), ('Organic & repeat', 16.3, '$16.3K')], 70) +
     '<p>Platform-attributed revenue, checked against the store total of about $99.6K. The store converted 1.40% of 64,970 visits.</p>'
     '<div class="callout">MER is the number a store owner can trust: it only uses what the store sold and what you spent. If MER and platform ROAS disagree, MER wins.</div>'
     '<h2>Screenshots from the ad accounts</h2></div>' +
     shots([('fragrance-snapchat', 'Snapchat: 6.63x ROAS, 591 purchases'),
            ('fragrance-meta', 'Meta: 12.38x ROAS, 125 purchases')], 'en'))
  },
  'ar': {
   'kicker': 'دراسة حالة 02 · عطور · تجارة إلكترونية · السعودية',
   'card': '882 طلبًا مقابل مستهدف 500 طلب بإنفاق إعلاني 11.5 ألف دولار.',
   'title': '882 طلبًا مقابل مستهدف 500 طلب، بإنفاق إعلاني 11.5 ألف دولار',
   'meta_title': 'دراسة حالة: 882 طلبًا مقابل مستهدف 500 | إبراهيم محمد',
   'desc': 'متجر عطور سعودي حقق 882 طلبًا مقابل مستهدف 500 بمعدل MER يبلغ 8.6x: إعادة بناء التتبع أولًا، وسناب شات للحجم، وحملة إنستجرام واحدة بعائد 12.38x.',
   'lead': 'متجر عطور سعودي. أعدت بناء التتبع من الصفر (GTM وGA4 وبكسل سناب شات وميتا) قبل أي إنفاق، حتى يمكن مطابقة كل رقم في المنصات مع طلبات المتجر نفسه.',
   'body': lambda: (
     kpis([('176%', 'من مستهدف الطلبات الشهري (882 / 500)'), ('8.6x', 'MER: إيراد المتجر ÷ إجمالي الإنفاق'),
           ('6.63x', 'عائد سناب شات · 591 عملية شراء'), ('12.38x', 'عائد حملة إنستجرام · 125 عملية شراء')]) +
     '<div class="prose narrow">'
     '<h2>لماذا بدأنا بالتتبع</h2>'
     '<p>كان المتجر يعمل على إعداد قديم ومتوقف من Universal Analytics، فلم تكن هناك طريقة موثوقة لمقارنة ما تقوله المنصات الإعلانية بما باعه المتجر فعلًا. استبدلته بـGA4 وأحداث شراء سليمة على المنصتين قبل الإنفاق، وحُدد مستهدف الـ500 طلب وتُوبع من لوحة تحكم المتجر نفسها.</p>'
     '<h2>ما الذي فعلته</h2><ol class="steps">'
     '<li><b>بنيت التتبع قبل الإنفاق.</b>GTM وGA4 وأحداث الشراء على بكسل سناب شات وميتا، مع مطابقتها بطلبات المتجر.</li>'
     '<li><b>جعلت سناب شات قناة الحجم.</b><bdi>4.77M</bdi> ظهور بتكلفة ألف ظهور تقارب <bdi>$2.2</bdi>، وعائد <bdi>6.63x</bdi> على إنفاق <bdi>$10.4K</bdi>.</li>'
     '<li><b>أبقيت ميتا محدودة.</b>حملة مبيعات واحدة دائمة على إنستجرام بميزانية صغيرة حققت <bdi>12.38x</bdi> بتكلفة <bdi>$9.4</bdi> للشراء.</li>'
     '<li><b>التقارير على طلبات المتجر لا على أرقام المنصات.</b>الرقم الرئيسي كان MER (إيراد المتجر ÷ كل الإنفاق الإعلاني)، لا عائد منصة بعينها.</li></ol>'
     '<h2>مصادر إيرادات الشهر</h2>' +
     bars([('سناب شات', 68.7, '$68.7K'), ('ميتا', 14.6, '$14.6K'), ('عضوي وتكرار', 16.3, '$16.3K')], 70) +
     '<p>إيرادات منسوبة للمنصات ومطابَقة مع إجمالي المتجر البالغ نحو <bdi>$99.6K</bdi>. وبلغ معدل تحويل المتجر <bdi>1.40%</bdi> من <bdi>64,970</bdi> زيارة.</p>'
     '<div class="callout">MER هو الرقم الذي يثق فيه صاحب المتجر، لأنه لا يعتمد إلا على ما باعه المتجر وما أنفقته. وإذا اختلف مع عائد المنصة فالكلمة لـMER.</div>'
     '<h2>لقطات من الحسابات الإعلانية</h2></div>' +
     shots([('fragrance-snapchat', 'سناب شات: عائد 6.63x و591 عملية شراء'),
            ('fragrance-meta', 'ميتا: عائد 12.38x و125 عملية شراء')], 'ar'))
  }
 },
 {
  'slug': 'b2b-snapchat-leads',
  'en': {
   'kicker': 'Case 03 · B2B lead generation · Snapchat · KSA',
   'card': '636 leads, 70% closed by sales, SAR 260K from $1.1K in media.',
   'title': '636 leads, 70% closed by sales, SAR 260K in revenue from $1.1K in media',
   'meta_title': 'B2B Snapchat leads case study | Ibrahem Muhamed',
   'desc': 'Snapchat lead forms for a Saudi B2B sales team: 636 leads at $1.73, 70% closed in the CRM, SAR 260K revenue on $1.1K in media.',
   'lead': 'Snapchat lead-form campaigns feeding a sales team. Success was measured on deals closed in the CRM, not on lead volume or cost per lead.',
   'body': lambda: (
     kpis([('70%', 'of leads closed, per the CRM'), ('63x', 'closed revenue ÷ media spend'),
           ('$1.73', 'average cost per lead'), ('$2.47', 'media cost per closed deal')]) +
     '<div class="prose narrow">'
     '<h2>What I did</h2><ol class="steps">'
     '<li><b>Ran two campaigns and kept what worked.</b>Cost per lead fell from $2.73 in the first campaign to $1.14 in the second (−58%), on $1.1K in total spend.</li>'
     '<li><b>Used Snapchat\'s native lead forms.</b>Leads were captured inside the app, without sending people to a landing page first.</li>'
     '<li><b>Judged the campaign on CRM closes.</b>70% of leads became sales, so a cheap lead here was also a qualified one.</li></ol>'
     '<h2>From impression to closed deal</h2>' +
     bars([('Impressions', 100, '329,756'), ('Leads', 60, '636'), ('Closed deals', 45, '≈ 445'), ('Revenue', 35, 'SAR 260K')], 100) +
     '<p>Bars show funnel stages, not scale. Lead and spend figures come from Snapchat Ads Manager; closed deals and revenue come from the client\'s CRM.</p>'
     '<div class="callout">Cost per lead only matters next to close rate. A $1.73 lead that closes 70% of the time beats a $0.80 lead nobody answers.</div>'
     '<h2>Screenshot from the ad account</h2></div>' +
     shots([('leads-snapchat', 'Snapchat: 636 leads at $1.73 each')], 'en'))
  },
  'ar': {
   'kicker': 'دراسة حالة 03 · عملاء محتملون B2B · سناب شات · السعودية',
   'card': '636 عميلًا محتملًا، أُغلق 70% منهم، و260 ألف ريال من إنفاق 1.1 ألف دولار.',
   'title': '636 عميلًا محتملًا، 70% منهم تحولوا إلى صفقات، و260 ألف ريال من إنفاق 1.1 ألف دولار',
   'meta_title': 'دراسة حالة: عملاء B2B عبر سناب شات | إبراهيم محمد',
   'desc': 'نماذج عملاء سناب شات لفريق مبيعات B2B في السعودية: 636 عميلًا محتملًا بتكلفة 1.73 دولار، وإغلاق 70% في نظام CRM، و260 ألف ريال إيرادات من إنفاق 1.1 ألف دولار.',
   'lead': 'حملات نماذج عملاء على سناب شات تغذّي فريق مبيعات. وقِيس النجاح بالصفقات المغلقة في نظام CRM، لا بعدد العملاء المحتملين ولا بتكلفتهم.',
   'body': lambda: (
     kpis([('70%', 'من العملاء المحتملين أُغلقوا وفق CRM'), ('63x', 'إيراد الصفقات ÷ الإنفاق الإعلاني'),
           ('$1.73', 'متوسط تكلفة العميل المحتمل'), ('$2.47', 'تكلفة الإعلان لكل صفقة مغلقة')]) +
     '<div class="prose narrow">'
     '<h2>ما الذي فعلته</h2><ol class="steps">'
     '<li><b>شغّلت حملتين واحتفظت بما نجح.</b>انخفضت تكلفة العميل المحتمل من <bdi>$2.73</bdi> في الحملة الأولى إلى <bdi>$1.14</bdi> في الثانية (<bdi>−58%</bdi>)، بإجمالي إنفاق <bdi>$1.1K</bdi>.</li>'
     '<li><b>استخدمت نماذج سناب شات المدمجة.</b>تُجمع البيانات داخل التطبيق دون إرسال المستخدم إلى صفحة هبوط أولًا.</li>'
     '<li><b>حكمت على الحملة بالصفقات المغلقة.</b>تحوّل <bdi>70%</bdi> من العملاء المحتملين إلى مبيعات، فالعميل الرخيص هنا كان مؤهلًا أيضًا.</li></ol>'
     '<h2>من الظهور إلى الصفقة المغلقة</h2>' +
     bars([('الظهور', 100, '329,756'), ('عملاء محتملون', 60, '636'), ('صفقات مغلقة', 45, '≈ 445'), ('الإيراد', 35, 'SAR 260K')], 100) +
     '<p>الأشرطة توضح مراحل القمع وليست بمقياس رسم. أرقام العملاء والإنفاق من مدير إعلانات سناب شات، والصفقات والإيراد من نظام CRM لدى العميل.</p>'
     '<div class="callout">تكلفة العميل المحتمل لا معنى لها دون نسبة الإغلاق. عميل بـ<bdi>$1.73</bdi> يُغلق بنسبة <bdi>70%</bdi> أفضل من عميل بـ<bdi>$0.80</bdi> لا يرد أحد عليه.</div>'
     '<h2>لقطة من الحساب الإعلاني</h2></div>' +
     shots([('leads-snapchat', 'سناب شات: 636 عميلًا محتملًا بتكلفة 1.73 دولار للعميل')], 'ar'))
  }
 },
]
