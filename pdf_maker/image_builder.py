from PIL import Image
import numpy as np
import uuid
import os
from PIL import ImageOps
import random
import string

# function to generate random numbers and letters
def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string_length
    return ''.join(random.choice(string.ascii_letters) for i in range(letters))


def image_builder(img_path,bates=False, multiCheck = False):

    img_path = img_path
    blank_image = "./images/blanks/blank.jpeg"
    img_header = "./images/blanks/header.jpeg"
    if multiCheck == True:
        num_its = int(len(img_path)/2)
        i0 = 0
        i1 = 1
        bi = 0
    else:
        num_its = int(len(img_path))
        i0 = 0
        bi=0
    

    for i in range(num_its):
        combined = []
        header = Image.open(img_header)
        header = header.resize((820, 150))
        combined.append(header)
        if multiCheck == True:
            list_imgs = [ "./images/to_convert/" + img_path[i0], "./images/to_convert/" + img_path[i1]]
        else:
            list_imgs = [ "./images/to_convert/" + img_path[i0], blank_image]
        for img in list_imgs:
            image = Image.open(img)
            # resize checks to fit on 8x10 page
            image = image.resize((800, 362))
            # add white boarder
            image = ImageOps.expand(image, border=10, fill='white')
            combined.append(image)
        if multiCheck == True:
           i0 = i1 + 1
           i1 = i1 + 2
        else:
            i0 = i0 + 1
        if bates == True:
            bates_path = (os.listdir("./images/bates"))
            bates_img = Image.open("./images/bates/" + bates_path[bi])
            bates_img = bates_img.resize((820, 90))
            combined.append(bates_img)
            bi = bi + 1
        else:
            blank_img = Image.open(blank_image)
            blank_img = blank_img.resize((820, 90))
            combined.append(blank_img)

        # combine and save
        combined = np.vstack(combined)
        combined = Image.fromarray( combined)
        combined.save( "./images/" + random_string() + ".jpeg" )

image_path = (os.listdir("./images/to_convert"))
image_builder(image_path, bates=True, multiCheck = True)

