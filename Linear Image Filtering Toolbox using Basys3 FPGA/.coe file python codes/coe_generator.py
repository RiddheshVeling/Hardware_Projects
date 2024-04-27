# -*- coding: utf-8 -*-
import cv2
gray = cv2.imread("Intermediate_Images/gray.bmp")
left = cv2.imread("Intermediate_Images/left.bmp")
right = cv2.imread("Intermediate_Images/right.bmp")
up = cv2.imread("Intermediate_Images/up.bmp")
down = cv2.imread("Intermediate_Images/down.bmp")
leftup = cv2.imread("Intermediate_Images/leftup.bmp")
leftdown = cv2.imread("Intermediate_Images/leftdown.bmp")
rightup = cv2.imread("Intermediate_Images/rightup.bmp")
rightdown = cv2.imread("Intermediate_Images/rightdown.bmp")
img = cv2.imread("laptop.jpg")

coe = open("flower_1.coe", "w")

coe.write("memory_initialization_radix=2;\nmemory_initialization_vector=\n")

lst = ["gray", "left", "right", "up", "down", "leftup", "leftdown", "rightup", "rightdown"]
st = ""

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        for k in lst:
            bi = ""
            string = "bi = bin(" + k + "[i][j][0])[2:]"
            exec(string)
            for l in range(8-len(bi)):
                bi = '0' + bi
            st = st + bi
        coe.write(st)
        x = ""
        for l in img[i][j]:
            bil = bin(l)[2:]
            for m in range(8-len(bil)):
                bil = '0' + bil
            x = x + bil
        coe.write(x + ',\n')
        st = ""
coe.close()