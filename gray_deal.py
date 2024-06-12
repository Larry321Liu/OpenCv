"""
cv2.imshow()和plt.imshow()的区别
什么时候使用plt.show()，什么时候用cv2.imshow()?
如果需要展示读入的图像，或者展示对读入图像进行一系列操作后的图像时，使用cv2.imshow()
如果不需要展示原始图像，而是绘制一张新的图像，使用plt.imshow()
其实两者都可以，但要注意的是opencv是BGR通道，plt默认RGB通道，
若使用cv2.imread()读入图像，用plt.imshow()展示原始图像或者展示对读入图像进行一系列操作后的图像时，需要进行通道转换。
在展示灰度图像时，cv2.imshow(‘gray’, gray)
plt.imshow(gray,cmap=‘gray’), plt.title(‘gray’)

"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('lenna.png')
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB) # BGR转化为RGB格式
plt.subplot(121)
plt.imshow(img1)
plt.title('Src_img')

# 灰度转换
image2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.subplot(122)
plt.imshow(image2, plt.cm.gray)
plt.title('Gray_img')
plt.show()