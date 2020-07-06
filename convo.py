"""
Convolution
learning about the Kernel image processing and convolution matrices
https://en.wikipedia.org/wiki/Kernel_(image_processing)#:~:text=In%20image%20processing%2C%20a%20kernel,a%20kernel%20and%20an%20image.
"""

import cv2
import numpy as np

default = [
    [10, 12, 14, 16, 18, 20, 22, 24, ],
    [20, 22, 24, 26, 28, 30, 32, 34, ],
    [30, 32, 34, 36, 38, 40, 42, 44, ],
    [40, 42, 44, 46, 48, 50, 52, 54, ],
    [50, 52, 54, 56, 58, 60, 62, 64, ],
    [60, 62, 64, 66, 68, 70, 72, 74, ],
]

default = cv2.imread('input/shaft.png', 0)

constant = 1
matrix = [
    [-1, -1, -1, ],
    [-1, 8, -1, ],
    [-1, -1, -1, ],
]



for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = constant * matrix[i][j]

width = int(default.shape[1])
height = int(default.shape[0])

transformed = np.zeros((height, width))


for y in range(1, len(default)-1):
    for x in range(1, len(default[y])-1):

        output_pixel = 0

        for i in range(-1, len(matrix)-1):
            for j in range(-1, len(matrix[i])-1):
                output_pixel += default[y+j][x+i] * matrix[i+1][j+1]
        transformed[y][x] = output_pixel

cv2.imwrite('output/transformed.jpg', transformed)




