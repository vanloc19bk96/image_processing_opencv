import cv2
import numpy as np


image = cv2.imread(r"C:\Users\LocTV7\Desktop\demo.jpg")
h, w = image.shape[:2]
tx, ty = (200, 200)

# move to bottom right
M1 = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
bottom_right = cv2.warpAffine(image, M1, (w, h))

# move to bottom left
M2 = np.array([[1, 0, -tx], [0, 1, ty]], dtype=np.float32)
bottom_left = cv2.warpAffine(image, M2, (w, h))

# move to top right
M3 = np.array([[1, 0, tx], [0, 1, -ty]], dtype=np.float32)
top_right = cv2.warpAffine(image, M3, (w, h))

# move to top left
M4 = np.array([[1, 0, -tx], [0, 1, -ty]], dtype=np.float32)
top_left = cv2.warpAffine(image, M4, (w, h))


cv2.imshow("image", top_left)
cv2.waitKey(0)