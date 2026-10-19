import requests
import os,re,writer3,writer2,datetime
from hub_blocks import children
OUT=os.path.expanduser('~/Library/CloudStorage/OneDrive-Personal/1_Research/4_Arms_Control_Treaties_Dataset/pilot_review_2026-10-11')
os.makedirs(OUT,exist_ok=True)
import sys
R_ALL=[('St Petersburg','2572b9a41a3081469912f753c3878e7d'),('Rush-Bagot','28d2b9a41a30809f8e39cc46922d634e'),('Rush-Bagot 1939','3f72b9a41a30811fb40dca6bf3dd9277'),('INF','2572b9a41a308136adc6e7ca3f5c87ec'),('CCW','2572b9a41a308194abdde54fadf2525f'),('CCW Protocol IV','2572b9a41a30817a8a3ed306152a1465'),('HCoC','2572b9a41a308167b43eda865adf4835'),('FMCT','2572b9a41a3081e9890ff84f7ec55f24'),('Hague IV,1','2572b9a41a3081bda1ced0705eb04d22'),('Hague IV,2','2572b9a41a3081f48953f91995339cbe'),('Hague IV,3','2572b9a41a308171bb9ac54cd39127c7'),('Hague XIV','2572b9a41a308164aec2f0a25b7177d5'),('Washington Naval Treaty','2572b9a41a30819b82bfd726d06a1401'),('Geneva Protocol','2572b9a41a3081348693e1d8624662eb')]
PUBLIC=['Record ID','Treaty Name (Full)','Treaty Name (Abbreviation/ Common Name)','Record Type','Instrument Form','Legal Character','Instrument Status','Negotiation Status','Participation Structure',writer3.AD,writer3.OS,'Date Entered into Force','Expiration Date','End Reason','Signed at:','Depository','Number of Parties','Parties As Of','Number of Signatories','Key Non-Signatories','Weapon Families','Legal Subject Matter','Operating Environment','Region','Weapons/Systems Limited','Key Provisions','Information Provisions','Inspection & Access','Monitoring Means Specified','Institutional Oversight','Consultation Mechanism','Reporting Requirements','Enforcement Mechanisms (Sanctions/What happens if caught)','Dispute Resolution Mechanism','National authority requirements','Technical cooperation provisions','Third party roles specified','Reservations allowed/prohibited','Duration Type','Duration (years)','Duration Clause','Extension Type','Extension Clause','Withdrawal Type','Withdrawal Notice (months)','Withdrawal Clause','Amendment Procedure','Amendment Clause','Review Conferences','Review Interval (years)','Number of review conferences held','Entry into force requirements','Number of Articles','Word Count','Treaty complexity (word count, number of articles, annex/appendix/protocol)','Behavior Change Required','Historical Background & Motivation (Preamble)','Treaty URL','Source Quality','Last Verified']
def val(p):
    return writer3.val(p)
def rt(b):
    t=b.get(b['type'],{}).get('rich_text',[]); s=''
    for x in t:
        p=x['plain_text']; a=x.get('annotations',{})
        if a.get('bold'): p=f'**{p}**'
        if x.get('href'): p=f'[{p}]({x["href"]})'
        s+=p
    return s
def body(bid,depth=0):
    out=[];ind='  '*depth
    for b in children(bid):
        t=b['type']
        if t=='heading_2': out.append(f'\n## {rt(b)}')
        elif t=='heading_3': out.append(f'\n### {rt(b)}')
        elif t=='paragraph': out.append(ind+rt(b))
        elif t=='bulleted_list_item': out.append(f'{ind}- {rt(b)}')
        elif t=='numbered_list_item': out.append(f'{ind}1. {rt(b)}')
        elif t=='table':
            rows=children(b['id'])
            for k,r in enumerate(rows):
                cells=[''.join((f"[{x['plain_text']}]({x['href']})" if x.get('href') else x['plain_text']) for x in c) for c in r['table_row']['cells']]
                out.append('| '+' | '.join(c.replace('|','/') for c in cells)+' |')
                if k==0: out.append('|'+'---|'*len(cells))
        elif t=='toggle': out.append(f'{ind}▸ (collapsed) {rt(b)}  [linked database view; rows listed in the appendix below]')
        elif t=='child_database': pass
        elif t=='divider': out.append('---')
    return out
def cell(v):
    if isinstance(v,list): v='; '.join(v)
    return str(v if v not in (None,'') else '').replace('|','/').replace('\n',' ')
R=[x for x in R_ALL if len(sys.argv)<2 or x[0] in sys.argv[1:]]
for name,pid in R:
    P=writer3.P(pid); val={k:writer3.val(P[k]) for k in P}
    L=[f'# {val["Treaty Name (Full)"]}','',f'Export of the Notion record as of {datetime.date.today()} (pilot review). Notion: https://www.notion.so/{pid}','','## Properties (public set)','','| Property | Value |','|---|---|']
    L+=[f'| {k} | {cell(val.get(k))} |' for k in PUBLIC if k in val and val.get(k) not in ('',None,[])]
    L+=['','# Page body']+body(pid)
    prov=sorted(writer3._q(writer2.PROV,pid),key=lambda r:(r['properties']['Order']['number'] or 0))
    if prov:
        L+=['','# Appendix A: provision rows','','| # | Provision | Article | Restriction type | Weapon/activity | Bound parties | Value | Unit | Exceptions | Text or paraphrase |','|---|---|---|---|---|---|---|---|---|---|']
        for r in prov:
            v={k:writer3.val(r['properties'][k]) for k in r['properties']}
            L.append('| '+' | '.join(cell(v.get(k)) for k in ['Order','Provision','Article','Restriction Type','Weapon/Activity','Bound Parties','Value','Unit','Exceptions','Text or Paraphrase'])+' |')
    ev=sorted(writer3._q(writer2.EVT,pid),key=lambda r:(r['properties']['Sort Key']['number'] or 99999999))
    L+=['','# Appendix B: event rows','','| When | Event | Type | Precision | Actors | Attribution | Description | Source |','|---|---|---|---|---|---|---|---|']
    for r in ev:
        v={k:writer3.val(r['properties'][k]) for k in r['properties']}
        when=v['Date'] or v['Date as Reported'] or 'Date unknown'
        L.append('| '+' | '.join(cell(x) for x in [when,v['Event'],v['Event Type'],v['Date Precision'],v['Actors'],v['Attribution'],v['Description'],v['Source URL']])+' |')
    part=[];cur=None
    while True:   # paginate: instruments can have more than 100 participation rows
        q={'filter':{'property':'Disarmament Treaties Database 1','relation':{'contains':pid}},'page_size':100}
        if cur: q['start_cursor']=cur
        res=requests.post('https://api.notion.com/v1/databases/2942b9a41a308090b37ef980db47fad3/query',headers=__import__('hub_blocks').H,json=q).json()
        part+=res['results']
        if not res.get('has_more'): break
        cur=res['next_cursor']
    if part:
        L+=['','# Appendix D: participation rows','','| Row | Country link | Type | Method | Date signed | Date of accession | Date of succession | Entry into force | Current status | Data entry | Notes |','|---|---|---|---|---|---|---|---|---|---|---|']
        for x in part:
            v={k:writer3.val(p) for k,p in x['properties'].items()}
            v['Country']=', '.join(writer3.val(writer3.P(c['id'])['Country Name']) for c in x['properties']['Country']['relation']) or '(not linked)'
            L.append('| '+' | '.join(cell(v.get(k)) for k in ['Title','Country','Participation Type','Method of Consent','Date Signed','Date of Accession','Date of Succession','Entry into Force','Current Status','Data Entry Status','Notes'])+' |')
    L+=['','# Appendix C: internal editorial log (not public)','']
    for r in writer3._q(writer3.LOG,pid):
        v={k:writer3.val(r['properties'][k]) for k in r['properties']}
        L+=[f'## {v["Entry Type"]}: {v["Entry"]}','']+[('    '+ln) for ln in v['Detail'].split('\n')]+['']
    fn=f'{OUT}/{name}.md'; open(fn,'w').write('\n'.join(L)); print(fn, len(L))
