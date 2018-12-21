from random import randint, choice
from PIL import Image, ImageFont, ImageDraw, ImageFilter


def random_char():
    return chr(choice(list(range(65, 90 + 1)) + list(range(97, 122 + 1)) + list(range(48, 57 + 1))))


def random_color():
    return randint(64, 255), randint(64, 255), randint(64, 255)


def random_color2():
    return randint(32, 127), randint(32, 127), randint(32, 127)


if __name__ == '__main__':
    height = 60
    width = height * 4
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_color())
    for t in range(4):
        draw.text((height * t + 10, 10), random_char(), font=font, fill=random_color2())
    image = image.filter(ImageFilter.BLUR)  # 模糊
    image.show()
