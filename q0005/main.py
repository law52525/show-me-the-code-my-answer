import os
from PIL import Image
from q0013.main import run, image_path

ip5_size = (1136//2, 640//2)

if __name__ == '__main__':
    run()
    for file in os.listdir(image_path):
        path = image_path + os.sep + file
        image = Image.open(path).convert("RGB")
        image.thumbnail(ip5_size)
        image.save(path)
