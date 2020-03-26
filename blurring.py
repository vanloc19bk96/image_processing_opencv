import cv2
import numpy as np

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo2.jpg")

# average filter
average = cv2.blur(image, (5, 5))

# gaussian filter
gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# median filter
median = cv2.medianBlur(image, 5, 0)

# bilateral
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow("original", image)
cv2.imshow("median", bilateral)
cv2.waitKey(0)
