import cv2
import json
import uuid
import text_generator
import add_text
import numpy as np


account_number = text_generator.accountNumber()
image_x = 550
image_y = 225

b,g,r = 255,255,255

docnum = 0

for i in range(20):
    # Create new image with cv2
    image = np.zeros((image_y, image_x, 3), np.uint8)
    image[:,:,0] = b
    image[:,:,1] = g
    image[:,:,2] = r
    
    deposit_pos = (image_x - 540, image_y - 200)
    virdoc_pos = (image_x - 540, image_y - 185)
    account_pos1 = (image_x - 540, image_y - 170)
    description_pos = (image_x - 540, image_y - 155)
    deposit = add_text.add_text_to_image(image, "Deposit Ticket", deposit_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    virdoc = add_text.add_text_to_image(image, "Virtual Document", virdoc_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    account_num1 = add_text.add_text_to_image(image, f"Account: {account_number}", account_pos1, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    description = add_text.add_text_to_image(image, "Description: Checking Deposit", description_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)


    name_pos = (image_x - 540, image_y - 100)
    cashdrw_pos = (image_x - 540, image_y - 85)
    rdmnum_pos = (image_x - 540, image_y - 70)
    bottom_pos = (image_x - 540, image_y - 25)
    deposit_name = text_generator.deposit_name()
    name = add_text.add_text_to_image(image, f"Name: {deposit_name}", name_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    cash_drawer_txt = text_generator.cash_drawer()
    user_txt = text_generator.user()
    cash_drawer = add_text.add_text_to_image(image, f"Cash Drawer: {cash_drawer_txt}     User: {user_txt}", cashdrw_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    rdm_txt = text_generator.random_text()
    random_number = add_text.add_text_to_image(image, rdm_txt, rdmnum_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)
    bottom_txt = f"|: 222222222   |:   {account_number} ||*  "
    bottom = add_text.add_text_to_image(image, bottom_txt, bottom_pos, .3, 1, cv2.FONT_HERSHEY_SIMPLEX)


    amount_pos = ((image_x // 3 * 2), (image_y // 2))
    amount_txt = text_generator.depositAmount()
    amount = add_text.add_text_to_image(image, f"$ {amount_txt}", amount_pos, .6, 1, cv2.FONT_HERSHEY_SIMPLEX)
    docnum = docnum + 1
    docId = f"deposit_{docnum}"
    output_path = f"output/{docId}.jpeg"
    cv2.imwrite(output_path, image)

    # cv2.imshow("image", image)
    # cv2.waitKey(0)
