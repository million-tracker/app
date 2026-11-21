const pw=require(require('child_process').execSync('npm root -g').toString().trim()+'/playwright');
const fs=require('fs');const H=fs.readFileSync(require('path').join(__dirname,'../../index.html'),'utf8');
const WD={2:[0,3],3:[0,2,4],4:[0,1,3,4],5:[0,1,2,3,4],6:[0,1,2,3,4,5]};
(async()=>{const b=await pw.chromium.launch();const out={};
for(const lang of ['uk','ru']){const c=await b.newContext({...pw.devices['iPhone 13']});await c.route('**/*',r=>{const u=r.request().url();if(u.startsWith('https://million-tracker.github.io/'))return r.fulfill({body:H,contentType:'text/html'});r.abort()});const p=await c.newPage();let errs=0;p.on('pageerror',e=>{errs++;console.log('ERR',e.message)});await p.goto('https://million-tracker.github.io/app/');await p.evaluate(l=>{localStorage.tb_lang=l;localStorage.tb_home='me'},lang);await p.reload();await p.waitForTimeout(800);
const clk=async(a,x)=>{await p.evaluate(([a,x])=>{const e=document.createElement('button');e.dataset.a=a;if(x!=null)e.dataset.x=x;document.body.appendChild(e);e.click();e.remove()},[a,x]);await p.waitForTimeout(60)};
await clk('consent');await clk('gopen2','auto');await clk('gsch','wd');await clk('gweeks','1');await clk('gst','2026-11-23');
const R={};
for(const sex of ['m','f'])for(const lvl of ['0','1','2'])for(const goal of ['mass','loss','dry','recomp'])for(const n of [2,3,4,5,6]){
 await clk('gsex',sex);await clk('glvl',lvl);await clk('ggoal',goal);
 for(let d=0;d<7;d++){const on=await p.evaluate(d=>document.querySelector('#sheetBody [data-a=gwd][data-x="'+d+'"]').getAttribute('aria-pressed')==='true',d);if(on!==WD[n].includes(d))await clk('gwd',String(d))}
 await clk('gst','2026-11-23');
 const r=await p.evaluate(()=>{const f=document.querySelector('#sheetBody [data-a=gswap]');if(!f)return null;const st=f.closest('.stack');
  const sp=[...document.querySelectorAll('#sheetBody *')].find(e=>e.children.length<3&&/^(По колу|По кругу)/.test(e.textContent.trim()));
  const vol=[...document.querySelectorAll('#sheetBody *')].find(e=>e.children.length==0&&/(робочих підходів|рабочих подходов)/.test(e.textContent));
  return {days:[...st.querySelectorAll(':scope>.plan')].map(pl=>({d:pl.querySelector('.eyebrow').textContent.trim(),t:pl.querySelector(':scope>b').textContent.trim(),ex:[...pl.querySelectorAll('li')].map(li=>[li.querySelector('b').textContent.trim().replace(/^\d+\.\s*/,''),(li.querySelector('.muted')||{}).textContent?.trim()||'',li.classList.contains('gsw')?1:0])})),vol:vol?vol.textContent.trim():''}});
 R[sex+lvl+goal+n]=r;}
 out[lang]=R;console.log(lang,'errs',errs,Object.keys(R).length);await c.close()}
fs.writeFileSync(require('path').join(__dirname,'prog_raw.json'),JSON.stringify(out));await b.close()})();
