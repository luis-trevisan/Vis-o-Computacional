#EQUALIZAÇÃO DE HISTOGRAMA
import cv2a

img = cv2.imread('Luis Paulo Silva Trevisan - Fig0309(a)(washed_out_aerial_image).tif')
img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('result.jpg', hist_equalization_result)
