import json
import threading
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'artifacts'
OUT.mkdir(exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_): pass
server = ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT/'dist')))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}'
results=[]
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='C:/Users/SISO/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',headless=True)
        page=browser.new_page()
        errors=[]
        page.on('pageerror',lambda e: errors.append(str(e)))
        page.on('console',lambda m: errors.append(m.text) if m.type=='error' else None)
        responses=[]
        page.on('response',lambda r: responses.append((r.url,r.status)))
        accessibility=[]
        for width,height in [(1440,1000),(1024,768),(768,1024),(390,844),(320,740)]:
            page.set_viewport_size({'width':width,'height':height})
            response=page.goto(base,wait_until='networkidle')
            assert response.status==200
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),f'Overflow {width}'
            assert page.locator('h1').count()==1
            if (ROOT/'.audit/axe.min.js').exists():
                page.add_script_tag(path=str(ROOT/'.audit/axe.min.js'))
                audit=page.evaluate("async () => await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}})")
                violations=[{'id':x['id'],'impact':x['impact'],'nodes':[n['target'] for n in x['nodes']]} for x in audit['violations']]
                accessibility.append({'viewport':width,'violations':violations})
                assert not violations,violations
            for image in page.locator('img').all():
                image.scroll_into_view_if_needed()
                assert image.evaluate('(img)=>img.complete && img.naturalWidth>0')
            page.locator('summary').first.click()
            assert page.locator('details').first.get_attribute('open') is not None
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            page.locator('summary').first.press('Enter')
            assert page.locator('details').first.get_attribute('open') is None
            page.locator('summary').first.evaluate('(el)=>el.blur()')
            page.evaluate('scrollTo(0,0)')
            page.screenshot(path=str(OUT/f'portfolio-{width}.png'),full_page=True,animations='disabled')
            if width<=780:
                toggle=page.locator('.menu-toggle')
                assert not page.locator('nav').is_visible()
                toggle.click()
                assert toggle.get_attribute('aria-expanded')=='true'
                page.keyboard.press('Escape')
                assert toggle.get_attribute('aria-expanded')=='false'
                assert toggle.evaluate('(el)=>el===document.activeElement')
                toggle.click()
                page.locator('nav a[href="#projects"]').click()
                assert not page.locator('nav').is_visible()
            results.append({'viewport':width,'overflow':False,'images':'ok','details_keyboard':'ok','navigation':'ok'})
        page.goto(base,wait_until='networkidle')
        page.keyboard.press('Tab')
        assert page.locator('.skip-link').evaluate('(el)=>el===document.activeElement')
        page.keyboard.press('Enter')
        assert page.evaluate('location.hash')=='#main'
        with page.expect_download() as download:
            page.locator('.hero-actions a[download]').click()
        item=download.value
        assert item.suggested_filename=='Vera-Martin-CV.pdf'
        item.save_as(str(OUT/'downloaded-cv.pdf'))
        assert (OUT/'downloaded-cv.pdf').read_bytes()==(ROOT/'img/Vera-Martin-CV.pdf').read_bytes()
        page.emulate_media(reduced_motion='reduce')
        assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
        assert not errors,errors
        assert all(status<400 for _,status in responses),responses
        browser.close()
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='C:/Users/SISO/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',headless=True)
        context=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
        page=context.new_page()
        page.goto(base)
        assert page.locator('nav').is_visible()
        page.locator('summary').first.click()
        assert page.locator('details').first.get_attribute('open') is not None
        browser.close()
    report={'viewports':results,'accessibility':accessibility,'console_errors':errors,'http_errors':[],'pdf_download':'ok','skip_link':'ok','reduced_motion':'ok','without_javascript':'ok'}
    (OUT/'browser-results.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps(report,indent=2))
finally:
    server.shutdown()
    server.server_close()
