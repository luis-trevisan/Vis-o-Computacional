#RESTAURAÇÃO DE IMAGEM - NUMPY.FFT
from numpy import fft
import matplotlib.pyplot as plt
import cv2

im = plt.imread('Fig0516(a)(applo17_boulder_noisy).tif')

im_fft = fft.fft2(im)

keep_fraction = 0.1

r, c = im_fft.shape

im_fft[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
im_fft[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0

im_new = fft.ifft2(im_fft).real

cv2.imwrite("resultado.jpg", im_new)
