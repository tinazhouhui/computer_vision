"""
exercise to try out blending two images together.
"""

import cv2

def blend():
    img_1 = cv2.imread('input_image/sky.jpg', 1)
    img_2 = cv2.imread('input_image/penguins.jpg', 1)

    width = int(img_2.shape[1])
    height = int(img_2.shape[0])

    dsize = (width, height)

    sky_resized = cv2.resize(img_1, dsize)

    blended = cv2.addWeighted(img_2, 0.5, sky_resized, 0.5, 10)

    # cv2.imwrite("output_image/sky_modified.jpg", sky_resized)
    cv2.imwrite("output_image/blended.jpg", blended)
