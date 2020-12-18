# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:30:55 2020

@author: Usuario
"""
import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img1 = cv2.imread('img/bananas.jpg')
I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
mascara = np.uint8((I<umbral)*255) #Binary image

#cv2.imshow("Img-COLOR",img1)
#cv2.imshow("Img-GRAY",I)
cv2.imshow("Img-BINARY",mascara)

#Get labels 
output = cv2.connectedComponentsWithStats(mascara,4,cv2.CV_32F)
cantObj = output[0]#objects quantify
labels = output[1]#labels
stats = output[2]

#Get ArgMax
mascara = (np.argmax(stats[:,4][1:])+1==labels)
mascara = ndimage.binary_fill_holes(mascara).astype(int)


cv2.waitKey(0)
cv2.destroyAllWindows()