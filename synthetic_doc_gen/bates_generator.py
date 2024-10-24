import cv2
import json
import uuid
import text_generator
import add_text


bates_position = (190,85)
for i in range(70):
    image = cv2.imread("images/bates_blank.jpeg")
    bates_number = text_generator.batesNumber()
    modified_image = add_text.add_text_to_image(image, bates_number, bates_position, 1, 2, cv2.FONT_HERSHEY_SIMPLEX)
    docId = str(uuid.uuid4())
    output_path = f"output/bates_" + str(docId) + ".jpeg"
    cv2.imwrite(output_path, modified_image)
