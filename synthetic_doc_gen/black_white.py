from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt


# #Load image and convert to greyscale
img = Image.open("./images/checks/0aa7480f-8476-4196-80e1-45101fd787db.jpeg")
img = img.convert("L")
bw = img.point(lambda x: 0 if x < 128 else 255, "1")




plt.imshow(bw)
plt.show()