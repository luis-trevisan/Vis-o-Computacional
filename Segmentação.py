#SEGMENTAÇÃO
import cv2
import numpy as np

image = cv2.imread('Fig0630(01)(strawberries_fullcolor).tif')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blur = cv2.medianBlur(hsv ,11)

lower = np.array([0,87,83])
upper = np.array([179,255,247])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(image,image, mask= mask)

cv2.imwrite('resultado.jpg', res)
