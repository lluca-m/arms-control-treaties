import json,writer3,writer2,requests
from hub_blocks import H
R={'inf':('2572b9a4-1a30-8136-adc6-e7ca3f5c87ec','INF'),'ccw':('2572b9a4-1a30-8194-abdd-e54fadf2525f','CCW'),'ccwp4':('2572b9a4-1a30-817a-8a3e-d306152a1465','CCW Protocol IV'),'hcoc':('2572b9a4-1a30-8167-b43e-da865adf4835','HCoC'),'fmct':('2572b9a4-1a30-81e9-890f-f84f7ec55f24','FMCT')}
RELS=['Protocol To','Amends','Replaces','Negotiated Alongside','Produced By','Has Protocols']
def snap():
    s={}
    for f,(pid,_) in R.items():
        P=writer3.P(pid)
        s[f]={'prov':sorted(r['id'] for r in writer3._q(writer2.PROV,pid)),'evt':sorted(r['id'] for r in writer3._q(writer2.EVT,pid)),
              'log':sorted(r['id'] for r in writer3._q(writer3.LOG,pid)),'rels':{k:sorted(x['id'] for x in P[k]['relation']) for k in RELS},
              'kf':[c['table_row']['cells'][1][0]['plain_text'] if c['table_row']['cells'][1] else '' for b in writer3.children(pid) if b['type']=='table' for c in writer3.children(b['id'])]}
    return s
def run():
    for f,(pid,nm) in R.items():
        print(f, writer3.write3(pid,json.load(open(f'pilot2/{f}.json')),nm))
