import urllib.request, urllib.error, json
from pathlib import Path
from pypdf import PdfReader
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.audit'
sources={
 'gold-doc.pdf':'https://veragoldprice.web.app/assets/documentacion_data_web_oro.pdf',
 'cancer-doc.pdf':'https://verapredictbreastcancer.web.app/assets/Document_ML_Cancer_mama.pdf',
 'axe.min.js':'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js',
}
for name,url in sources.items():
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'PortfolioEvidenceReview'})
        with urllib.request.urlopen(request,timeout=30) as r:
            (OUT/name).write_bytes(r.read())
        if name.endswith('.pdf'):
            reader=PdfReader(OUT/name)
            text='\n'.join(p.extract_text() or '' for p in reader.pages)
            (OUT/(name+'.txt')).write_text(text,encoding='utf8')
        print(name,'OK')
    except Exception as e:print(name,type(e).__name__,str(e)[:160])
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='C:/Users/SISO/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',headless=True)
    page=browser.new_page(viewport={'width':1440,'height':1000})
    # Captura de la comparación de precios, evitando los indicadores ambiguos del hero original.
    page.goto('https://veragoldprice.web.app/',wait_until='networkidle')
    page.get_by_text('Predicción vs Precio Real',exact=False).first.scroll_into_view_if_needed()
    page.screenshot(path=str(OUT/'gold-chart.png'),animations='disabled')
    browser.close()
