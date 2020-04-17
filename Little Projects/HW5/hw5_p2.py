#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

if __name__ == "__main__":
    img1 = mpimg.imread('g.jpg').copy()
    img2 = mpimg.imread('h.jpg').copy()
    img1 = img1 / 255.0
    img2 = img2 / 255.0
    a, b, c = img1.shape
    img3 = np.empty([a, b, c])
    for i in range(a):
        for j in range(b):
            for k in range(c):
                img3[i, j, k] = abs(img2[i, j, k]-img1[i, j, k])    #find the difference
    plt.axis('off')
    plt.imshow(img3)
    mpimg.imsave('i.jpg', img3)
    plt.show()
