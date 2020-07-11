"""
Convolution
learning about the Kernel image processing and convolution matrices
https://en.wikipedia.org/wiki/Kernel_(image_processing)#:~:text=In%20image%20processing%2C%20a%20kernel,a%20kernel%20and%20an%20image.
"""

import math

import cv2
import numpy as np

KERNELS = {
        'edge-detection': {
            'constant': 1,
            'matrix': [
                [-1, -1, -1, ],
                [-1, 8, -1, ],
                [-1, -1, -1, ],
            ]
        },
        'gaussian-blur': {
            'constant': 1 / 256,
            'matrix': [
                [1, 4, 6, 4, 1, ],
                [4, 16, 24, 16, 4, ],
                [6, 24, 36, 24, 6, ],
                [4, 16, 24, 16, 4, ],
                [1, 4, 6, 4, 1, ],
            ]
        },
        'sharpen': {
            'constant': 1,
            'matrix': [
                [0, -1, 0, ],
                [-1, 5, -1, ],
                [0, -1, 0, ],
            ]
        },
        'low-pass': {
            'constant': 1/9,
            'matrix':  [
                [1, 1, 1, ],
                [1, 1, 1, ],
                [1, 1, 1, ],
            ]
        },
        'high-pass': {
            'constant': 1/2,
            'matrix':  [
                [1, 0, 1, ],
                [1, 0, 1, ],
                [1, 0, 1, ],
            ]
        },
    }

def select_kernel(transformation):
    """
    Takes the transformation desired and selects the correct constant and matrix to return the
    correct kernel.
    """
    global KERNELS

    if transformation not in KERNELS:
        print('argument does not exist')

    constant = KERNELS[transformation]['constant']
    matrix = KERNELS[transformation]['matrix']

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = constant * matrix[i][j]

    return matrix


def image_convolution(original_image, transformation):
    """
    Takes the image and the desired matrix and the desired transformation.
    """
    matrix = select_kernel(transformation)

    width = int(original_image.shape[1])
    height = int(original_image.shape[0])
    matrix_halfsize = math.floor(len(matrix) / 2)

    transformed_image = np.zeros((height, width))

    for y in range(matrix_halfsize, len(original_image) - matrix_halfsize):
        for x in range(matrix_halfsize, len(original_image[y]) - matrix_halfsize):

            transformed_pixel = 0

            for i in range(-matrix_halfsize, matrix_halfsize + 1):
                for j in range(-matrix_halfsize, matrix_halfsize + 1):
                    transformed_pixel += original_image[y + i][x + j] * matrix[i + 1][j + 1]
            transformed_image[y][x] = transformed_pixel

    return transformed_image

def create_transformed_outputs():
    """
    Creates all available transformations of original image
    """

    # path to image that you want to transform
    original_image_blur = cv2.imread('input_image/hairy-dog.jpg', 0)
    original_image_sharpen = cv2.imread('input_image/penguins.jpg', 0)
    original_image_pass = cv2.imread('input_image/puppy.jpg', 0)

    # transformation
    blurred = image_convolution(original_image_blur, 'gaussian-blur')
    sharpen = image_convolution(original_image_sharpen, 'sharpen')
    high_pass = image_convolution(original_image_pass, 'high-pass')
    low_pass = image_convolution(original_image_blur, 'low-pass')

    # transformed image and where to save it
    cv2.imwrite('output_image/convolution_transformed/blurred.jpg', blurred)
    cv2.imwrite('output_image/convolution_transformed/sharpen.jpg', sharpen)
    cv2.imwrite('output_image/convolution_transformed/high_pass.jpg', high_pass)
    cv2.imwrite('output_image/convolution_transformed/low_pass.jpg', low_pass)

def edge_detection():
    """
    Uses same principles of convolution but just edge detection
    """
    original_image_edge = cv2.imread('input_image/wheels.jpg', 0)
    edge = image_convolution(original_image_edge, 'edge-detection')
    cv2.imwrite('output_image/convolution_transformed/edge.jpg', edge)