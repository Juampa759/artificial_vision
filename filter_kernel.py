# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:42:47 2020

@author: Usuario
"""

import cv2
import numpy as np

img_ori = cv2.imread('img/banano.jpg')
cv2.imshow('Img-Ori', img_ori)

#Kernel's
kernel_3x3 = np.ones((3,3),np.float32)/(3*3)
output = cv2.filter2D(img_ori, -1,kernel_3x3)
cv2.imshow('3x3', output)

kernel_3x3 = np.ones((5,5),np.float32)/(5*5)
output = cv2.filter2D(img_ori, -1,kernel_3x3)
cv2.imshow(' 5x5', output)

kernel_3x3 = np.ones((31,31),np.float32)/(31*31)
output = cv2.filter2D(img_ori, -1,kernel_3x3)
cv2.imshow('31x31', output)

#Filtro Gaussiano
output = cv2.GaussianBlur(src, ksize, sigmaX)


cv2.waitKey(0)
cv2.destroyAllWindows()