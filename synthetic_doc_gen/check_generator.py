import cv2
import json
import uuid
import text_generator
import add_text

# Create truth table dictionary
truth_table = {}

# Opening configuration file
f = open('configuration.json')
config = json.load(f)

doc_types = ["check", "check2", "check3"]


# Set account number
account_number = text_generator.accountNumber()

for doc_type in doc_types:
    # set range for number of documents to generate
    for j in range(20):
        if doc_type == "check":
            image = cv2.imread("images/check_blank.jpeg")
        elif doc_type == "check2":
            image = cv2.imread("images/check2_blank.jpeg")
        else :
            image = cv2.imread("images/check3_blank.jpeg")

        
        payor = text_generator.fullName()
        address = text_generator.address()
        citystate = text_generator.cityStateZip()
        numeric_amount = text_generator.dollarAmount()
        word_amount = text_generator.writtenAmount(numeric_amount)
        signature = payor
        payee = text_generator.fullName()
        check_date = text_generator.createDate()
        memo = text_generator.shortSentence()
        check_number = text_generator.checkNumber()

        docId = str(uuid.uuid4())
        doc = config[doc_type]

        # measured with online tool https://pixspy.com/
        citystate_position = (doc["cityStateZip"]["x"],doc["cityStateZip"]["y"])
        address_position = (doc["address"]["x"],doc["address"]["y"])
        payor_position = (doc["payor"]["x"],doc["payor"]["y"])
        payee_position = (doc["payee"]["x"],doc["payee"]["y"])
        check_date_position = (doc["date"]["x"],doc["date"]["y"])
        numeric_amount_position = (doc["amount"]["x"],doc["amount"]["y"])
        word_amount_position = (doc["writtenAmount"]["x"],doc["writtenAmount"]["y"])
        memo_position = (doc["memo"]["x"],doc["memo"]["y"])
        signature_position = (doc["signature"]["x"],doc["signature"]["y"])
        check_number_position = (doc["checknumber"]["x"], doc["checknumber"]["y"])
        account_number_position = (doc["accountnumber"]["x"], doc["accountnumber"]["y"])

        # Add text to the image
        # font_size=doc["cityStateZip"]["fontSize"], thickness=doc["cityStateZip"]["fontThickness"], font=doc["cityStateZip"]["fontType"]
        modified_image = add_text.add_text_to_image(image, citystate, citystate_position, doc["cityStateZip"]["fontSize"],doc["cityStateZip"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, address, address_position, doc["address"]["fontSize"],doc["address"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, payor, payor_position, doc["payor"]["fontSize"],doc["payor"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, payee, payee_position, doc["payee"]["fontSize"],doc["payee"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, check_date, check_date_position, doc["date"]["fontSize"],doc["date"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, numeric_amount, numeric_amount_position, doc["amount"]["fontSize"],doc["amount"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, word_amount, word_amount_position, doc["writtenAmount"]["fontSize"],doc["writtenAmount"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, memo, memo_position, doc["memo"]["fontSize"],doc["memo"]["fontThickness"], cv2.FONT_HERSHEY_COMPLEX)
        modified_image = add_text.add_text_to_image(image, signature, signature_position, doc["signature"]["fontSize"],doc["signature"]["fontThickness"], cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)
        modified_image = add_text.add_text_to_image(image, check_number, check_number_position, doc["checknumber"]["fontSize"],doc["checknumber"]["fontThickness"], cv2.FONT_HERSHEY_SIMPLEX)
        modified_image = add_text.add_text_to_image(image, account_number, account_number_position, doc["accountnumber"]["fontSize"],doc["accountnumber"]["fontThickness"], cv2.FONT_HERSHEY_SIMPLEX)


        # Creates truth table entry
        # To Do -> add (x,y) position
        doc_dict = {
        "Payor": payor,
        "Amount": numeric_amount,
        "AmountWords": word_amount,
        "Address": address,
        "CityState": citystate,
        "Date": check_date,
        "Memo": memo,
        "Payee": payee,
        "Signature": signature,
        "CheckNumber": check_number,
        "AccountNumber": account_number,
        }

        truth_table[docId] = doc_dict


        # Save the modified image
        output_path = f"output/{docId}.jpeg"
        cv2.imwrite(output_path, modified_image)

# Converts truth table to JSON and saves
json_output_path = "output/truth_table.json"
with open(json_output_path, "w") as json_file:
    json.dump(truth_table, json_file, indent=2)

# Closing file
f.close()