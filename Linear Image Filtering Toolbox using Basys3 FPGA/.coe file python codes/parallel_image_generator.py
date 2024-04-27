# -*- coding: utf-8 -*-
import numpy as np
import cv2
img = cv2.imread("flower.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("Intermediate_Images/gray.bmp", gray_img)

#shift 1 bit down
a = np.zeros(img.shape)
for i in range(1, len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i-1][j][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/down.bmp', a)

#shift 1 bit up
a = np.zeros(img.shape)
for i in range(len(img)-1):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i+1][j][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/up.bmp', a)

#shift 1 bit left
a = np.zeros(img.shape)
for i in range(len(img)):
    for j in range(1, len(img[i])):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i][j-1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/left.bmp', a)

#shift 1 bit right
a = np.zeros(img.shape)
for i in range(len(img)):
    for j in range(len(img[i])-1):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i][j+1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/right.bmp', a)

#shift 1 bit down 1 bit left
a = np.zeros(img.shape)
for i in range(1, len(img)):
    for j in range(1, len(img[i])):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i-1][j-1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/leftdown.bmp', a)

#shift 1 bit up
a = np.zeros(img.shape)
for i in range(len(img)-1):
    for j in range(len(img[i])-1):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i+1][j+1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/rightup.bmp', a)

#shift 1 bit left
a = np.zeros(img.shape)
for i in range(len(img)-1):
    for j in range(1, len(img[i])):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i+1][j-1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/leftup.bmp', a)

#shift 1 bit right
a = np.zeros(img.shape)
for i in range(1, len(img)):
    for j in range(len(img[i])-1):
        for k in range(len(img[i][j])):
            #print(img[i][j][k])
            a[i-1][j+1][k] = img[i][j][k]

cv2.imwrite('Intermediate_Images/rightdown.bmp', a)


