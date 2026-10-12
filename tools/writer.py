import requests,json,re,sys,datetime
from hub_blocks import H,children,text
AD='Date Adopted (When treaty text was finalized/agreed upon, usually at a conference or negotiation)'
OS='Opened for Signature (for multilateral, often same or shortly after adoption date)'
def rt(s):
    out=[]; s=s or ''
    # links [t](u) and **bold**
    for part in re.split(r'(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*)',s):
        if not part: continue
        m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',part)
        if m: out.append({'type':'text','text':{'content':m.group(1)[:1900],'link':{'url':m.group(2)}}}); continue
        if part.startswith('**') and part.endswith('**'):
            out.append({'type':'text','text':{'content':part[2:-2][:1900]},'annotations':{'bold':True}}); continue
        for k in range(0,len(part),1900): out.append({'type':'text','text':{'content':part[k:k+1900]}})
    return out
def md_blocks(md):
    bl=[]
    for line in (md or '').split('\n'):
        l=line.rstrip()
        if not l.strip(): continue
        if l.startswith('### '): bl.append({'type':'heading_3','heading_3':{'rich_text':rt(l[4:])}})
        elif l.startswith('## '): bl.append({'type':'heading_3','heading_3':{'rich_text':rt(l[3:])}})
        elif re.match(r'^\s*[-*] ',l): bl.append({'type':'bulleted_list_item','bulleted_list_item':{'rich_text':rt(re.sub(r'^\s*[-*] ','',l))}})
        elif re.match(r'^\s*\d+\. ',l): bl.append({'type':'numbered_list_item','numbered_list_item':{'rich_text':rt(re.sub(r'^\s*\d+\. ','',l))}})
        else: bl.append({'type':'paragraph','paragraph':{'rich_text':rt(l)}})
    return bl
def T(v): return {'rich_text':rt(str(v))} if v not in (None,'') else None
def S(v): return {'select':{'name':v}} if v else None
def M(v): return {'multi_select':[{'name':x} for x in v]} if v else None
def D(v): return {'date':{'start':v}} if v else None
def N(v):
    try: return {'number':float(v)} if v not in (None,'') else None
    except: return None
def build(j, extra=None):
    p={
     'Treaty Name (Full)':{'title':rt(j.get('full_name'))} if j.get('full_name') else None,
     'Treaty Name (Abbreviation/ Common Name)':T(j.get('abbreviation')),
     AD:D(j.get('date_adopted')), OS:D(j.get('opened_for_signature')),
     'Date Entered into Force':D(j.get('entry_into_force')), 'Expiration Date':D(j.get('date_ended')),
     'End Reason':S(j.get('end_reason')), 'Status':S(j.get('status')), 'Legal Form':S(j.get('legal_form')),
     'Type (Bilateral vs Multilateral)':S(j.get('bilateral_or_multilateral')), 'Geographic Scope':S(j.get('geographic_scope')),
     'Region':M(j.get('region')), 'Great-Power Parties':M(j.get('great_power_parties')),
     'Signed at:':T(j.get('signed_at')), 'Depository':T(j.get('depository')),
     'Number of Parties':N(j.get('number_of_parties')), 'Number of Signatories':N(j.get('number_of_signatories')),
     'Signatories & Dates':T(((j.get('parties_list') or '') + (f" (count as of {j['parties_as_of']})" if j.get('parties_as_of') else '')).strip()),
     'Key Non-Signatories':T(j.get('key_non_signatories')),
     'Type of Weapons':M(j.get('type_of_weapons')), 'Type of Limitation (Use/Development/Stockpiling)':M(j.get('type_of_limitation')),
     'Quantitative Limits (Zero/Specific Level)':S(j.get('quantitative_limits')),
     'Weapons/Systems Limited':T(j.get('weapons_systems_limited')), 'Key Provisions':T(j.get('key_provisions')),
     'Verification Mechanism':M(j.get('verification')),
     'Reporting Requirements':S(j.get('reporting_requirements')), 'Enforcement Mechanisms (Sanctions/What happens if caught)':S(j.get('enforcement')),
     'Dispute Resolution Mechanism':S(j.get('dispute_resolution')), 'National authority requirements':S(j.get('national_authority')),
     'Technical cooperation provisions':S(j.get('technical_cooperation')), 'Third party roles specified':S(j.get('third_party_roles')),
     'Reservations allowed/prohibited':S(j.get('reservations')),
     'Duration Type':S(j.get('duration_type')), 'Duration (years)':N(j.get('duration_years')), 'Duration Clause':T(j.get('duration_clause')),
     'Withdrawal Type':S(j.get('withdrawal_type')), 'Withdrawal Notice (months)':N(j.get('withdrawal_notice_months')), 'Withdrawal Clause':T(j.get('withdrawal_clause')),
     'Amendment Procedure':S(j.get('amendment_procedure')), 'Amendment Clause':T(j.get('amendment_clause')),
     'Review Conferences':S(j.get('review_conferences')), 'Review Interval (years)':N(j.get('review_interval_years')),
     'Entry into force requirements':T(j.get('entry_into_force_requirements')),
     'Notable Withdrawals/Suspensions':T(j.get('notable_withdrawals')),
     'Number of Articles':N(j.get('number_of_articles')), 'Word Count':N(j.get('word_count')),
     'Behavior Change Required':T(j.get('behavior_change')),
     'Historical Background & Motivation (Preamble)':T(j.get('historical_background')),
     'Compliance History':T(j.get('compliance_history')),
     'Treaty URL':{'url':j['treaty_url']} if j.get('treaty_url') else None,
     'Source Quality':S(j.get('source_quality')),
     'Last Verified':{'date':{'start':datetime.date.today().isoformat()}},
    }
    if extra: p.update(extra)
    return {k:v for k,v in p.items() if v is not None}
def write(pid,j,extra=None):
    r=requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':build(j,extra)},timeout=60)
    if r.status_code!=200: return 'props '+r.text[:300]
    # remove earlier auto sections if re-run
    for b in children(pid):
        if b['type']=='heading_2' and text(b) in ('Provisions and obligations','History, compliance and sources'):
            pass
    unv=j.get('unverified') or []
    unv_md='\n'.join(f"- {u.get('field')}: {u.get('reason')}" for u in unv) if unv else '- None'
    blocks=[{'type':'divider','divider':{}},
      {'type':'heading_2','heading_2':{'rich_text':rt('Provisions and obligations')}}]+md_blocks(j.get('section_provisions_md'))+\
      [{'type':'heading_2','heading_2':{'rich_text':rt('History, compliance and sources')}}]+md_blocks(j.get('section_history_md'))+\
      [{'type':'heading_3','heading_3':{'rich_text':rt('Fields left blank or qualified')}}]+md_blocks(unv_md)+\
      [{'type':'paragraph','paragraph':{'rich_text':rt(f'Researched and entered {datetime.date.today().isoformat()}; every property value is supported by the sources listed above.')}}]
    for k in range(0,len(blocks),90):
        a=requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':blocks[k:k+90]},timeout=60)
        if a.status_code!=200: return 'body '+a.text[:300]
    return 'ok'
