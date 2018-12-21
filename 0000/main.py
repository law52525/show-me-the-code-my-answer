from random import randint
from PIL import Image, ImageDraw, ImageFont

image = Image.open('head.png')
width, height = image.size
font = ImageFont.truetype('Arial.ttf', height // 2)
draw = ImageDraw.Draw(image)
draw.text((width - 150, -30), str(randint(1, 9)), fill=(220, 20, 60), font=font)
# print(draw.textsize(str(randint(1, 9)), font=font))
image.show()
