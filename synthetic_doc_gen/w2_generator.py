import cv2
import json
import uuid
import text_generator
import add_text

# Create truth table dictionary
truth_table = {}


name_position = (90,176)
for i in range(50):
    image = cv2.imread("images/w2.jpeg")
    name = text_generator.fullName()
    modified_image = add_text.add_text_to_image(image, name, name_position, 1, 2, cv2.FONT_HERSHEY_SIMPLEX)
    docId = str(uuid.uuid4())
    output_path = f"output/" + str(docId) + ".jpeg"
    cv2.imwrite(output_path, modified_image)

 # Creates truth table entry
# To Do -> add (x,y) position
doc_dict = {
"Name": name,

}

truth_table[docId] = doc_dict


# Save the modified image
output_path = f"output/{docId}.jpeg"
cv2.imwrite(output_path, modified_image)

# Converts truth table to JSON and saves
json_output_path = "output/truth_table.json"
with open(json_output_path, "w") as json_file:
    json.dump(truth_table, json_file, indent=2)
