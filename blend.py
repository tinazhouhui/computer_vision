"""
exercise to try out blending two images together.
"""

import cv2

sky = cv2.imread('input/sky.jpg', 1)
penguins = cv2.imread('input/penguins.jpg', 1)

width = int(penguins.shape[1])
height = int(penguins.shape[0])

dsize = (width, height)

sky_resized = cv2.resize(sky, dsize)

blended = cv2.addWeighted(penguins, 0.5, sky_resized, 0.5, 10)

cv2.imwrite("output/sky_modified.jpg", sky_resized)
cv2.imwrite("output/blended.jpg", blended)