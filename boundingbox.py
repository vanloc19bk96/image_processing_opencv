import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Admin\Desktop\demo3.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# area of contours
area = [cv2.contourArea(contour) for contour in contours]
sorted_area = np.argsort(area)[::-1]
print(sorted_area[:5])

# draw bouding box for contour wich has the second largest area
contour = contours[sorted_area[1]]
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# draw bouding box with smallest area around contour
rect = cv2.minAreaRect(contour)
box = cv2.boxPoints(rect)
box = np.int0(box)
image = cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)