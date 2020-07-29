"""
coin recognition
task: draw a circle around each coin
method: comparing a circle by increasing its diameter by 1 px and then see if the edge matches
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

# optimisation by decreasing the size of image, resulting in 4x faster run time
coins_resized = cv2.resize(coins, (int(coins_width/2), int(coins_height/2)))

# blur to optimise edge finding
coins_blurred = cv2.GaussianBlur(coins_resized, (5, 5), cv2.BORDER_DEFAULT)

# used Canny to find the edge
coins_edge = cv2.Canny(coins_blurred, 127, 255)

# obtain the image size
max_height, max_width, channel = coins_resized.shape

start_x = 0
start_y = 0

edge_threshold = 0.35  # how many pixels need to pass to be considered a coin edge
pixel_threshold = 255 * 0.123  # the min value of pixel to be considered edge
next_circle_step = 1  # the amount of pixels to move to start comparing again
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
        for start_y in range(0, max_height - 2 * radius, next_circle_step):
            for start_x in range(0, max_width - 2 * radius, next_circle_step):
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

                if (count / circumference) > edge_threshold:
                    coin_detection.append((start_x + radius, start_y + radius, radius)) # center
                    print(('-----------------', start_x + radius, start_y + radius, radius))

    return coin_detection


def circle_coins():

    coins_circled = coin_center_detect()
    coins_copy = coins.copy()
    for detected_circle in coins_circled:
        x_coor, y_coor, detected_radius = detected_circle
        coins_detected = cv2.circle(coins_copy, (x_coor * 2, y_coor * 2), detected_radius * 2, (0, 0, 255), 1)

    cv2.imwrite("output_image/coin_detection/coins_detected.jpg", coins_detected)
    cv2.imwrite("output_image/coins_blurred.jpg", coins_blurred)
    cv2.imwrite("output_image/coins_edge.jpg", coins_edge)
    # cv2.imwrite("output_image/coins_resized.jpg", coins_resized)


def Hough_circle_detection():
    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(
        img,  # source image
        cv2.HOUGH_GRADIENT,  # type of detection
        1,
        40,
        param1=50,
        param2=30,
        minRadius=min_r*2,  # minimal distance between two centers
        maxRadius=max_r*2,  # max distance between two centers
    )

    coins_copy = coins.copy()

    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        coins_detected = cv2.circle(coins_copy, (x_coor, y_coor), detected_radius, (0, 0, 255), 1)

    cv2.imwrite("output_image/coin_detection/coins_detected_Hough.jpg", coins_detected)


def compare_circle_detection():
    circle_coins()
    Hough_circle_detection()
