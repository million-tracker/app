import json,os
H=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(H,'prog_raw.json')))
WDN={'Пн':0,'Вт':1,'Ср':2,'Чт':3,'Пт':4,'Сб':5,'Нд':6,'Вс':6}
for L in d:
  names=[];N={};days=[];D={};C={}
  def ni(s):
    if s not in N:N[s]=len(names);names.append(s)
    return N[s]
  for k,r in d[L].items():
    out=[]
    for x in r['days']:
      sig=json.dumps([ni(x['t'])]+[[ni(e[0]),ni(e[1]),e[2]] for e in x['ex']])
      if sig not in D:D[sig]=len(days);days.append(json.loads(sig))
      out.append([WDN[x['d'][:2]],D[sig]])
    C[k]=[ni(r['vol']),out]
  json.dump({'n':names,'d':days,'c':C},open(os.path.join(H,'prog_'+L+'.json'),'w'),ensure_ascii=False,separators=(',',':'))
print('packed')
