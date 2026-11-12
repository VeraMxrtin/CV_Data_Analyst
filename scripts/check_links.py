"""Comprueba los enlaces públicos de la web sin enviar formularios ni mensajes."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import json
import urllib.request
import urllib.error

ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls=set()
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            href=dict(attrs).get('href','')
            if href.startswith('https://'):self.urls.add(href)
parser=Links()
parser.feed((ROOT/'index.html').read_text(encoding='utf8'))
def check(url):
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 PortfolioLinkCheck'})
        with urllib.request.urlopen(request,timeout=25) as response:
            return {'url':url,'status':response.status,'final_url':response.url}
    except urllib.error.HTTPError as error:
        return {'url':url,'status':error.code,'note':'No se puede confirmar acceso público automatizado.'}
    except Exception as error:
        return {'url':url,'error':str(error)}
with ThreadPoolExecutor(max_workers=5) as pool:
    results=list(pool.map(check,sorted(parser.urls)))
(ROOT/'artifacts').mkdir(exist_ok=True)
(ROOT/'artifacts/link-results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
