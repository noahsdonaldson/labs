import matplotlib.pyplot as plt
import cv2


def test_layout(image):

    
    
    # Convert BGR image to RGB (for displaying with Matplotlib)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Plot the modified image
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()