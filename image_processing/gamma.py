"""
implementation of linear stretching and gamma
http://spatial-analyst.net/ILWIS/htm/ilwisapp/stretch_algorithm.htm
"""

import cv2
import numpy as np

def gamma_correction():
    moon = cv2.imread('input_image/moon.jpg', 0)
    max_value = np.max(moon)
    min_value = np.min(moon)

    for y in range(len(moon)):
        for x in range(len(moon[y])):
            moon[y][x] = (moon[y][x] - min_value) * ((255-0)/(max_value-min_value)) + 0

    cv2.imwrite('output_image/moon_gamma.jpg', moon)