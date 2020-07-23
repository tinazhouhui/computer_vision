"""
implementation of linear stretching and gamma
http://spatial-analyst.net/ILWIS/htm/ilwisapp/stretch_algorithm.htm
"""

import cv2
import numpy as np


def linear_stretching(input, lower_stretch_from, upper_stretch_from):
    """
    Linear stretching of input pixels
    :param input: integer, the input value of pixel that needs to be stretched
    :param lower_stretch_from: lower value of stretch from range - input
    :param upper_stretch_from: upper value of stretch from range - input
    :return: integer, integer, the final stretched value
    """

    lower_stretch_to = 0  # lower value of the range to stretch to - output
    upper_stretch_to = 255  # upper value of the range to stretch to - output

    output = (input - lower_stretch_from) * ((upper_stretch_to - lower_stretch_to) / (upper_stretch_from - lower_stretch_from)) + lower_stretch_to

    return output


def gamma_correction():
    """
    Restore the contrast in the faded image using linear stretching.
    """
    # imports the image of the moon
    moon = cv2.imread('input_image/moon.jpg', 0)

    # assign variable to max and min value of image pixels
    max_value = np.max(moon)
    min_value = np.min(moon)

    # cycle to apply linear stretching formula on each pixel
    for y in range(len(moon)):
        for x in range(len(moon[y])):
            moon[y][x] = linear_stretching(moon[y][x], min_value, max_value)

    # writes out the resulting restored picture
    cv2.imwrite('output_image/moon_gamma_restored.jpg', moon)