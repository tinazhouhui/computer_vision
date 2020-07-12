"""
excercise to work with bitwise operations.
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html
"""

import cv2

def bitwise():
    penguins = cv2.imread('input_image/penguins.jpg')
    logo = cv2.imread('input_image/codeac.png', 1)

    rows, cols, channels = logo.shape

    roi = penguins[0:rows, 0:cols]

    logo2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(logo2gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    penguins_bg = cv2.bitwise_and(roi, roi, mask = mask)

    logo_fg = cv2.bitwise_and(logo, logo, mask = mask_inv)

    output = cv2.add(penguins_bg, logo_fg)
    penguins[0:rows, 0:cols] = output

    # cv2.imwrite('output_image/logo_gray.jpg', mask)
    # cv2.imwrite('output_image/penguins_bg.jpg', penguins_bg)
    # cv2.imwrite('output_image/logo_fg.jpg', logo_fg)
    cv2.imwrite('output_image/penguins_logo.jpg', penguins)




