"""
Coin recognition, real life application
task: calculate the value of coins on picture
"""

import cv2
import numpy as np

def detect_coins():
    coins = cv2.imread('../input_image/koruny.jpg', 1)

    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 7)
    circles = cv2.HoughCircles(
        img,  # source image
        cv2.HOUGH_GRADIENT,  # type of detection
        1,
        50,
        param1=100,
        param2=50,
        minRadius=10,  # minimal radius
        maxRadius=380,  # max radius
    )

    coins_copy = coins.copy()


    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        coins_detected = cv2.circle(
            coins_copy,
            (int(x_coor), int(y_coor)),
            int(detected_radius),
            (0, 255, 0),
            4,
        )

    cv2.imwrite("../output_image/coin_amount/koruny_test_Hough.jpg", coins_detected)

    return circles

def calculate_amount():
    koruny = {
        "1 CZK": {
            "value": 1,
            "radius": 20,
            "ratio": 1,
            "count": 0,
        },
        "2 CZK": {
            "value": 2,
            "radius": 21.5,
            "ratio": 1.075,
            "count": 0,
        },
        "5 CZK": {
            "value": 5,
            "radius": 23,
            "ratio": 1.15,
            "count": 0,
        },
        "10 CZK": {
            "value": 10,
            "radius": 24.5,
            "ratio": 1.225,
            "count": 0,
        },
        "20 CZK": {
            "value": 20,
            "radius": 26,
            "ratio": 1.3,
            "count": 0,
        },
        "50 CZK": {
            "value": 50,
            "radius": 27.5,
            "ratio": 1.375,
            "count": 0,
        },
    }

    circles = detect_coins()
    radius = []
    coordinates = []

    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        radius.append(detected_radius)
        coordinates.append([x_coor, y_coor])

    smallest = min(radius)
    tolerance = 0.0375
    total_amount = 0

    coins_circled = cv2.imread('../output_image/coin_amount/koruny_test_Hough.jpg', 1)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for coin in circles[0]:
        ratio_to_check = coin[2] / smallest
        coor_x = coin[0]
        coor_y = coin[1]
        for koruna in koruny:
            value = koruny[koruna]['value']
            if abs(ratio_to_check - koruny[koruna]['ratio']) <= tolerance:
                koruny[koruna]['count'] += 1
                total_amount += koruny[koruna]['value']
                cv2.putText(coins_circled, str(value), (int(coor_x), int(coor_y)), font, 1,
                            (0, 0, 0), 4)

    print(f"The total amount is {total_amount} CZK")
    for koruna in koruny:
        pieces = koruny[koruna]['count']
        print(f"{koruna} = {pieces}x")


    cv2.imwrite("../output_image/coin_amount/koruny_hodnota.jpg", coins_circled)



if __name__ == "__main__":
    calculate_amount()
