import cv2
import numpy as np

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")
h, w = image.shape[:2]

original_points = np.float32([[50, 50], [350, 50], [50, 350], [350, 350]])
output_points = np.float32([[0, 0], [200, 50], [50, 300], [300, 300]])

M = cv2.getPerspectiveTransform(original_points, output_points)
perspectiveImage = cv2.warpPerspective(image, M, (h, w))

cv2.imshow("image", perspectiveImage)
cv2.waitKey(0)