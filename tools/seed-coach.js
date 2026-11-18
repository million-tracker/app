const d=n=>{const x=new Date();x.setDate(x.getDate()+n);return x.toISOString().slice(0,10)};
localStorage.setItem("tb_home","coach");
localStorage.setItem("tb_cl",JSON.stringify([{n:"Наташа",at:Date.now()-864e5*30},{n:"Олег",at:Date.now()-864e5*10}]));
const P=JSON.parse(localStorage.getItem("tb_plans")||"[]");const base=P[0];
const mk=(id,who,date,extra)=>Object.assign(JSON.parse(JSON.stringify(base)),{id,who,date},extra||{});
P.push(mk("pcT","Наташа",d(0)),mk("pcP","Наташа",d(-2)),mk("pcF","Наташа",d(3)),mk("pcS","Олег",d(1),{sent:1,chg:1}));
localStorage.setItem("tb_plans",JSON.stringify(P));
