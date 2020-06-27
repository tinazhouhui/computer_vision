import cv2

sky = cv2.imread('sky.jpg', 1)
penguins = cv2.imread('penguins.jpg', 1)

width = int(penguins.shape[1])
height = int(penguins.shape[0])

dsize = (width, height)

sky_resized = cv2.resize(sky, dsize)

blended = cv2.addWeighted(penguins, 0.5, sky_resized, 0.5, 10)



cv2.imwrite("sky_modified.jpg", sky_resized)
cv2.imwrite("blended.jpg", blended)