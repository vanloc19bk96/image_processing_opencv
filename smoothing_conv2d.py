import cv2
import numpy as np

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")

kernel = np.ones((5, 5), np.float32)/25
imgSmooth = cv2.filter2D(image, -1, kernel)
cv2.imshow("original", image)
cv2.imshow("smooth", imgSmooth)
cv2.waitKey(0)