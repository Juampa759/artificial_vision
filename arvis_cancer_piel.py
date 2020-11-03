import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('img/A.jpg')
img2 = cv2.imread('img/B.jpg')

I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
mascara = np.uint8((I<umbral)+255) #Binary image

E = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
umbral2,_ = cv2.threshold(E,0,255,cv2.THRESH_OTSU)
mascara2 = np.uint8((E<umbral2)+255) #Binary image

cv2.imshow("Img1-GRAY",I)
cv2.imshow("Img1-BINARY",mascara)


cv2.imshow("Img2-GRAY",E)
cv2.imshow("Img2-BINARY",mascara2)

suma1 = np.sum(img1)
minimo1 = np.min(img1)
maximo1 = np.max(img1)
prom1 = np.mean(img1)
var1 = np.var(img1)
de1 = np.sqrt(var1)

suma2 = np.sum(img2)
minimo2 = np.min(img2)
maximo2 = np.max(img2)
prom2 = np.mean(img2)
var2 = np.var(img2)
de2 = np.sqrt(var2)


pxX = np.size(img1, axis=0)
pxY = np.size(img1, axis=1)
pxXY = np.size(img1, axis=None)

pxX2 = np.size(img2, axis=0)
pxY2 = np.size(img2, axis=1)
pxXY2 = np.size(img2, axis=None)

#histograma 1 
data = I.flatten()
plt.hist(data, bins=100)
red = img1[:,:,0].flatten()
green = img1[:,:,1].flatten()
blue =  img1[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")

#histograma 2
data = E.flatten()
plt.hist(data, bins=100)
red = img2[:,:,0].flatten()
green = img2[:,:,1].flatten()
blue =  img2[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")


cv2.waitKey(0)
cv2.destroyAllWindows()