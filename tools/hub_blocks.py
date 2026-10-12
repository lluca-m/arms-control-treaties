import json,requests,sys
TOK=json.load(open('/Users/laura/Library/CloudStorage/OneDrive-Personal/1_Research/1_Research_Pipeline/Data/api_keys.json'))['NOTION_TOKEN']
H={'Authorization':f'Bearer {TOK}','Notion-Version':'2022-06-28','Content-Type':'application/json'}
PAGE='1f32b9a41a308005ac7ce2240f82df6e'
def children(bid):
    out=[];cur=None
    while True:
        u=f'https://api.notion.com/v1/blocks/{bid}/children?page_size=100'+(f'&start_cursor={cur}' if cur else '')
        r=requests.get(u,headers=H,timeout=60).json()
        out+=r['results']
        if not r.get('has_more'): return out
        cur=r['next_cursor']
def text(b):
    t=b['type']; rt=b.get(t,{}).get('rich_text',[])
    return ''.join(x.get('plain_text','') for x in rt)
if __name__=='__main__':
    kids=children(PAGE)
    for i,b in enumerate(kids[:80]):
        print(i,b['id'],b['type'],b['has_children'],text(b)[:90])
