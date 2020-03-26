import cv2
import numpy as np

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")
h, w = image.shape[:2]

# choose 3 points at original image
original_points = np.float32([[50, 50], [200, 50], [50, 200]])

# choose 3 points as a output
output_points = np.float32([[50, 300], [200, 150], [150, 400]])

M = cv2.getAffineTransform(original_points, output_points)
imageAffine = cv2.warpAffine(image, M, (h, w))

cv2.imshow("image", imageAffine)
cv2.waitKey(0)