from django.shortcuts import render, redirect
from .models import ImageModel
from PIL import Image, ImageDraw,ImageFont
import uuid

def copyright_apply(input_path,text)->str:
    photo = Image.open(input_path)
    w,h = photo.size
    drawing = ImageDraw.Draw(photo)
    text = f"© {text}  "
    font = ImageFont.truetype('segoesc.ttf',68)
    text_w,text_h = drawing.textsize(text, font)
    pos = w - text_w, (h - text_h) - 50
    c_text = Image.new('RGB',(text_w, text_h), color="#000")
    drawing.text((0, 0), text, file="#fff", font = font)

    # input
    c_text.putalpha(100)
    # output
    photo.paste(c_text,pos,c_text)

    file_name = f'{uuid.uuid4()}.png'
    output_path = f'public/static/output/{file_name}'
    photo.save(output_path)

    return f'http://127.0.0.1:8000/media/output/{file_name}'

def index(request):
    if request.method == "POST":
        image = request.FILES['image']
        watermark_text = request.POST.get('watermark_text')
        image = ImageModel.objects.create(image = image, watermark_text=watermark_text)
        output_path = copyright_apply(f'public/static/{image.image}',watermark_text)
        return redirect(output_path)
    return render(request,'index.html')
