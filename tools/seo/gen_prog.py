import json,os,html as H
from gen import BASE,CSS
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'..','..')
BOTP="https://t.me/set_tracker_bot/train?startapp="
T={
"uk":{"path":"prohrama-trenuvan/","alt":"ru/programma-trenirovok/","lang":"uk","loc":"uk_UA",
 "title":"Програма тренувань у залі онлайн — для чоловіків і жінок | Million",
 "desc":"Безкоштовна програма тренувань у тренажерному залі: оберіть мету, рівень і кількість тренувань на тиждень — і одразу побачите вправи, підходи й повтори на тиждень.",
 "h1":"Програма тренувань у залі",
 "lead":"Оберіть мету, рівень і скільки разів на тиждень готові тренуватися — нижче з’явиться програма на тиждень: дні, вправи, підходи й повтори. Без реєстрації.",
 "sex":"Стать","sexs":[["m","Чоловік"],["f","Жінка"]],
 "lvl":"Рівень","lvls":[["0","Новачок<small>до 1 року</small>"],["1","Середній<small>1–3 роки</small>"],["2","Досвідчений<small>від 3 років</small>"]],
 "goal":"Мета","goals":[["mass","Набір маси"],["loss","Схуднути"],["dry","Сушка"],["recomp","Рекомпозиція"]],
 "n":"Силових тренувань на тиждень",
 "wd":["Понеділок","Вівторок","Середа","Четвер","Пʼятниця","Субота","Неділя"],
 "res":"Ваш тиждень","vol":"Обсяг",
 "ss":"⛓ — суперсет: виконуйте одразу після попередньої вправи, без відпочинку між ними.",
 "cardio":"Кардіо-дні — легка ходьба в зоні 2 між силовими днями: допомагає витратити більше калорій без втоми для м’язів.",
 "cta":"Отримати повну програму з вагами в Million",
 "ctas":"У застосунку: пробні ваги під вашу вагу й рівень, календар на 4–8 тижнів, техніка кожної вправи, заміна вправ і облік прогресу. Відкривається в Telegram.",
 "note":"Це орієнтир для старту, а не медична рекомендація. Перші тижні беріть вагу, з якою техніка не ламається. Якщо є болі чи захворювання — порадьтеся з лікарем; у застосунку можна вказати обмеження (спина, коліна, плечі, тиск), і вправи підберуться з їх урахуванням.",
 "how_h":"Як складається програма",
 "how":["<b>Спліт</b> залежить від кількості тренувань: 2–3 на тиждень — усе тіло за тренування, 4 — верх і низ, 5–6 — окремі групи м’язів. Кожен м’яз отримує навантаження 2–3 рази на тиждень.",
        "<b>Обсяг</b> — кількість робочих підходів на м’яз за тиждень — підібрано за рівнем: новачкам менше, досвідченим більше. Орієнтири взято з мета-аналізів досліджень.",
        "<b>Підходи й повтори</b> залежать від мети: на масу — базові вправи у 6–10 повторах, на схуднення й сушку — помірна вага, 10–15 повторів і кардіо.",
        "<b>Для жінок</b> більше вправ на сідниці й задню поверхню стегна, для новачків — більше тренажерів, де простіше тримати техніку."],
 "faq_h":"Часті запитання",
 "faq":[["Скільки разів на тиждень тренуватися новачку?","Зазвичай 2–3 силові тренування на все тіло. Цього достатньо, щоб прогресувати й відновлюватися. Більше тренувань має сенс, коли техніка вже стабільна."],
        ["Яку вагу брати на початку?","Таку, з якою останні 2–3 повтори даються важко, але техніка не ламається. У Million пробні ваги підбираються за вагою тіла, статтю й рівнем, а далі — за вашими результатами."],
        ["Скільки відпочивати між підходами?","У базових вправах — 2–3 хвилини, в ізолюючих — 1–1,5 хвилини. У застосунку таймер відпочинку запускається сам."],
        ["Чим програма для жінок відрізняється від чоловічої?","Принципи ті самі, але більше уваги сідницям і задній поверхні стегна, а верх тіла тренується з меншим обсягом."],
        ["Це заміна тренера?","Ні. Це безпечний старт і облік результатів. Техніку краще поставити з тренером — у Million можна знайти тренера й працювати з ним онлайн."]],
 "kb":"Калькулятор КБЖВ","kbp":"kalkulyator-kbzhv/",
 "foot":"Million — фітнес-асистент у Telegram","other":"Русская версия"},
"ru":{"path":"ru/programma-trenirovok/","alt":"prohrama-trenuvan/","lang":"ru","loc":"ru_UA",
 "title":"Программа тренировок в зале онлайн — для мужчин и женщин | Million",
 "desc":"Бесплатная программа тренировок в тренажёрном зале: выберите цель, уровень и количество тренировок в неделю — и сразу увидите упражнения, подходы и повторы на неделю.",
 "h1":"Программа тренировок в зале",
 "lead":"Выберите цель, уровень и сколько раз в неделю готовы тренироваться — ниже появится программа на неделю: дни, упражнения, подходы и повторы. Без регистрации.",
 "sex":"Пол","sexs":[["m","Мужчина"],["f","Женщина"]],
 "lvl":"Уровень","lvls":[["0","Новичок<small>до 1 года</small>"],["1","Средний<small>1–3 года</small>"],["2","Опытный<small>от 3 лет</small>"]],
 "goal":"Цель","goals":[["mass","Набор массы"],["loss","Похудеть"],["dry","Сушка"],["recomp","Рекомпозиция"]],
 "n":"Силовых тренировок в неделю",
 "wd":["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"],
 "res":"Ваша неделя","vol":"Объём",
 "ss":"⛓ — суперсет: выполняйте сразу после предыдущего упражнения, без отдыха между ними.",
 "cardio":"Кардио-дни — лёгкая ходьба в зоне 2 между силовыми днями: помогает потратить больше калорий без усталости для мышц.",
 "cta":"Получить полную программу с весами в Million",
 "ctas":"В приложении: пробные веса под ваш вес и уровень, календарь на 4–8 недель, техника каждого упражнения, замена упражнений и учёт прогресса. Открывается в Telegram.",
 "note":"Это ориентир для старта, а не медицинская рекомендация. Первые недели берите вес, с которым техника не ломается. Если есть боли или заболевания — посоветуйтесь с врачом; в приложении можно указать ограничения (спина, колени, плечи, давление), и упражнения подберутся с их учётом.",
 "how_h":"Как составляется программа",
 "how":["<b>Сплит</b> зависит от количества тренировок: 2–3 в неделю — всё тело за тренировку, 4 — верх и низ, 5–6 — отдельные группы мышц. Каждая мышца получает нагрузку 2–3 раза в неделю.",
        "<b>Объём</b> — количество рабочих подходов на мышцу за неделю — подобран по уровню: новичкам меньше, опытным больше. Ориентиры взяты из мета-анализов исследований.",
        "<b>Подходы и повторы</b> зависят от цели: на массу — базовые упражнения в 6–10 повторах, на похудение и сушку — умеренный вес, 10–15 повторов и кардио.",
        "<b>Для женщин</b> больше упражнений на ягодицы и заднюю поверхность бедра, для новичков — больше тренажёров, где проще держать технику."],
 "faq_h":"Частые вопросы",
 "faq":[["Сколько раз в неделю тренироваться новичку?","Обычно 2–3 силовые тренировки на всё тело. Этого достаточно, чтобы прогрессировать и восстанавливаться. Больше тренировок имеет смысл, когда техника уже стабильна."],
        ["Какой вес брать в начале?","Такой, с которым последние 2–3 повтора даются тяжело, но техника не ломается. В Million пробные веса подбираются по весу тела, полу и уровню, а дальше — по вашим результатам."],
        ["Сколько отдыхать между подходами?","В базовых упражнениях — 2–3 минуты, в изолирующих — 1–1,5 минуты. В приложении таймер отдыха запускается сам."],
        ["Чем программа для женщин отличается от мужской?","Принципы те же, но больше внимания ягодицам и задней поверхности бедра, а верх тела тренируется с меньшим объёмом."],
        ["Это замена тренера?","Нет. Это безопасный старт и учёт результатов. Технику лучше поставить с тренером — в Million можно найти тренера и работать с ним онлайн."]],
 "kb":"Калькулятор КБЖУ","kbp":"ru/kalkulyator-kbzhu/",
 "foot":"Million — фитнес-ассистент в Telegram","other":"Українська версія"}}
CSS2=""".seg button small{display:block;font:600 11.5px var(--body);color:var(--muted);margin-top:2px}
.day{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:14px 16px;margin:10px 0}.day .wd{font:700 12px var(--body);letter-spacing:1.2px;text-transform:uppercase;color:var(--muted)}.day h3{font:700 17px var(--display);color:var(--gold);margin:4px 0 8px}
.day ol{list-style:none;padding:0;margin:0}.day li{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-top:1px solid var(--line)}.day li:first-child{border-top:0}.day li span{color:var(--fg)}.day li b{color:var(--gold);white-space:nowrap}.day li.cd span{color:#D9CBA2}.day li.cd{flex-direction:column;gap:2px}.day li.cd b{color:var(--muted);font-weight:600;white-space:normal;font-size:14px}
.vol{font-size:14px;color:var(--muted);margin:4px 2px 8px}"""
JS=r"""(function(){var P=window.__P,L=window.__L,S={sex:"m",lvl:"0",goal:"mass",n:"3"};
try{var sv=JSON.parse(localStorage.getItem("mk_prog")||"null");if(sv)for(var k in S)if(sv[k])S[k]=String(sv[k])}catch(e){}
function e(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function draw(){var c=P.c[S.sex+S.lvl+S.goal+S.n];if(!c)return;var h="",ss=0,cd=0;
c[1].forEach(function(x){var d=P.d[x[1]],str=0;var li=d.slice(1).map(function(r){var nm=P.n[r[0]],sr=P.n[r[1]];if(nm.indexOf("⛓")>-1)ss=1;if(r[2])str=1;return'<li'+(r[2]?'':' class="cd"')+'><span>'+e(nm)+'</span><b>'+e(sr)+'</b></li>'}).join("");if(!str)cd=1;
h+='<div class="day"><div class="wd">'+L.wd[x[0]]+'</div><h3>'+e(P.n[d[0]])+'</h3><ol>'+li+'</ol></div>'});
document.getElementById("days").innerHTML=h;document.getElementById("vol").textContent=L.vol+": "+P.n[c[0]];
document.getElementById("ss").hidden=!ss;document.getElementById("cdn").hidden=!cd;
document.getElementById("cta").href="https://t.me/set_tracker_bot/train?startapp=p"+S.sex+S.lvl+S.goal+S.n;
try{localStorage.setItem("mk_prog",JSON.stringify(S))}catch(e){}}
["sex","lvl","goal","n"].forEach(function(k){var el=document.getElementById("s_"+k);[].forEach.call(el.children,function(b){b.setAttribute("aria-pressed",b.dataset.v===S[k])});
el.addEventListener("click",function(ev){var b=ev.target.closest("button");if(!b)return;S[k]=b.dataset.v;[].forEach.call(el.children,function(x){x.setAttribute("aria-pressed",x===b)});draw()})});
draw()})();"""
def seg(id,items,cur,cols):
  return '<div class="seg" id="'+id+'" style="grid-template-columns:repeat('+str(cols)+',1fr)">'+''.join('<button type="button" data-v="'+str(v)+'" aria-pressed="'+('true' if str(v)==str(cur) else 'false')+'">'+t+'</button>' for v,t in items)+'</div>'
def static_days(P,d,key):
  c=P['c'][key];out=''
  for w,di in c[1]:
    day=P['d'][di];li=''.join('<li'+('' if r[2] else ' class="cd"')+'><span>'+H.escape(P['n'][r[0]])+'</span><b>'+H.escape(P['n'][r[1]])+'</b></li>' for r in day[1:])
    out+='<div class="day"><div class="wd">'+d['wd'][w]+'</div><h3>'+H.escape(P['n'][day[0]])+'</h3><ol>'+li+'</ol></div>'
  return out,d['vol']+': '+P['n'][c[0]]
def page(L):
  d=T[L];P=json.load(open(os.path.join(HERE,'prog_'+L+'.json')));url=BASE+d["path"]
  days,vol=static_days(P,d,'m0mass3')
  faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in d["faq"]]}
  app={"@context":"https://schema.org","@type":"WebApplication","name":d["h1"]+" — Million","url":url,"applicationCategory":"HealthApplication","operatingSystem":"Web, Telegram","inLanguage":d["lang"],"offers":{"@type":"Offer","price":"0","priceCurrency":"UAH"},"description":d["desc"]}
  hl='<link rel="alternate" hreflang="uk" href="'+BASE+T["uk"]["path"]+'"><link rel="alternate" hreflang="ru" href="'+BASE+T["ru"]["path"]+'"><link rel="alternate" hreflang="x-default" href="'+BASE+T["uk"]["path"]+'">'
  return f'''<!DOCTYPE html>
<html lang="{d["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d["title"]}</title><meta name="description" content="{d["desc"]}"><meta name="robots" content="index,follow">
<link rel="canonical" href="{url}">{hl}
<meta property="og:type" content="website"><meta property="og:title" content="{d["title"]}"><meta property="og:description" content="{d["desc"]}"><meta property="og:url" content="{url}"><meta property="og:locale" content="{d["loc"]}"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0A0A09">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Unbounded:wght@600;700&display=swap">
<script type="application/ld+json">{json.dumps(app,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(faq,ensure_ascii=False)}</script>
<style>{CSS}
{CSS2}</style></head><body><main>
<header><a class="brand" href="{BOTP}wprog">MILLION</a><a class="lng" href="{BASE+d["alt"]}" hreflang="{'ru' if L=='uk' else 'uk'}">{d["other"]}</a></header>
<h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>
<div class="card"><span class="l">{d["sex"]}</span>{seg("s_sex",d["sexs"],"m",2)}<span class="l" style="margin-top:14px">{d["lvl"]}</span>{seg("s_lvl",d["lvls"],"0",3)}</div>
<div class="card"><span class="l">{d["goal"]}</span>{seg("s_goal",d["goals"],"mass",2)}<span class="l" style="margin-top:14px">{d["n"]}</span>{seg("s_n",[(i,str(i)) for i in range(2,7)],3,5)}</div>
<h2>{d["res"]}</h2><p class="vol" id="vol">{vol}</p>
<section id="days" aria-live="polite">{days}</section>
<p class="hint" id="ss" hidden>{d["ss"]}</p><p class="hint" id="cdn" hidden>{d["cardio"]}</p>
<a class="btn p" id="cta" href="{BOTP}pm0mass3" rel="noopener" style="margin-top:16px">{d["cta"]}</a><p class="hint" style="text-align:center">{d["ctas"]}</p>
<p class="note">{d["note"]}</p>
<h2>{d["how_h"]}</h2><ul class="how">{''.join('<li>'+x+'</li>' for x in d["how"])}</ul>
<h2>{d["faq_h"]}</h2>{''.join('<details><summary>'+q+'</summary><p>'+a+'</p></details>' for q,a in d["faq"])}
<a class="btn s" href="{BASE+d["kbp"]}">{d["kb"]}</a>
<footer><a href="{BOTP}wprog">{d["foot"]}</a></footer></main>
<script>window.__L={json.dumps({"wd":d["wd"],"vol":d["vol"]},ensure_ascii=False)};window.__P={json.dumps(P,ensure_ascii=False,separators=(',',':'))};</script><script>{JS}</script></body></html>'''
def main():
  for L in T:
    p=os.path.join(ROOT,T[L]["path"]);os.makedirs(p,exist_ok=True);open(os.path.join(p,'index.html'),'w').write(page(L))
