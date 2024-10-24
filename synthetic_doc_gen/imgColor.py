from PIL import Image, ImageOps
import os
import random


print(len((os.listdir("./output"))))


folder_path = "./output/"
random_list = []

for i in range(len((os.listdir(folder_path)))):
    r = random.randint(0, len((os.listdir(folder_path))) - 1)
    if r not in random_list:
        random_list.append(r)
        print(random_list)
    for y in random_list:
        img_path = folder_path + os.listdir(folder_path)[y]
        image = Image.open(img_path)
        new_image = ImageOps.grayscale(image)  
        new_image.save(img_path)

