#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

if __name__ == "__main__":
    img1 = mpimg.imread('d.jpg').copy()
    img2 = mpimg.imread('e.jpg').copy()
    img3 = img1.copy()
    # img1 = img1/255.0
    # img2 = img2/255.0
    a,b,c = img2.shape
    for i in range(a):
        for j in range(b):
            if img2[i,j][0]<140 and img2[i,j][2]<140 and img2[i,j,1] > 170:#include basically all the "green" pixels
                img2[i,j] = np.array([0,0,0])
    # print img3.shape, img2.shape
    for i in range(a):
        for j in range(b):
            if not (img2[i,j,0]==0 and img2[i,j,1]==0 and img2[i,j,2]==0):  #it is a black pixel
                img3[574+i, 250+j] = img2[i,j]
    plt.axis("off")
    plt.imshow(img3)
    mpimg.imsave('f.jpg',img3)
    plt.show()