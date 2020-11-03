# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:20:36 2020

@author: Usuario
"""

import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/bananas.jpg')

pxX = np.size(img, axis=0)
pxY = np.size(img, axis=1)
pxXY = np.size(img, axis=None)

promManual = np.sum(img)/(pxX * pxY * 3)

suma = np.sum(img)
minimo = np.min(img)
maximo = np.max(img)
prom = np.mean(img)
var = np.var(img)
de = np.sqrt(var)

#cv2.imshow('img_Original', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('img-HSV', hsv)

I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img_GRAY', I)

#umbral,_ = cv2.threshold(I,0,255, cv2.THRESH_OTSU)
#binaria = np.uint8((I<umbral)+255)
#cv2.imshow('img_Binary', binaria)

#histograma
data = I.flatten()
plt.hist(data, bins=100)
red = img[:,:,0].flatten()
green = img[:,:,1].flatten()
blue =  img[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")


cv2.waitKey(0)
cv2.destroyAllWindows()