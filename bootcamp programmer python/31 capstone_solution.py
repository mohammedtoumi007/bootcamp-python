import numpy as np
import cv2



img = cv2.imread('capstone_coins.png',cv2.IMREAD_GRAYSCALE)
original_image = cv2.imread('capstone_coins.png',1)
img = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('Detected Coins',original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()