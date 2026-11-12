"""Genera un PDF de una columna con texto seleccionable y enlaces reales."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialBold', italic='Arial', boldItalic='ArialBold')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='ArialBold',fontSize=25,leading=30,textColor=HexColor('#17243b'),spaceAfter=5))
styles.add(ParagraphStyle(name='RoleCV',fontName='Arial',fontSize=13,leading=18,textColor=HexColor('#245be0'),spaceAfter=10))
styles.add(ParagraphStyle(name='BodyCV',fontName='Arial',fontSize=9,leading=13,textColor=HexColor('#26354a'),spaceAfter=7))
styles.add(ParagraphStyle(name='SectionCV',fontName='ArialBold',fontSize=10,leading=14,textColor=HexColor('#245be0'),spaceBefore=9,spaceAfter=6))
styles.add(ParagraphStyle(name='TitleCV',fontName='ArialBold',fontSize=9.5,leading=13,textColor=HexColor('#17243b'),spaceBefore=4,spaceAfter=3))
story=[]
def add(text,style='BodyCV'):
    story.append(Paragraph(text,styles[style]))
def link(url,label):
    return f'<link href="{url}" color="#245be0">{label}</link>'

add('Vera Martín','NameCV')
add('Analista de Datos Junior','RoleCV')
add('Lima, Perú  |  +51 947 082 837  |  '+link('mailto:vera124486@gmail.com','vera124486@gmail.com'))
add(link('https://cvveramartin.web.app/','Portafolio: cvveramartin.web.app')+'  |  '+link('https://github.com/VeraMxrtin','GitHub: VeraMxrtin')+'  |  '+link('https://www.linkedin.com/in/vera-martin-40375b328/','LinkedIn'))
add('PERFIL PROFESIONAL','SectionCV')
add('Formación en Administración de Sistemas para la Transformación Digital en CERTUS, con enfoque en análisis de datos. En proyectos independientes he trabajado con SQL, tableros en Power BI y reportes en Excel con Power Query. Desarrollo aplicaciones con Python y flujos de automatización. Busco oportunidades junior en análisis de datos, operaciones y automatización.')
add('HABILIDADES TÉCNICAS','SectionCV')
add('<b>Análisis y bases de datos:</b> Python, Pandas, NumPy, SQL, MySQL, Excel y Power Query.<br/><b>Visualización:</b> Power BI, Matplotlib y D3.js.<br/><b>Modelado y desarrollo:</b> scikit-learn, Flask, Streamlit, SHAP, JavaScript, Git y GitHub.<br/><b>Automatización:</b> n8n e integración con WhatsApp Cloud API.')
add('PROYECTOS INDEPENDIENTES','SectionCV')
add('Análisis de datos y reportes | 2026','TitleCV')
add('Extracción y transformación de datos públicos con SQL, creación de tableros en Power BI y automatización de reportes en Excel con Power Query. Kaggle como fuente de datos y aprendizaje.')
add('Spotify-YouTube Predictor','TitleCV')
add('API con Flask y NumPy para estimar visualizaciones de YouTube a partir de 10 variables musicales y de reproducciones de Spotify. Interfaz web con D3.js. '+link('https://veraspotify.web.app/','Ver aplicación')+' · '+link('https://github.com/VeraMxrtin/Model-Spotify','Código del modelo'))
add('Predicción del precio del oro','TitleCV')
add('Modelo supervisado en Python con scikit-learn y tablero en D3.js para comparar valores históricos y predicciones. El tablero reporta R² = 0,952 y su PDF ≈ 0,93; diferencia pendiente de aclarar. '+link('https://veragoldprice.web.app/','Ver proyecto'))
add('Clasificación de cáncer de mama','TitleCV')
add('Proyecto educativo con Breast Cancer Wisconsin (según documentación), Python y Streamlit. La app carga un modelo Random Forest y muestra importancia de variables; SHAP se describe en el informe. Sin validación clínica ni uso diagnóstico. '+link('https://verapredictbreastcancer.web.app/','Ver proyecto'))
add('DESARROLLO Y EMPRENDIMIENTO','SectionCV')
add('<b>VeraFlow | 2026.</b> Iniciativa independiente: desarrollo de un CRM para comunicaciones y ventas; flujos con n8n para WhatsApp.<br/><b>MS Wisdom Press | 2025–2026.</b> Iniciativa de contenidos digitales y comercio electrónico con Shopify, analítica y automatización.<br/><b>Otros proyectos | 2025–2026.</b> Diseño web para TIKKY y proyectos personales; modelado de procesos BPMN con Bizagi Modeler y Bonita.')
add('FORMACIÓN ACADÉMICA','SectionCV')
add('<b>CERTUS</b> | Administración de Sistemas para la Transformación Digital.<br/>Periodo y estado académico pendientes de confirmación.')
doc=SimpleDocTemplate(str(ROOT/'img/Vera-Martin-CV.pdf'),pagesize=(595.28,841.89),rightMargin=45,leftMargin=45,topMargin=34,bottomMargin=30,title='Vera Martín | Analista de Datos Junior',author='Vera Martín')
doc.build(story)
print('CV generado: img/Vera-Martin-CV.pdf')
