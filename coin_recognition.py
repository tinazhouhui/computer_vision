"""
coin recognition
task: draw a circle around each coin
method: redrawing a circle by increasing its diameter by 1 px and then see if the edge matches
the circle at least by some threshold. if yes, change color.

edge detection using Canny
"""

import cv2
import numpy as np
import math

# defining minimal and maximal radius
min_r = 22
max_r = 38

coins = cv2.imread('input_image/coins.jpg', 1)
coins_height, coins_width, coins_channel = coins.shape
coins_resized = cv2.resize(coins, (int(coins_width/2), int(coins_height/2)))
coins_blurred = cv2.GaussianBlur(coins_resized, (5, 5), cv2.BORDER_DEFAULT)
coins_edge = cv2.Canny(coins_blurred, 127, 255)
# obtain the image size
max_height, max_width, channel = coins_resized.shape

start_x = 0
start_y = 0

threshold = 0.35
pixel_threshold = 255 * 0.123
picture_step = 1
coin_detection = []


def coin_center_detect():
    # draw circles
    for radius in range(min_r, max_r):
        img_circle = np.zeros((radius * 2, radius * 2, 1), np.uint8)
        circle = cv2.circle(img_circle, (radius, radius), radius, 255)

        circumference = 2 * math.pi * radius

        circle_pixels = []

        for y in range(len(circle)):
            for x in range(len(circle[y])):
                if circle[x][y] == 255:
                    circle_pixels.append((x, y))

        print(('radius', radius))

        # move circle through image
        for start_y in range(0, max_height - 2 * radius, picture_step):
            for start_x in range(0, max_width - 2 * radius, picture_step):
                count = 0

                # cycle through the image of circle
                for (x, y) in circle_pixels:
                    image_y = start_y + y
                    image_x = start_x + x

                    if coins_edge[image_y][image_x] >= pixel_threshold:
                        count += 1

                if count > 50:
                    percentage = round(count / circumference * 100, 2)
                    print(('candidate', start_x + radius, start_y + radius, radius, percentage))

                if (count / circumference) > threshold:
                    coin_detection.append((start_x + radius, start_y + radius, radius)) # center
                    print(('-----------------', start_x + radius, start_y + radius, radius))

    return coin_detection

def Hough_circle_detection():
    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 40, param1=50, param2=30, minRadius=min_r*2, maxRadius=max_r*2)
    return circles

coins_circled = Hough_circle_detection()

for detected_circle in coins_circled[0]:
    print(detected_circle)
    x_coor, y_coor, detected_radius = detected_circle
    coins_detected = cv2.circle(coins, (x_coor, y_coor), detected_radius, (0, 0, 255), 1)

cv2.imwrite("output_image/coins_detected.jpg", coins_detected)
# cv2.imwrite("output_image/circles/circle{}.jpg".format(radius), circle)
# cv2.imwrite("output_image/coins_blurred.jpg", coins_blurred)
# cv2.imwrite("output_image/coins_edge.jpg", coins_edge)
# cv2.imwrite("output_image/coins_resized.jpg", coins_resized)
