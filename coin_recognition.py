"""
coin recognition
task: draw a circle around each coin
method: redrawing a circle by increasing its diameter by 1 px and then see if the edge matches
the circle at least by some threshold. if yes, change color.

edge detection using Canny
20 px < r < 100 px
"""

import cv2
import numpy as np

# defining minimal and maximal radius
min_r = 20
max_r = 100

coins = cv2.imread('input/coins.jpg', 0)
coins_edge = cv2.Canny(coins, 127, 255)


cv2.imwrite("output/coins_circled.jpg", coins_edge)