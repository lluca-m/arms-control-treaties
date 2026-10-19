import requests,json,datetime,re
from hub_blocks import H,children,text
API='https://api.notion.com/v1'
LOG='3f62b9a41a3081979f69cb581b3c2b93'
AD='Date Adopted (When treaty text was finalized/agreed upon, usually at a conference or negotiation)'
OS='Opened for Signature (for multilateral, often same or shortly after adoption date)'
def P(pid): return requests.get(f'{API}/pages/{pid}',headers=H).json()['properties']
def val(p):
    t=p['type']; v=p[t]
    if t in('rich_text','title'): return ''.join(x['plain_text'] for x in v)
    if t=='select': return v['name'] if v else ''
    if t=='multi_select': return [o['name'] for o in v]
    if t=='date': return v['start'] if v else ''
    if t=='number': return v
    if t=='url': return v or ''
    if t=='unique_id': return f"{v.get('prefix')}-{v.get('number')}" if v and v.get('number') else ''
    return ''
def d(s):
    if not s: return ''
    y,m,dd=s.split('-'); return f"{int(dd)} {['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {y}"
def esc(s): return re.sub(r'([\\*~`$\[\]<>{}|^])',r'\\\1',str(s))
SKIP={'','Not applicable','None','None specified','None stated',None}
def _has_event(pid,etype):
    r=requests.post(f'{API}/databases/c474dab17e5e4b43bbf3a03f3493da73/query',headers=H,json={'filter':{'and':[{'property':'Instrument','relation':{'contains':pid}},{'property':'Event Type','select':{'equals':etype}}]},'page_size':1}).json()
    return bool(r.get('results'))
def keyfacts(pid):
    raw=P(pid); p={k:val(v) for k,v in raw.items()}
    rows=[]
    for prop,label in [('Interprets','Interprets'),('Amends','Amends'),('Protocol To','Protocol to'),('Interpreted By','Interpreted by'),('Amended By','Amended by'),('Has Protocols','Protocols')]:
        ids=[x['id'] for x in (raw.get(prop) or {}).get('relation',[])]
        if ids:
            links=[]
            for i in ids:
                t=P(i); nm=val(t['Treaty Name (Abbreviation/ Common Name)']) or val(t['Treaty Name (Full)'])
                links.append(f"[{nm}](https://www.notion.so/{i.replace('-','')})")
            rows.append((label,'; '.join(links)))
    if p['Record Type']=='Negotiation':
        rows.append(('Record',f"Negotiation, {p['Negotiation Status'].lower()}; no agreed treaty text"))
    else:
        form=p['Instrument Form']; lc=p['Legal Character']
        ps=re.sub(r' \(.*\)','',p['Participation Structure'] or '')
        fm='treaty' if form=='Treaty/Convention' else form.lower()
        rows.append(('Instrument',f"{ps} {fm}, {lc.lower()}" if ps else f"{fm[0].upper()+fm[1:]}, {lc.lower()}"))
        st=p['Instrument Status']
        if st not in SKIP: rows.append(('Status','Operative' if (st=='In force' and p['Legal Character']=='Politically binding') else st))
    if p[AD]: rows.append(('Adopted',d(p[AD])+(f", {', '.join(p['Adopted at:'])}" if False else '')))
    pol=p['Legal Character']=='Politically binding'
    if p[OS]: rows.append(('Opened for signature' if _has_event(pid,'Opening for signature') else 'Signed',d(p[OS])+(f", {p['Signed at:']}" if p['Signed at:'] else '')))
    if p['Date Entered into Force']: rows.append(('Entry into force',d(p['Date Entered into Force'])))
    if p['Expiration Date']: rows.append(('Ended',d(p['Expiration Date'])))
    if p['Number of Parties'] is None:
        part=requests.post(f'{API}/databases/{PDB}/query',headers=H,json={'filter':{'property':'Disarmament Treaties Database 1','relation':{'contains':pid}},'page_size':100}).json().get('results',[])
        if part:
            sig=sum(1 for x in part if val(x['properties']['Participation Type'])=='Original Signatory')
            acc=[val(x['properties']['Date of Accession'])[:4] for x in part if val(x['properties']['Date of Accession'])]
            yrs=sorted(set(acc)); yr=(' in '+', '.join(yrs)) if yrs else ''
            chk=f"; list checked {d(p['Parties As Of'])}" if p.get('Parties As Of') else ''
            rat=sum(1 for x in part if val(x['properties']['Method of Consent'])=='Ratification')
            ratt=f"{rat} ratifications; " if rat else ''
            acct=f"{len(acc)} accessions{yr}" if acc else 'no accessions'
            rows.append(('Listed participants',f"{len(part)} ({sig} original signatories; {ratt}{acct}{chk}); historical count, one row per participation as listed, not a count of current parties"))
    if p['Number of Parties'] is not None:
        asof=p.get('Parties As Of')
        lab='Participating states' if p['Legal Character']=='Politically binding' else 'Parties'
        rows.append((lab,f"{int(p['Number of Parties'])}"+(f" (as of {d(asof)})" if asof else '')))
    if p['Weapons/Systems Limited']: rows.append(('Covers',p['Weapons/Systems Limited']))
    ver=[x for x in p['Information Provisions']+p['Inspection & Access']+p['Monitoring Means Specified'] if x not in SKIP]
    if ver: rows.append(('Transparency and verification','; '.join(ver)))
    io=p['Institutional Oversight']
    if io not in SKIP: rows.append(('Institutional arrangements' if pol else 'Oversight',('Regular meetings of participating states' if (pol and io=='Treaty body or commission') else io)+(f"; {p['Consultation Mechanism'].lower()}" if p['Consultation Mechanism'] not in SKIP else '')))
    if p['Withdrawal Type'] not in SKIP:
        n=p['Withdrawal Notice (months)']
        wt={'Notice':'','Supreme interests (with notice)':'Supreme interests clause','Mutual consent only':'Mutual consent only'}.get(p['Withdrawal Type'],p['Withdrawal Type'])
        rows.append(('Withdrawal',', '.join(x for x in [wt,f"{int(n)} months' notice" if n else ''] if x) or p['Withdrawal Type']))
    if p['Treaty URL']:
        rep=p.get('Source Quality')=='Reproduction'
        rows.append(('Text' if rep else 'Official text',f"[{'Code text' if pol else 'Treaty text'}{' (reproduction)' if rep else ''}]({p['Treaty URL']})"))
    out='<table fit-page-width="true" header-column="true">\n'
    for a,b in rows:
        bb=b if b.startswith('[') and '](' in b else esc(b)
        out+=f'\t<tr>\n\t\t<td>{esc(a)}</td>\n\t\t<td>{bb}</td>\n\t</tr>\n'
    out+='</table>\nGenerated from the record\'s properties; edit the properties, not this table.'
    return out
def chunks(s): return [{'type':'text','text':{'content':s[k:k+1900]}} for k in range(0,len(s),1900)][:100]
def log(pid,entry,etype,detail):
    r=requests.post(f'{API}/pages',headers=H,json={'parent':{'database_id':LOG},'properties':{
      'Entry':{'title':[{'type':'text','text':{'content':entry[:200]}}]},'Instrument':{'relation':[{'id':pid}]},
      'Entry Type':{'select':{'name':etype}},'Date':{'date':{'start':datetime.date.today().isoformat()}},
      'Detail':{'rich_text':chunks(detail)}}})
    return r.status_code
def flat(bid,depth=0):
    out=[]
    for b in children(bid):
        t=text(b) if b['type'] not in ('child_database','table','divider') else ''
        if t.strip(): out.append('  '*depth+t)
        if b.get('has_children') and b['type'] not in ('child_database','child_page'): out+=flat(b['id'],depth+1)
    return out
def old_notes(pid):
    kids=children(pid); out=[]
    for b in kids:
        if b['type']=='divider' and out: pass
        if b['type']=='heading_2' and text(b)=='Provisions and obligations': break
        t=text(b) if b['type'] not in ('child_database','table','divider') else ''
        if t.strip(): out.append(t)
        if b.get('has_children') and b['type'] not in ('child_database','child_page'): out+=flat(b['id'],1)
    return '\n'.join(out)
def rt_md(s):
    out=[]
    for part in re.split(r'(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*)',s):
        if not part: continue
        m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',part)
        if m: out.append({'type':'text','text':{'content':m.group(1),'link':{'url':m.group(2)}}})
        elif part.startswith('**'): out.append({'type':'text','text':{'content':part[2:-2]},'annotations':{'bold':True}})
        else: out+=chunks(part)
    return out
def keyfacts_blocks(pid):
    md=keyfacts(pid)
    rows=re.findall(r'<td>(.*?)</td>\s*<td>(.*?)</td>',md,re.S)
    un=lambda s: re.sub(r'\\(.)',r'\1',s)
    tb={'type':'table','table':{'table_width':2,'has_column_header':False,'has_row_header':True,
        'children':[{'type':'table_row','table_row':{'cells':[rt_md(un(a)),rt_md(un(b))]}} for a,b in rows]}}
    note={'type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':"Generated from the record's properties; edit the properties, not this table."},'annotations':{'italic':True,'color':'gray'}}]}}
    return [tb]
def set_keyfacts(pid):
    kids=children(pid)
    i=next((k for k,b in enumerate(kids) if b['type']=='heading_2' and text(b)=='Key facts'),None)
    if i is None: return ('no Key facts heading yet','')
    j=i+1
    while j<len(kids) and kids[j]['type']!='heading_2':
        requests.delete(f"{API}/blocks/{kids[j]['id']}",headers=H); j+=1
    r=requests.patch(f"{API}/blocks/{pid}/children",headers=H,json={'children':keyfacts_blocks(pid),'after':kids[i]['id']})
    return r.status_code, r.text[:200] if not r.ok else ''

# ---- v3 write: safe clearing, idempotent rows and log, key facts resync ----
import writer2
def _q(db,pid):
    out=[];cur=None
    while True:
        b={'filter':{'property':'Instrument','relation':{'contains':pid}},'page_size':100}
        if cur: b['start_cursor']=cur
        r=requests.post(f'{API}/databases/{db}/query',headers=H,json=b).json()
        out+=r['results']
        if not r.get('has_more'): return out
        cur=r['next_cursor']
def _key(row,title_prop,extra):
    p=row['properties']; t=''.join(x['plain_text'] for x in p[title_prop]['title'])
    e=p[extra]; ev=(e.get('rich_text') and ''.join(x['plain_text'] for x in e['rich_text'])) if e['type']=='rich_text' else ((e['date'] or {}).get('start','')[:10] if e['type']=='date' else '')
    return (t.strip(), ev or '')
def upsert_rows(db,pid,items,f,title_prop,extra_prop,extra_json):
    existing={}
    for row in _q(db,pid): existing.setdefault(_key(row,title_prop,extra_prop),[]).append(row['id'])
    seen=set(); stats={'updated':0,'created':0,'archived':0,'fail':0}
    for x in items:
        ev=x.get(extra_json) or ''
        if extra_prop=='Date': ev=ev if len(ev)==10 else ''
        k=((x.get('provision') or x.get('event') or '').strip(), ev)
        props=f(x,pid)
        if k in existing and existing[k]:
            rid=existing[k].pop(0); seen.add(rid)
            r=requests.patch(f'{API}/pages/{rid}',headers=H,json={'properties':props}); stats['updated' if r.ok else 'fail']+=1
        else:
            r=requests.post(f'{API}/pages',headers=H,json={'parent':{'database_id':db},'properties':props}); stats['created' if r.ok else 'fail']+=1
    for ids in existing.values():
        for rid in ids:
            requests.patch(f'{API}/pages/{rid}',headers=H,json={'archived':True}); stats['archived']+=1
    return stats
def evt_props3(x,pid):
    p=writer2.evt_props(x,pid)
    d=x.get('date')
    if d and len(d)!=10:  # month or year only: never infer a day
        p.pop('Date',None); x.setdefault('date_precision','Month' if len(d)==7 else 'Year')
        if not x.get('date_as_reported'):
            M=['January','February','March','April','May','June','July','August','September','October','November','December']
            x['date_as_reported']=f"{M[int(d[5:7])-1]} {d[:4]}" if len(d)==7 else d
    if not d: p['Date']={'date':None}
    prec=x.get('date_precision') or ('Exact day' if d and len(d)==10 else 'Date unknown')
    p['Date Precision']={'select':{'name':prec}}
    p['Date as Reported']={'rich_text':chunks(x['date_as_reported'])} if x.get('date_as_reported') else {'rich_text':[]}
    return p
def upsert_log(pid,entry,etype,detail):
    # match on this writer's own entry title only, so entries made by other sessions (e.g. the 2021 coding-sheet migration) are never overwritten
    r=requests.post(f'{API}/databases/{LOG}/query',headers=H,json={'filter':{'and':[{'property':'Instrument','relation':{'contains':pid}},{'property':'Entry','title':{'equals':entry[:200]}}]}}).json()
    props={'Entry':{'title':[{'type':'text','text':{'content':entry[:200]}}]},'Instrument':{'relation':[{'id':pid}]},
      'Entry Type':{'select':{'name':etype}},'Date':{'date':{'start':datetime.date.today().isoformat()}},'Detail':{'rich_text':chunks(detail)}}
    if r['results']:
        cur=''.join(x['plain_text'] for x in r['results'][0]['properties']['Detail']['rich_text'])
        if cur==detail: return 'unchanged'
        return 'updated' if requests.patch(f"{API}/pages/{r['results'][0]['id']}",headers=H,json={'properties':props}).ok else 'fail'
    return 'created' if requests.post(f'{API}/pages',headers=H,json={'parent':{'database_id':LOG},'properties':props}).ok else 'fail'
CLEARABLE={'opened_for_signature':OS,'date_adopted':AD,'entry_into_force':'Date Entered into Force','date_ended':'Expiration Date',
 'signed_at':'Signed at:','depositary':'Depository','number_of_parties':'Number of Parties','number_of_signatories':'Number of Signatories',
 'parties_as_of':'Parties As Of','treaty_url':'Treaty URL','end_reason':'End Reason',
 'duration_years':'Duration (years)','review_conferences_held':'Number of review conferences held'}
def _empty(prop_type): return {'date':{'date':None},'rich_text':{'rich_text':[]},'number':{'number':None},'url':{'url':None},'select':{'select':None},'multi_select':{'multi_select':[]}}[prop_type]
def write3(pid,j,name,old_text=None):
    """Properties (null = leave as is), explicit clears, idempotent rows, log upsert, key-facts resync. Page prose is not touched."""
    i=j['instrument']; log=[]
    p=writer2.props(i)
    p.pop('Signatories & Dates',None)
    if i.get('parties_as_of'): p['Parties As Of']={'date':{'start':i['parties_as_of']}}
    schema=P(pid)
    for c in j.get('clear_fields') or []:   # [{"field": json key, "reason": ...}] - the ONLY way a value is erased
        prop=CLEARABLE.get(c['field'])
        if prop and prop in schema: p[prop]=_empty(schema[prop]['type']); log.append(f"cleared {prop}: {c.get('reason')}")
    rel={}
    for r in i.get('related') or []:
        tid=r.get('target_page_id')
        if not tid and r.get('target_id'):
            import json as _j
            tid=next((x['page_id'] for x in _j.load(open('/Users/laura/Library/CloudStorage/OneDrive-Personal/1_Research/4_Arms_Control_Treaties_Dataset/records/pilot2/rows_list.json')) if x['record_id']==r['target_id']),None)
        if not tid and r.get('target_id'): log.append(f"relation target {r['target_id']} not found")
        if tid: rel.setdefault(writer2.REL[r['relation']],[]).append({'id':tid})
    for k,v in rel.items(): p[k]={'relation':v}   # replaces the whole relation list, so reruns never duplicate
    rr=requests.patch(f'{API}/pages/{pid}',headers=H,json={'properties':p})
    if not rr.ok: return ['props '+rr.text[:300]]
    for n,x in enumerate(j['provisions'],1): x['_order']=n
    log.append(('prov',upsert_rows(writer2.PROV,pid,j['provisions'],lambda x,pid: prov_props3(x,pid),'Provision','Article','article')))
    log.append(('evt',upsert_rows(writer2.EVT,pid,j['events'],lambda x,pid: evt_props3(x,pid),'Event','Date','date')))
    log.append(('log-corr',upsert_log(pid,f'{name}: corrections to the earlier entry','Correction to earlier entry','\n'.join('- '+c for c in j.get('corrections',[])) or '(none)')))
    rn=j.get('research_notes') or [f"{u['field']}: {u['reason']}" for u in j.get('unverified',[])]
    log.append(('log-notes',upsert_log(pid,f'{name}: research notes','Research note','\n'.join('- '+x for x in rn) or '(none)')))
    if old_text is not None: log.append(('log-old',upsert_log(pid,f'{name}: earlier notes (unchecked)','Earlier notes (unchecked)',old_text)))
    log.append(('keyfacts',set_keyfacts(pid)[0]))
    return log
def resync_all_keyfacts():
    out=[]
    for row in writer2.all_rows(writer2.INST):
        if any(b['type']=='heading_2' and text(b)=='Key facts' for b in children(row['id'])): out.append(set_keyfacts(row['id'])[0])
    return out
MONTHS={m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
def sort_key(x):
    """YYYYMMDD; 00 for an unknown day or month. A sort aid only, never shown as a date."""
    d=x.get('date') or ''
    if len(d)>=4 and d[:4].isdigit():
        y=int(d[:4]); m=int(d[5:7]) if len(d)>=7 else 0; dd=int(d[8:10]) if len(d)==10 else 0
        return y*10000+m*100+dd
    rep=x.get('date_as_reported') or ''
    mm=re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})',rep)
    if mm and not rep.lower().startswith('date unknown'): return int(mm.group(2))*10000+MONTHS[mm.group(1)]*100
    yy=re.fullmatch(r'\s*(\d{4})\s*',rep)
    return int(yy.group(1))*10000 if yy else None
_evt3=evt_props3
RANK={'Negotiation round':0,'Adoption':1,'Opening for signature':2,'Entry into force':3}
def evt_props3(x,pid):
    p=_evt3(x,pid); k=sort_key(x)
    if k is not None: k=k+RANK.get(x.get('event_type'),5)/10
    if x.get('sort_key') is not None: k=x['sort_key']  # explicit placement for imprecise dates with a known sequence
    p['Sort Key']={'number':k}; return p
_prov=writer2.prov_props
def prov_props3(x,pid):
    p=_prov(x,pid)
    if x.get('_order') is not None: p['Order']={'number':x['_order']}
    return p

PDB='2942b9a41a308090b37ef980db47fad3'; CDB='d538b6bc3aed4da3a13ba8a2066f2184'
def write_participation(pid,rows,short,country_ids):
    """One Participation row per state; upserts on Title so reruns do not duplicate."""
    ex={}; cur=None
    while True:   # paginate: instruments can have more than 100 participation rows
        q={'filter':{'property':'Disarmament Treaties Database 1','relation':{'contains':pid}},'page_size':100}
        if cur: q['start_cursor']=cur
        res=requests.post(f'{API}/databases/{PDB}/query',headers=H,json=q).json()
        ex.update({val(r['properties']['Title']):r['id'] for r in res['results']})
        if not res.get('has_more'): break
        cur=res['next_cursor']
    out=[]
    for p in rows:
        title=f"{p.get('iso3') or p['state']} - {short}"
        props={'Title':{'title':[{'type':'text','text':{'content':title}}]},'Disarmament Treaties Database 1':{'relation':[{'id':pid}]},
          'Country':{'relation':[{'id':country_ids[p['state']]}]} if country_ids.get(p['state']) else {'relation':[]},
          'Participation Type':{'select':{'name':p['participation_type']}} if p.get('participation_type') else {'select':None},
          'Date Signed':{'date':{'start':p['date_signed']}} if p.get('date_signed') else {'date':None},
          'Entry into Force':{'date':{'start':p['entry_into_force']}} if p.get('entry_into_force') else {'date':None},
          'Date of Accession':{'date':{'start':p['date_of_accession']}} if p.get('date_of_accession') else {'date':None},
          'Date of Succession':{'date':{'start':p['date_of_succession']}} if p.get('date_of_succession') else {'date':None},
          'Current Status':{'select':{'name':p['current_status']}} if p.get('current_status') else {'select':None},
          'Method of Consent':{'select':{'name':p['method_of_consent']}} if p.get('method_of_consent') else {'select':None},
          'Data Entry Status':{'select':{'name':p.get('data_entry_status') or 'Needs Verification'}},
          'Notes':{'rich_text':chunks(p.get('notes') or '')}}
        if title in ex: r=requests.patch(f"{API}/pages/{ex[title]}",headers=H,json={'properties':props}); out.append(('updated',title,r.status_code))
        else: r=requests.post(f'{API}/pages',headers=H,json={'parent':{'database_id':PDB},'properties':props}); out.append(('created',title,r.status_code))
    return out
