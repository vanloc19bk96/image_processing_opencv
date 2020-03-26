import cv2

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")
print('Origin image shape: {}'.format(image.shape))

h, w = image.shape[:2]
imgScale = cv2.resize(image, (int(w*2), int(h*2)))
print('Scale image shape: {}'.format(imgScale.shape))

cv2.imshow("image", image)
cv2.imshow("scale", imgScale)
cv2.waitKey(0)