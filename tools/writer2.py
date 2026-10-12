import requests,json,datetime,re
from hub_blocks import H,children,text
from writer import rt,md_blocks,T,S,M,D,N,AD,OS
INST='2172b9a41a3080798862e526c0451113'; PROV='1be0ad26c4134f6da434cc59d7c5e394'; EVT='c474dab17e5e4b43bbf3a03f3493da73'
API='https://api.notion.com/v1'
REL={'protocol_to':'Protocol To','amends':'Amends','interprets':'Interprets','replaces':'Replaces','negotiated_alongside':'Negotiated Alongside','produced_by':'Produced By'}
def U(v): return {'url':v} if v else None
def all_rows(db):
    out=[];cur=None
    while True:
        b={'page_size':100}; 
        if cur: b['start_cursor']=cur
        r=requests.post(f'{API}/databases/{db}/query',headers=H,json=b).json()
        out+=r['results']
        if not r.get('has_more'): return out
        cur=r['next_cursor']
def names(p):
    pr=p['properties']
    a=''.join(x['plain_text'] for x in pr['Treaty Name (Full)']['title'])
    b=''.join(x['plain_text'] for x in pr['Treaty Name (Abbreviation/ Common Name)']['rich_text'])
    return a,b
_ROWS=None
def lookup(target):
    global _ROWS
    if _ROWS is None: _ROWS=all_rows(INST)
    t=target.lower().strip(); hits=[]
    for p in _ROWS:
        a,b=names(p)
        if t in (a.lower(),b.lower()) or (b and b.lower() in t.split('(')[-1].rstrip(')').lower().split(', ')) : hits.append(p['id'])
    if not hits:
        for p in _ROWS:
            a,b=names(p)
            if a and (a.lower() in t or t in a.lower()): hits.append(p['id'])
    return list(dict.fromkeys(hits))
def props(i):
    p={
     'Treaty Name (Full)':{'title':rt(i.get('full_name'))} if i.get('full_name') else None,
     'Treaty Name (Abbreviation/ Common Name)':T(i.get('short_name')),
     'Record Type':S(i.get('record_type')),'Instrument Form':S(i.get('instrument_form')),
     'Legal Character':S(i.get('legal_character')),'Instrument Status':S(i.get('instrument_status')),
     'Negotiation Status':S(i.get('negotiation_status')),
     AD:D(i.get('date_adopted')),OS:D(i.get('opened_for_signature')),
     'Date Entered into Force':D(i.get('entry_into_force')),'Expiration Date':D(i.get('date_ended')),
     'End Reason':S(i.get('end_reason')),
     'Participation Structure':S(i.get('participation_structure')),
     'Region':M(i.get('geographic_coverage')),'Operating Environment':M(i.get('operating_environment')),
     'Weapon Families':M(i.get('weapon_families')),'Legal Subject Matter':M(i.get('legal_subject_matter')),
     'Signed at:':T(i.get('signed_at')),'Depository':T(i.get('depositary')),
     'Number of Parties':N(i.get('number_of_parties')),'Number of Signatories':N(i.get('number_of_signatories')),
     'Signatories & Dates':T(f"Counts as of {i['parties_as_of']}" if i.get('parties_as_of') else None),
     'Key Non-Signatories':T(i.get('key_non_parties')),
     'Information Provisions':M(i.get('information_provisions')),'Inspection & Access':M(i.get('inspection_access')),
     'Monitoring Means Specified':M(i.get('monitoring_means_specified')),
     'Institutional Oversight':S(i.get('institutional_oversight')),'Consultation Mechanism':S(i.get('consultation_mechanism')),
     'Reporting Requirements':S(i.get('reporting_requirements')),
     'Enforcement Mechanisms (Sanctions/What happens if caught)':S(i.get('enforcement')),
     'Dispute Resolution Mechanism':S(i.get('dispute_resolution')),'National authority requirements':S(i.get('national_authority')),
     'Technical cooperation provisions':S(i.get('technical_cooperation')),'Third party roles specified':S(i.get('third_party_roles')),
     'Reservations allowed/prohibited':S(i.get('reservations')),
     'Duration Type':S(i.get('duration_type')),'Duration (years)':N(i.get('duration_years')),'Duration Clause':T(i.get('duration_clause')),
     'Extension Type':S(i.get('extension_type')),'Extension Clause':T(i.get('extension_clause')),
     'Withdrawal Type':S(i.get('withdrawal_type')),'Withdrawal Notice (months)':N(i.get('withdrawal_notice_months')),'Withdrawal Clause':T(i.get('withdrawal_clause')),
     'Amendment Procedure':S(i.get('amendment_procedure')),'Amendment Clause':T(i.get('amendment_clause')),
     'Review Conferences':S(i.get('review_conferences')),'Review Interval (years)':N(i.get('review_interval_years')),
     'Number of review conferences held':N(i.get('review_conferences_held')),
     'Entry into force requirements':T(i.get('entry_into_force_requirements')),
     'Number of Articles':N(i.get('number_of_articles')),'Word Count':N(i.get('word_count')),
     'Treaty complexity (word count, number of articles, annex/appendix/protocol)':T(i.get('count_basis')),
     'Weapons/Systems Limited':T(i.get('weapons_systems_limited')),'Key Provisions':T(i.get('key_provisions')),
     'Behavior Change Required':T(i.get('behavior_change')),
     'Historical Background & Motivation (Preamble)':T(i.get('historical_background')),
     'Treaty URL':U(i.get('treaty_url')),'Source Quality':S(i.get('source_quality')),
     'Last Verified':{'date':{'start':datetime.date.today().isoformat()}},
    }
    return {k:v for k,v in p.items() if v is not None}
def clear_children(db,pid):
    # archive earlier generated rows for this instrument so reruns replace, not stack
    r=requests.post(f'{API}/databases/{db}/query',headers=H,json={'filter':{'property':'Instrument','relation':{'contains':pid}},'page_size':100}).json()
    for row in r['results']: requests.patch(f"{API}/pages/{row['id']}",headers=H,json={'archived':True})
    return len(r['results'])
def prov_props(x,pid):
    return {k:v for k,v in {
     'Provision':{'title':rt(x.get('provision'))},'Instrument':{'relation':[{'id':pid}]},
     'Article':T(x.get('article')),'Weapon/Activity':M(x.get('weapon_activity')),
     'Restriction Type':S(x.get('restriction_type')),'Value':N(x.get('value')),'Unit':T(x.get('unit')),
     'Bound Parties':S(x.get('bound_parties')),'Bound Parties Detail':T(x.get('bound_parties_detail')),
     'Geographic Scope':T(x.get('geographic_scope')),'Exceptions':T(x.get('exceptions')),
     'Effective From':D(x.get('effective_from')),'Effective Until':D(x.get('effective_until')),
     'Text or Paraphrase':T(x.get('text_or_paraphrase')),'Source URL':U(x.get('source_url')),'Locator':T(x.get('locator'))}.items() if v is not None}
def evt_props(x,pid):
    return {k:v for k,v in {
     'Event':{'title':rt(x.get('event'))},'Instrument':{'relation':[{'id':pid}]},
     'Date':D(x.get('date')),'Effective Date':D(x.get('effective_date')),'Event Type':S(x.get('event_type')),
     'Actors':T(x.get('actors')),'Attribution':T(x.get('attribution')),'Description':T(x.get('description')),
     'Source URL':U(x.get('source_url')),'Locator':T(x.get('locator'))}.items() if v is not None}
def body(pid,j):
    kids=children(pid)
    idx=next((k for k,b in enumerate(kids) if b['type']=='heading_2' and text(b)=='Provisions and obligations'),None)
    if idx is not None:
        if idx>0 and kids[idx-1]['type']=='divider': idx-=1
        for b in kids[idx:]: requests.delete(f"{API}/blocks/{b['id']}",headers=H)
    unv=j.get('unverified') or []
    unv_md='\n'.join(f"- {u.get('field')}: {u.get('reason')}" for u in unv) or '- None'
    cor=j.get('corrections') or []
    cor_md='\n'.join(f"- {c}" for c in cor) or '- None'
    blocks=[{'type':'divider','divider':{}},{'type':'heading_2','heading_2':{'rich_text':rt('Provisions and obligations')}}]+md_blocks(j.get('section_provisions_md'))+\
      [{'type':'heading_2','heading_2':{'rich_text':rt('History, compliance and sources')}}]+md_blocks(j.get('section_history_md'))+\
      [{'type':'heading_3','heading_3':{'rich_text':rt('Fields left blank or qualified')}}]+md_blocks(unv_md)+\
      [{'type':'heading_3','heading_3':{'rich_text':rt('Corrections to the earlier entry')}}]+md_blocks(cor_md)+\
      [{'type':'paragraph','paragraph':{'rich_text':rt(f'Researched and entered {datetime.date.today().isoformat()}. Structured provisions and dated events are in the Treaty Provisions and Treaty Events databases.')}}]
    for k in range(0,len(blocks),90):
        a=requests.patch(f'{API}/blocks/{pid}/children',headers=H,json={'children':blocks[k:k+90]})
        if a.status_code!=200: return 'body '+a.text[:300]
    return 'ok'
def write(pid,j):
    i=j['instrument']; log=[]
    p=props(i)
    rels={}
    for r in i.get('related') or []:
        ids=lookup(r['target'])
        if len(ids)==1: rels.setdefault(REL[r['relation']],[]).append({'id':ids[0]})
        else: log.append(f"relation {r['relation']} -> {r['target']}: {len(ids)} matches, not set")
    for k,v in rels.items(): p[k]={'relation':v}
    r=requests.patch(f'{API}/pages/{pid}',headers=H,json={'properties':p})
    if r.status_code!=200: return ['props '+r.text[:400]]
    log.append(f"archived old: prov {clear_children(PROV,pid)}, evt {clear_children(EVT,pid)}")
    for db,items,f in [(PROV,j['provisions'],prov_props),(EVT,j['events'],evt_props)]:
        for x in items:
            a=requests.post(f'{API}/pages',headers=H,json={'parent':{'database_id':db},'properties':f(x,pid)})
            if a.status_code!=200: log.append(f"row fail {x.get('provision') or x.get('event')}: {a.text[:200]}")
    log.append('body '+body(pid,j))
    return log
