import cv2

image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")
h, w = image.shape[:2]

# rotate 45 degree at center of image, scaled rotation unchange
M1 = cv2.getRotationMatrix2D(center=(h/2, w/2), angle=-45, scale=1)
trans1 = cv2.warpAffine(image, M1, (h, w))

# rotate -45 degree at center of image, scaled rotation is 0.5
M2 = cv2.getRotationMatrix2D(center=(h/2, w/2), angle=45, scale=0.5)
trans2 = cv2.warpAffine(image, M2, (h, w))

# rotate 20 degree at the top left of image, scaled rotation is 0.5
M3 = cv2.getRotationMatrix2D(center=(0, 0), angle=20, scale=1)
trans3 = cv2.warpAffine(image, M3, (h, w))

cv2.imshow("bottom_right", trans3)
cv2.waitKey(0)