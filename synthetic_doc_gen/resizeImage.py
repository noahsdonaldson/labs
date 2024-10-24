from PIL import Image
import os

image_x = 550
image_y = 225

folder_path = "./output/"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpeg"):
        img_path = folder_path + filename
        image = Image.open(img_path)
        new_image = image.resize((image_x, image_y))
        new_image.save(img_path)
