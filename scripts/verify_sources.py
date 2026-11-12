"""Consulta evidencias públicas; no modifica sitios ni envía formularios."""
import json
import urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.audit'
OUT.mkdir(exist_ok=True)
def get(url):
    request=urllib.request.Request(url,headers={'User-Agent':'PortfolioEvidenceReview'})
    return urllib.request.urlopen(request,timeout=30).read()
for repo in ['Model-Spotify','App_breast_cancer','data_web_breastcancer']:
    try:
        tree=json.loads(get(f'https://api.github.com/repos/VeraMxrtin/{repo}/git/trees/HEAD?recursive=1'))
        (OUT/f'{repo}-tree.json').write_text(json.dumps(tree),encoding='utf8')
        paths=[x['path'] for x in tree.get('tree',[]) if x['path'].lower().endswith(('.py','.ipynb','.md')) and x.get('size',0)<3000000]
        print(repo,paths)
        for n,path in enumerate(paths[:12]):
            data=get(f'https://raw.githubusercontent.com/VeraMxrtin/{repo}/HEAD/{urllib.parse.quote(path)}')
            (OUT/f'{repo}-{n}.txt').write_bytes(data)
    except Exception as e: print(repo,type(e).__name__,str(e))
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='C:/Users/SISO/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',headless=True)
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    for name,url in [('spotify','https://veraspotify.web.app/'),('gold','https://veragoldprice.web.app/'),('cancer','https://verapredictbreastcancer.web.app/')]:
        try:
            response=page.goto(url,wait_until='networkidle',timeout=45000)
            page.screenshot(path=str(OUT/f'{name}-live.png'),animations='disabled')
            print(name,response.status)
        except Exception as e: print(name,type(e).__name__,str(e)[:200])
    browser.close()
