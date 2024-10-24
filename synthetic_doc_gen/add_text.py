# https://python.plainenglish.io/how-to-create-synthetic-datasets-of-document-images-5f140dee5e40

import cv2

def add_text_to_image(image, text, position, font_size, thickness, font):
    
    # Choose a font and font scale
    font = font

    # Set font color as black
    font_color = (0,0,0)
    
    # Set position
    x, y = position
    
    # Set default font size and thickness
    font_size = font_size
    thickness = thickness

    # Add the text to the image
    cv2.putText(image, text, (x, y), font, font_size, font_color, thickness, cv2.LINE_AA)

    # Return the modified image
    return image

