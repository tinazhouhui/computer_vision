import numpy as np
import cv2

penguins = cv2.imread('penguins.jpg', 0)

image = np.zeros((512, 512, 3), np.uint8) # each zero has specific length, uint8 max 255
# 3 cause RGB depth

length_of_square = 100
start_x = 10
start_y = 10

for y in range(length_of_square):
    for i in range(length_of_square):
        image[start_x][start_y] = [255, 255, 255]
        start_x += 1
    start_x = start_x - length_of_square
    start_y += 1

square = image[0:120, 0:120]
image[120:240, 120:240] = square


head = penguins[110:310, 750:970]
head = np.flip(head, 1)
penguins[0:200, 0:220] = head

cv2.imwrite("image.jpg", image)
cv2.imwrite("penguins_bnw.jpg", penguins)

