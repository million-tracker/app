import json,os
BASE="https://million-tracker.github.io/app/"
BOT="https://t.me/set_tracker_bot/train?startapp=wkbzh"
T={
"uk":{"path":"kalkulyator-kbzhv/","alt":"ru/kalkulyator-kbzhu/","lang":"uk",
 "title":"Калькулятор КБЖВ і калорій онлайн — розрахунок норми | Million",
 "desc":"Безкоштовний калькулятор КБЖВ: норма калорій, білків, жирів і вуглеводів для схуднення, сушки чи набору маси. Формула Міффліна–Сан Жеора з урахуванням тренувань.",
 "h1":"Калькулятор КБЖВ і калорій",
 "lead":"Порахуйте, скільки калорій, білків, жирів і вуглеводів вам потрібно на день — для схуднення, сушки, підтримки чи набору маси. Без реєстрації.",
 "sex":"Стать","m":"Чоловік","f":"Жінка","age":"Вік","hgt":"Зріст, см","wgt":"Вага, кг",
 "act":"Активність — кроки за день","acts":["Низька · до 5 тис.","Середня · 7–8 тис.","Висока · 10–12 тис.","Дуже висока · 15 тис.+"],
 "actn":"Скільки ви в середньому ходите за день, без урахування тренувань.",
 "tr":"Тренувань на тиждень","lvl":"Інтенсивність тренувань","lvls":["Легка","Середня","Висока"],
 "goal":"Мета","goals":[["loss","Схуднути"],["dry","Сушка"],["keep","Підтримка"],["recomp","Рекомпозиція"],["mass","Набір маси"]],
 "calc":"Розрахувати","kcal":"ккал на день","p":"Білки","fa":"Жири","c":"Вуглеводи","g":"г",
 "bmr":"Базовий обмін","tdee":"Витрата за день","err":"Вкажіть вік (14–90), зріст (120–230 см) і вагу (35–250 кг).",
 "cta":"Зберегти норму й вести харчування в Million","ctas":"Million — фітнес-асистент у Telegram: калькулятор КБЖВ, меню, програма тренувань і прогрес. Безкоштовно відкривається в Telegram.",
 "cta2":"Скласти програму тренувань",
 "note":"Розрахунок — орієнтир, а не медична рекомендація. Перші 2–3 тижні стежте за вагою й самопочуттям і коригуйте калорії на 5–10%. При захворюваннях порадьтеся з лікарем.",
 "how_h":"Як рахує калькулятор",
 "how":["<b>Базовий обмін</b> — за формулою Міффліна–Сан Жеора: 10 × вага + 6,25 × зріст − 5 × вік, +5 для чоловіків або −161 для жінок.",
        "<b>Активність</b> рахується за кроками: кожна тисяча кроків понад 3000 додає близько 0,5 ккал на кг ваги. <b>Тренування</b> додають витрату за їхньою кількістю та інтенсивністю.",
        "<b>Мета</b>: для схуднення — дефіцит, що дає втрату близько 0,5–1% ваги на тиждень (не нижче базового обміну), для набору маси — профіцит ~12%, для рекомпозиції — невеликий дефіцит ~5%.",
        "<b>Білки</b> — 1,6–2,4 г на кг ваги залежно від мети, <b>жири</b> — 0,8–1,2 г на кг, решта — <b>вуглеводи</b>."],
 "faq_h":"Часті запитання",
 "faq":[["Що таке КБЖВ?","Калорії, білки, жири й вуглеводи — добова норма енергії та поживних речовин. Українське КБЖВ і російське КБЖУ — це одне й те саме."],
        ["Скільки білка потрібно на день?","Для людей, які тренуються, найчастіше рекомендують 1,6–2,2 г білка на кг ваги. На сушці — ближче до верхньої межі, щоб зберегти м’язи."],
        ["Чому вага не змінюється на розрахованій нормі?","Формула дає оцінку, а реальна витрата відрізняється в межах ±10%. Зважуйтеся 3–4 рази на тиждень і дивіться на середнє за 2 тижні; якщо вага стоїть — змініть калорії на 5–10%."],
        ["Наскільки швидко можна безпечно худнути?","Орієнтир — 0,5–1% ваги тіла на тиждень. Швидше — більший ризик втратити м’язи й сповільнити обмін."],
        ["Це медична рекомендація?","Ні. Це розрахунок за загальноприйнятими формулами. При захворюваннях, вагітності чи прийомі ліків норму підбирає лікар."]],
 "foot":"Million — фітнес-асистент у Telegram",
 "other":"Русская версия"},
"ru":{"path":"ru/kalkulyator-kbzhu/","alt":"kalkulyator-kbzhv/","lang":"ru",
 "title":"Калькулятор КБЖУ и калорий онлайн — расчёт нормы | Million",
 "desc":"Бесплатный калькулятор КБЖУ: норма калорий, белков, жиров и углеводов для похудения, сушки или набора массы. Формула Миффлина–Сан Жеора с учётом тренировок.",
 "h1":"Калькулятор КБЖУ и калорий",
 "lead":"Посчитайте, сколько калорий, белков, жиров и углеводов вам нужно в день — для похудения, сушки, поддержания или набора массы. Без регистрации.",
 "sex":"Пол","m":"Мужчина","f":"Женщина","age":"Возраст","hgt":"Рост, см","wgt":"Вес, кг",
 "act":"Активность — шаги за день","acts":["Низкая · до 5 тыс.","Средняя · 7–8 тыс.","Высокая · 10–12 тыс.","Очень высокая · 15 тыс.+"],
 "actn":"Сколько вы в среднем ходите за день, без учёта тренировок.",
 "tr":"Тренировок в неделю","lvl":"Интенсивность тренировок","lvls":["Лёгкая","Средняя","Высокая"],
 "goal":"Цель","goals":[["loss","Похудеть"],["dry","Сушка"],["keep","Поддержание"],["recomp","Рекомпозиция"],["mass","Набор массы"]],
 "calc":"Рассчитать","kcal":"ккал в день","p":"Белки","fa":"Жиры","c":"Углеводы","g":"г",
 "bmr":"Базовый обмен","tdee":"Расход за день","err":"Укажите возраст (14–90), рост (120–230 см) и вес (35–250 кг).",
 "cta":"Сохранить норму и вести питание в Million","ctas":"Million — фитнес-ассистент в Telegram: калькулятор КБЖУ, меню, программа тренировок и прогресс. Бесплатно открывается в Telegram.",
 "cta2":"Составить программу тренировок",
 "note":"Расчёт — ориентир, а не медицинская рекомендация. Первые 2–3 недели следите за весом и самочувствием и корректируйте калории на 5–10%. При заболеваниях посоветуйтесь с врачом.",
 "how_h":"Как считает калькулятор",
 "how":["<b>Базовый обмен</b> — по формуле Миффлина–Сан Жеора: 10 × вес + 6,25 × рост − 5 × возраст, +5 для мужчин или −161 для женщин.",
        "<b>Активность</b> считается по шагам: каждая тысяча шагов сверх 3000 добавляет около 0,5 ккал на кг веса. <b>Тренировки</b> добавляют расход по их количеству и интенсивности.",
        "<b>Цель</b>: для похудения — дефицит, дающий потерю около 0,5–1% веса в неделю (не ниже базового обмена), для набора массы — профицит ~12%, для рекомпозиции — небольшой дефицит ~5%.",
        "<b>Белки</b> — 1,6–2,4 г на кг веса в зависимости от цели, <b>жиры</b> — 0,8–1,2 г на кг, остальное — <b>углеводы</b>."],
 "faq_h":"Частые вопросы",
 "faq":[["Что такое КБЖУ?","Калории, белки, жиры и углеводы — суточная норма энергии и питательных веществ."],
        ["Сколько белка нужно в день?","Тем, кто тренируется, чаще всего рекомендуют 1,6–2,2 г белка на кг веса. На сушке — ближе к верхней границе, чтобы сохранить мышцы."],
        ["Почему вес не меняется на рассчитанной норме?","Формула даёт оценку, а реальный расход отличается в пределах ±10%. Взвешивайтесь 3–4 раза в неделю и смотрите на среднее за 2 недели; если вес стоит — измените калории на 5–10%."],
        ["Как быстро можно безопасно худеть?","Ориентир — 0,5–1% веса тела в неделю. Быстрее — выше риск потерять мышцы и замедлить обмен."],
        ["Это медицинская рекомендация?","Нет. Это расчёт по общепринятым формулам. При заболеваниях, беременности или приёме лекарств норму подбирает врач."]],
 "foot":"Million — фитнес-ассистент в Telegram",
 "other":"Українська версія"}}
CSS=r""":root{--bg:#0A0A09;--card:#161512;--fg:#F3E7C4;--gold:#E9C966;--muted:#A8915A;--line:#2E2A20;--body:"Manrope",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--display:"Unbounded","Manrope",system-ui,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--bg);color:var(--fg);font:500 16px/1.55 var(--body)}
a{color:var(--gold)}main{max-width:640px;margin:0 auto;padding:20px 16px 48px}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px}header .brand{font:700 18px var(--display);color:var(--gold);text-decoration:none;letter-spacing:.5px}header .lng{font-size:13px;color:var(--muted)}
h1{font:700 26px/1.2 var(--display);color:var(--gold);margin:6px 0 10px}h2{font:700 19px/1.3 var(--display);color:var(--gold);margin:34px 0 12px}
.lead{color:#D9CBA2;margin:0 0 18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:16px;margin:12px 0}
label.l,.l{display:block;font:700 12px var(--body);letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.row3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
input{width:100%;background:#0F0E0B;border:1px solid var(--line);border-radius:14px;color:var(--gold);font:700 20px var(--body);padding:12px 12px;outline:none}input:focus{border-color:var(--gold)}input::placeholder{color:#4d4636}
.seg{display:grid;gap:8px}.seg button{background:#0F0E0B;border:1px solid var(--line);border-radius:14px;color:#D9CBA2;font:700 14px var(--body);padding:12px 6px;cursor:pointer}.seg button[aria-pressed=true]{border-color:var(--gold);color:var(--gold);box-shadow:0 0 0 1px var(--gold) inset,0 0 18px rgba(233,201,102,.15)}
.hint{font-size:13px;color:var(--muted);margin:8px 2px 0}
.btn{display:block;width:100%;text-align:center;border:0;border-radius:16px;padding:16px;font:800 17px var(--body);cursor:pointer;text-decoration:none}.btn.p{background:linear-gradient(135deg,#F3DA8B,#C9A040);color:#1a1405}.btn.s{background:#0F0E0B;border:1px solid var(--gold);color:var(--gold);margin-top:10px}
.res{display:none}.res.on{display:block}.big{font:700 40px/1 var(--display);color:var(--gold)}.big small{font:600 15px var(--body);color:var(--muted);margin-left:6px}
.mac{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px}.mac div{background:#0F0E0B;border:1px solid var(--line);border-radius:14px;padding:10px;text-align:center}.mac b{display:block;font:700 22px var(--display);color:var(--gold)}.mac span{font-size:12.5px;color:var(--muted)}
.sub{display:flex;justify-content:space-between;font-size:14px;color:var(--muted);margin-top:12px}.err{color:#FF8A6B;font-size:14px;margin-top:10px;min-height:1em}
.note{font-size:13px;color:var(--muted);margin-top:12px}ul.how{padding-left:18px;margin:0}ul.how li{margin:8px 0}
details{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px;margin:8px 0}summary{font-weight:700;cursor:pointer;color:var(--fg)}details p{margin:8px 0 0;color:#D9CBA2}
footer{margin-top:36px;font-size:13px;color:var(--muted);text-align:center}"""
JS=r"""(function(){var D=window.__D,S={sex:"m",act:1,tr:3,lvl:1,goal:"loss"};
function seg(id,key){var el=document.getElementById(id);el.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;S[key]=isNaN(+b.dataset.v)?b.dataset.v:+b.dataset.v;[].forEach.call(el.children,function(x){x.setAttribute("aria-pressed",x===b)});if(document.getElementById("res").classList.contains("on"))calc()})}
seg("s_sex","sex");seg("s_act","act");seg("s_tr","tr");seg("s_lvl","lvl");seg("s_goal","goal");
function num(id){return parseFloat(String(document.getElementById(id).value).replace(",","."))||0}
function sd(g,w,h,bmr,td){var bmi=w/Math.pow(h/100,2);if(g==="mass")return Math.round(Math.max(bmr,td*1.12)/10)*10;if(g==="recomp")return Math.round(Math.max(bmr,td*.95)/10)*10;if(g==="loss"||g==="dry"){var r=bmi<25?.5:g==="dry"?.75:1,c=w*r/100*7700/7,p=Math.min(td*.2,Math.max(td*.15,c));return Math.round(Math.max(bmr,td-p)/10)*10}return Math.round(td/10)*10}
function calc(){var a=num("age"),h=num("hgt"),w=num("wgt"),er=document.getElementById("err");if(!(a>=14&&a<=90&&h>=120&&h<=230&&w>=35&&w<=250)){er.textContent=D.err;document.getElementById("res").classList.remove("on");return}er.textContent="";
var f=S.sex==="f",bmr=10*w+6.25*h-5*a+(f?-161:5),neat=Math.max(0,[4000,7500,11000,17000][S.act]-3000)*w*5e-4,met=[3.5,5,6.5][S.lvl],train=S.tr*(met-1)*w/7,td=Math.min(bmr*2.4,bmr*1.2+neat+train),k=sd(S.goal,w,h,bmr,td),bmi=w/Math.pow(h/100,2),hh=bmi>30?27*Math.pow(h/100,2):w,
pc={loss:f?1.9:2,dry:f?2.2:2.4,recomp:f?2:2.2,keep:f?1.5:1.6,mass:f?1.8:2}[S.goal],fc={loss:f?1:.9,dry:f?.9:.8,recomp:f?1.1:1,keep:f?1:.9,mass:f?1.2:1.1}[S.goal],P=Math.round(hh*pc),F=Math.round(w*fc);S.goal==="dry"&&(F=Math.max(F,f?55:50));
var X=50,M=function(){return P*4+F*9+X*4-k};if(M()>0){var j=Math.max(30,Math.round(w*(f?.7:.6)));F=Math.max(Math.min(F,j),Math.round(F-M()/9))}if(M()>0){var j2=Math.round(hh*1.4);P=Math.max(Math.min(P,j2),Math.round(P-M()/4))}if(M()>0)k=Math.ceil((P*4+F*9+X*4)/10)*10;var C=Math.max(X,Math.round((k-P*4-F*9)/4));
var fm=function(v){return String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g," ")};
document.getElementById("o_k").firstChild.nodeValue=fm(k);document.getElementById("o_p").textContent=P;document.getElementById("o_f").textContent=F;document.getElementById("o_c").textContent=C;document.getElementById("o_b").textContent=fm(bmr);document.getElementById("o_t").textContent=fm(td);
var r=document.getElementById("res");r.classList.add("on");try{localStorage.setItem("mk_calc",JSON.stringify({a:a,h:h,w:w,S:S}))}catch(e){}var sp="n"+Math.round(w)+"_"+Math.round(h)+"_"+Math.round(a)+"_"+S.sex+"_"+S.act+"_"+S.tr+"_"+S.lvl+"_"+S.goal;var cta=document.getElementById("cta");cta&&(cta.href="https://t.me/set_tracker_bot/train?startapp="+sp)}
document.getElementById("go").addEventListener("click",function(){calc();var r=document.getElementById("res");r.classList.contains("on")&&r.scrollIntoView({behavior:"smooth",block:"start"})});
try{var sv=JSON.parse(localStorage.getItem("mk_calc")||"null");if(sv){document.getElementById("age").value=sv.a;document.getElementById("hgt").value=sv.h;document.getElementById("wgt").value=sv.w;}}catch(e){}
})();"""
def page(L):
  d=T[L];url=BASE+d["path"];alt=BASE+d["alt"]
  seg=lambda id,items,cur,cols: '<div class="seg" id="'+id+'" style="grid-template-columns:repeat('+str(cols)+',1fr)">'+''.join('<button type="button" data-v="'+str(v)+'" aria-pressed="'+('true' if str(v)==str(cur) else 'false')+'">'+t+'</button>' for v,t in items)+'</div>'
  faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in d["faq"]]}
  app={"@context":"https://schema.org","@type":"WebApplication","name":d["h1"]+" — Million","url":url,"applicationCategory":"HealthApplication","operatingSystem":"Web, Telegram","inLanguage":d["lang"],"offers":{"@type":"Offer","price":"0","priceCurrency":"UAH"},"description":d["desc"]}
  hl='<link rel="alternate" hreflang="uk" href="'+BASE+T["uk"]["path"]+'"><link rel="alternate" hreflang="ru" href="'+BASE+T["ru"]["path"]+'"><link rel="alternate" hreflang="x-default" href="'+BASE+T["uk"]["path"]+'">'
  html=f'''<!DOCTYPE html>
<html lang="{d["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d["title"]}</title><meta name="description" content="{d["desc"]}"><meta name="robots" content="index,follow">
<link rel="canonical" href="{url}">{hl}
<meta property="og:type" content="website"><meta property="og:title" content="{d["title"]}"><meta property="og:description" content="{d["desc"]}"><meta property="og:url" content="{url}"><meta property="og:locale" content="{'uk_UA' if L=='uk' else 'ru_UA'}"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0A0A09">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Unbounded:wght@600;700&display=swap">
<script type="application/ld+json">{json.dumps(app,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq,ensure_ascii=False)}</script>
<style>{CSS}</style></head><body><main>
<header><a class="brand" href="{BOT}">MILLION</a><a class="lng" href="{alt}" hreflang="{'ru' if L=='uk' else 'uk'}">{d["other"]}</a></header>
<h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>
<div class="card"><span class="l">{d["sex"]}</span>{seg("s_sex",[("m",d["m"]),("f",d["f"])],"m",2)}</div>
<div class="card"><div class="row3"><label><span class="l">{d["age"]}</span><input id="age" inputmode="numeric" placeholder="30"></label><label><span class="l">{d["hgt"]}</span><input id="hgt" inputmode="decimal" placeholder="175"></label><label><span class="l">{d["wgt"]}</span><input id="wgt" inputmode="decimal" placeholder="75"></label></div></div>
<div class="card"><span class="l">{d["act"]}</span>{seg("s_act",list(enumerate(d["acts"])),1,2)}<p class="hint">{d["actn"]}</p></div>
<div class="card"><span class="l">{d["tr"]}</span>{seg("s_tr",[(i,str(i)) for i in range(8)],3,8)}<span class="l" style="margin-top:14px">{d["lvl"]}</span>{seg("s_lvl",list(enumerate(d["lvls"])),1,3)}</div>
<div class="card"><span class="l">{d["goal"]}</span>{seg("s_goal",d["goals"],"loss",2)}</div>
<button class="btn p" id="go" type="button">{d["calc"]}</button><div class="err" id="err" role="alert"></div>
<section class="res" id="res" aria-live="polite"><div class="card"><div class="big" id="o_k">0<small>{d["kcal"]}</small></div>
<div class="mac"><div><b id="o_p">0</b><span>{d["p"]}, {d["g"]}</span></div><div><b id="o_f">0</b><span>{d["fa"]}, {d["g"]}</span></div><div><b id="o_c">0</b><span>{d["c"]}, {d["g"]}</span></div></div>
<div class="sub"><span>{d["bmr"]}: <b id="o_b">0</b></span><span>{d["tdee"]}: <b id="o_t">0</b></span></div><p class="note">{d["note"]}</p></div>
<a class="btn p" id="cta" href="{BOT}" rel="noopener">{d["cta"]}</a><p class="hint" style="text-align:center">{d["ctas"]}</p><a class="btn s" href="{BASE+('prohrama-trenuvan/' if L=='uk' else 'ru/programma-trenirovok/')}">{d["cta2"]}</a></section>
<h2>{d["how_h"]}</h2><ul class="how">{''.join('<li>'+x+'</li>' for x in d["how"])}</ul>
<h2>{d["faq_h"]}</h2>{''.join('<details><summary>'+q+'</summary><p>'+a+'</p></details>' for q,a in d["faq"])}
<footer><a href="{BOT}">{d["foot"]}</a></footer></main>
<script>window.__D={json.dumps({"err":d["err"]},ensure_ascii=False)};</script><script>{JS}</script></body></html>'''
  return html
PAGES=[("kalkulyator-kbzhv/","ru/kalkulyator-kbzhu/"),("prohrama-trenuvan/","ru/programma-trenirovok/")]
if __name__=="__main__":
  R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
  for L in T:
    p=os.path.join(R,T[L]["path"]);os.makedirs(p,exist_ok=True);open(os.path.join(p,'index.html'),'w').write(page(L))
  import gen_prog;gen_prog.main()
  open(os.path.join(R,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'+''.join(f'<url><loc>{BASE+u}</loc><xhtml:link rel="alternate" hreflang="uk" href="{BASE+a}"/><xhtml:link rel="alternate" hreflang="ru" href="{BASE+b}"/><changefreq>monthly</changefreq><priority>0.9</priority></url>\n' for a,b in PAGES for u in (a,b))+'</urlset>\n')
  print('ok')
