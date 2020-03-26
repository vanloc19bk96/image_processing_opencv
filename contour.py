import cv2

image = cv2.imread(r"C:\Users\Admin\Desktop\demo2.jpg")
original_image = image.copy()

imgCanny = cv2.Canny(image, 100, 200)
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(original_image, contours, -1, (0, 255, 0), 3)
cv2.imshow("image", original_image)
cv2.waitKey(0)