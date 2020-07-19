import cv2
from image_processing.convo import image_convolution


def edge_detection():
    """
    Uses same principles of convolution but for edge detection
    """

    original_image_edge = cv2.imread('input_image/wheels.jpg', 0)

    #Sobel edge detection
    edge_sobel_x = cv2.Sobel(original_image_edge, -1, 1, 0, ksize=3)
    edge_sobel_y = cv2.Sobel(original_image_edge, -1, 0, 1, ksize=3)

    edge_sobel_combined = cv2.addWeighted(edge_sobel_x, 0.5, edge_sobel_y, 0.5, 0)

    cv2.imwrite('output_image/convolution_edge/edge_sobel_x.jpg', edge_sobel_x)
    cv2.imwrite('output_image/convolution_edge/edge_sobel_y.jpg', edge_sobel_y)
    cv2.imwrite('output_image/convolution_edge/edge_sobel_combined.jpg', edge_sobel_combined)

    #Laplacian operator without Gaussian
    edge_laplacian = image_convolution(original_image_edge, 'edge-detection')

    cv2.imwrite('output_image/convolution_edge/edge_laplacian.jpg', edge_laplacian)

    #Laplacian of Gaussian edge detection
    blur = cv2.GaussianBlur(original_image_edge, (5,5), 0, 0)
    edge_LoG = cv2.Laplacian(blur, cv2.CV_8U, 3, scale=10) #scale increases the contrast

    cv2.imwrite('output_image/convolution_edge/edge_LoG.jpg', edge_LoG)

    #Canny edge detection
    edge_canny = cv2.Canny(original_image_edge, 100, 200)

    cv2.imwrite('output_image/convolution_edge/edge_canny.jpg', edge_canny)