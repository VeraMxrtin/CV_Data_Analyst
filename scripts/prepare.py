from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
for source, name, size in [('fotocv.png','portrait.webp',(640,854))]:
    image = Image.open(root/'img'/source).convert('RGB')
    image.thumbnail(size)
    image.save(root/'img'/name, 'WEBP', quality=85)
canvas = Image.new('RGB',(1200,630),'#f5f7fb')
draw = ImageDraw.Draw(canvas)
font_path = 'C:/Windows/Fonts/arial.ttf'
draw.rectangle((64,72,72,558),fill='#245be0')
draw.text((110,115),'VERA MARTÍN',font=ImageFont.truetype(font_path,72),fill='#14203b')
draw.text((110,230),'Analista de Datos Junior',font=ImageFont.truetype(font_path,46),fill='#245be0')
draw.text((110,340),'Análisis. Visualización. Automatización.',font=ImageFont.truetype(font_path,32),fill='#48566e')
draw.text((110,490),'Python  /  SQL  /  Power BI  /  Excel',font=ImageFont.truetype(font_path,30),fill='#14203b')
canvas.save(root/'img/social.jpg',quality=90)
