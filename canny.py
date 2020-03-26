import cv2

image = cv2.imread(r"C:\Users\Admin\Desktop\demo.jpg")

# 100 is lower threshold for removing pixel, 200 is higher threshold
edges = cv2.Canny(image, 100, 200)

cv2.imshow("image", edges)
cv2.waitKey(0)