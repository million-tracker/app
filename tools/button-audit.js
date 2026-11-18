// Button audit for Million: opens the app in headless Chromium under its real hostname,
// clicks every [data-a] button on every tab and in every sheet it opens (up to DEPTH levels),
// each from a fresh copy of the start state, and reports JS errors (ERR) and buttons with
// no visible effect (NOCHANGE). Usage:
//   node tools/button-audit.js [index.html] [uk|ru|en] [out.json] [DEPTH=3] [seed.js]
//   env TAB=train|hist|food|prog (one tab), R=a-b (slice of top-level buttons), TL=ms time limit
// seed.js runs in the page before the start state is captured (e.g. tools/seed-coach.js).
// Playwright: require path below; adjust if `npm root -g` differs.
const {chromium}=require(process.env.PW||"/home/claude/.npm-global/lib/node_modules/playwright");const fs=require("fs");
const launch=async(file,lang)=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844}});
 await ctx.route("https://million-tracker.github.io/**",r=>r.fulfill({contentType:"text/html",body:fs.readFileSync(file)}));
 await ctx.route(/^(?!https:\/\/million-tracker\.github\.io).*/,r=>r.abort());
 const pg=await ctx.newPage();pg.errs=[];pg.on("pageerror",e=>pg.errs.push(e.message));pg.dialogs=[];pg.on("dialog",d=>{pg.dialogs.push(d.type()+":"+d.message().slice(0,60));d.accept().catch(()=>{})});
 if(lang) await ctx.addInitScript(l=>{try{if(!localStorage.getItem("tb_lang"))localStorage.setItem("tb_lang",l)}catch{}},lang);
 await pg.goto("https://million-tracker.github.io/app/");await pg.waitForTimeout(3000);return {b,ctx,pg};};


const FILE=process.argv[2]||require("path").join(__dirname,"..","index.html"), LANG=process.argv[3]||"en", OUT=process.argv[4]||"/tmp/aud/res.json", MAXD=+(process.argv[5]||3), SEED=process.argv[6]||"";
(async()=>{const {b,pg}=await launch(FILE,LANG);
 if(SEED) await pg.evaluate(new Function(fs.readFileSync(SEED,"utf8")));
 await pg.reload();await pg.waitForTimeout(2500);
 const snap=await pg.evaluate(()=>({l:JSON.stringify(Object.assign({},localStorage)),s:JSON.stringify(Object.assign({},sessionStorage))}));
 const restore=async()=>{await pg.evaluate(sn=>{localStorage.clear();const l=JSON.parse(sn.l);for(const k in l)localStorage.setItem(k,l[k]);const s=JSON.parse(sn.s);for(const k in s)sessionStorage.setItem(k,s[k])},snap);await pg.reload();await pg.waitForTimeout(1000);pg.errs.length=0;pg.dialogs.length=0;};
 const sig=()=>pg.evaluate(()=>{const H=s=>{let x=0;for(let i=0;i<s.length;i++)x=(x*31+s.charCodeAt(i))|0;return x};const sh=document.getElementById("sheet"),sb=document.getElementById("sheetBody");
   const ov=[...document.body.children].filter(e=>!["view","sheet","rest"].includes(e.id)&&e.tagName!=="SCRIPT"&&getComputedStyle(e).display!=="none"&&e.offsetHeight>0).map(e=>e.id||e.className).join(",");
   return {v:H((document.getElementById("view")||document.body).innerHTML),open:!sh.hidden,s:sh.hidden?0:H(sb.innerHTML),st:sh.hidden?"":(sb.querySelector("h1,h2,h3,b")||sb).innerText.trim().slice(0,40),ov,rest:H((document.getElementById("rest")||{innerHTML:""}).innerHTML),y:Math.round(scrollY),cls:document.documentElement.className}});
 // click by path: each step {scope:'main'|'sheet', a, k}  (k = index among [data-a=a] in scope)
 const clickStep=st=>pg.evaluate(st=>{const root=st.scope==="sheet"?document.getElementById("sheetBody"):document;const els=[...root.querySelectorAll('[data-a="'+st.a+'"]')].filter(e=>st.scope==="sheet"||!e.closest("#sheet"));const e=els[st.k];if(!e)return false;e.click();return true},st);
 const list=scope=>pg.evaluate(scope=>{const root=scope==="sheet"?document.getElementById("sheetBody"):document;const m=[];const cnt={};root.querySelectorAll("[data-a]").forEach(e=>{if(scope!=="sheet"&&e.closest("#sheet"))return;if(e.tagName==="INPUT"&&e.type!=="checkbox"&&e.type!=="button")return;const a=e.dataset.a;const k=cnt[a]=(cnt[a]||0);cnt[a]++;m.push({a,k,x:(e.dataset.x||"").slice(0,30),pr:e.getAttribute("aria-pressed")==="true"||e.getAttribute("aria-current")==="true"||e.classList.contains("on")||e.classList.contains("sel"),dis:!!e.disabled||e.getAttribute("aria-disabled")==="true",t:(e.innerText||e.getAttribute("aria-label")||"").trim().replace(/\s+/g," ").slice(0,40)})});return m},scope);
 const res=[];const seen=new Set();const cap={};
 const pick=items=>{const by={};for(const it of items)(by[it.a]=by[it.a]||[]).push(it);const out=[];for(const a in by){const L=by[a];const xs=new Set(L.map(z=>z.x));const idx=xs.size<=6&&L.length<=6?L.map((_,i)=>i):[...new Set([0,Math.floor(L.length/2),L.length-1])];for(const i of idx)out.push(L[i])}return out};
 const replay=async path=>{await restore();for(const st of path){if(!await clickStep(st))return false;await pg.waitForTimeout(350)}return true};
 const tabs=await pg.evaluate(()=>[...document.querySelectorAll('[data-a="tab"]')].map(e=>e.dataset.x));console.log("tabs",tabs);const ONLY=process.env.TAB;const t0=Date.now();
 async function explore(path,scope,depth,ctxName){
   if(!await replay(path)) return;
   let items=pick(await list(scope));if(depth===1&&process.env.R){const [a,b2]=process.env.R.split("-").map(Number);items=items.slice(a,b2)}
   for(const it of items){
     const key=ctxName+"|"+it.a+"|"+it.x;const ck=ctxName+"|"+it.a;cap[ck]=cap[ck]||0;if(seen.has(key)||cap[ck]>=4)continue;seen.add(key);cap[ck]++;
     if(!await replay(path))break;const before=await sig();const e0=pg.errs.length;
     if(!await clickStep({scope,a:it.a,k:it.k})){res.push({ctx:ctxName,...it,r:"NOT FOUND"});continue}
     await pg.waitForTimeout(600);const after=await sig();const errs=pg.errs.slice(e0);
     const ch=[];if(after.v!==before.v)ch.push("view");if(after.open&&!before.open)ch.push("sheet-open:"+after.st);else if(!after.open&&before.open)ch.push("sheet-closed");else if(after.open&&after.s!==before.s)ch.push("sheet-change:"+after.st);
     if(after.ov!==before.ov)ch.push("overlay:"+after.ov);if(after.rest!==before.rest)ch.push("rest");if(after.y!==before.y)ch.push("scroll");if(after.cls!==before.cls)ch.push("cls");if(pg.dialogs.length)ch.push("dialog:"+pg.dialogs.join("|"));
     const r={ctx:ctxName,path:path.map(p=>p.a).join(">"),...it,ch,errs};res.push(r);
     if(errs.length||(!ch.length&&!it.pr&&!it.dis)) console.log((errs.length?"ERR ":"NOCHANGE ")+ctxName+" "+it.a+" '"+it.t+"' "+errs.join(";"));
     const opened=after.open&&(after.s!==before.s);
     if(opened&&depth<MAXD){const nctx="sheet:"+after.st;await explore([...path,{scope,a:it.a,k:it.k}],"sheet",depth+1,nctx)}
     if(Date.now()-t0>(+process.env.TL||540000)){console.log("TIME LIMIT");return}
   }}
 for(const t of tabs){if(ONLY&&t!==ONLY)continue;await explore([{scope:"main",a:"tab",k:tabs.indexOf(t)}],"main",1,"tab:"+t);fs.writeFileSync(OUT,JSON.stringify(res,null,1))}
 fs.writeFileSync(OUT,JSON.stringify(res,null,1));console.log("DONE clicks",res.length,"time",Math.round((Date.now()-t0)/1000)+"s");await b.close();})();
