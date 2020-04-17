#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

def heart(im):
    """It takes an image im as input, and outputs a heart-shaped cut-out of it on a pink background."""
    im2 = im.copy()
    x,y,z = im2.shape
    print x,y,z
    for i in range(x):
        for j in range(y/2):
            if i-j > x-(y/2):
                im2[i,j] = np.array([229,178,229])
                im2[i,y-j-1] = np.array([229,178,229])  #make the right side of the picture symmetrically for pink
            r = (y/4)*1.05
            if i < r and (i-y/4)**2+(j-y/4)**2>r**2:    #the region above the upper circle centered at (y/4, y/4)
                im2[i,j] = np.array([229,178,229])
                im2[i, y-j-1] = np.array([229,178,229])

    return im2

# img1 = mpimg.imread('kitty-cat.jpg')
# img2 = heart(img1)
# plt.axis('off')
# plt.imshow(img2)
# plt.show()


def blurring(im, method):
    """It takes a gray-scale picture, and offers two options for noise blurring: uniform or Gaussian."""
    im2 = im.copy()
    if im2.dtype=="uint8":
        im2=im2/255.0
    x,y,z = im2.shape
    if method == 'uniform':
        k = 5
        mult = np.array([[1.0 / k ** 2] * k] * k)  # times each value with 1/(k*k) to calculate the average
        for i in range(k/2, x-k/2):
            for j in range(k/2, y-k/2):
                temp = im[(i - (k - 1) / 2):(i + (k - 1) / 2) + 1, (j - (k - 1) / 2):(j + (k - 1) / 2) + 1,0]
                im2[i,j] = np.sum(temp*mult)
        return im2
    if method == 'Gaussian':
        sigma = 1
        k = 5
        filter = np.array([[0] * k] * k, dtype='float')
        for a in range(k):
            for b in range(k):
                filter[a, b] = np.exp(-((a - (k - 1) * 0.5) ** 2 + (b - (k - 1) * 0.5) ** 2) / (2.0 * sigma ** 2))
        filter_sum = np.sum(filter)
        filter = filter / filter_sum    #now filter is the Gaussian filter
        # print filter
        x,y,z=im2.shape
        for i in range(k/2, x-(k/2)):
            for j in range(k/2, y-k/2):
                temp = im[(i - (k - 1) / 2):(i + (k - 1) / 2) + 1, (j - (k - 1) / 2):(j + (k - 1) / 2) + 1,0]
                im2[i,j]=np.sum(temp*filter)
        return im2
    return im2

# img3 = mpimg.imread('kitty-cat.jpg')
# img3 = img3/255.0
# greyImg = img3[:,:,0]*0.21+img3[:,:,1]*0.72+img3[:,:,2]*0.07
# greyImg = np.repeat(greyImg[:, :, np.newaxis], 3, axis=2)
# plt.imshow(greyImg)
# plt.show()
# # res1 = blurring(greyImg, "uniform")
# # plt.imshow(res1)
# # plt.show()
# res2 = blurring(greyImg, "Gaussian")
# plt.imshow(res2)
# plt.show()

def detect_edge(im, method):
    """It takes a gray-scale image and detects edges, with the option of horizontal, vertical or both."""
    im2 = im.copy()
    if im2.dtype=="uint8":
        im2=im2/255.0
    x,y,z = im2.shape
    vertical_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    horizontal_filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    if method == "vertical":
        for i in range(1,x-1):
            for j in range(1,y-1):
                temp = im[(i-1):(i+2), (j-1):(j+2), 0]
                im2[i,j] = (np.sum(temp*vertical_filter)+4)/8.0 #normalize
        return im2
    if method == "horizontal":
        for i in range(1,x-1):
            for j in range(1,y-1):
                temp = im[(i-1):(i+2), (j-1):(j+2), 0]
                im2[i,j] = (np.sum(temp*horizontal_filter)+4)/8.0
        return im2
    if method == "both":
        for i in range(1,x-1):
            for j in range(1,y-1):
                temp = im[(i-1):(i+2), (j-1):(j+2), 0]
                im2[i,j] = math.sqrt(np.sum(temp*horizontal_filter)**2+np.sum(temp*vertical_filter)**2)/4
        return im2
    return im2

# img4 = mpimg.imread('edge1.jpg')
# hor = detect_edge(img4,"both")
# plt.axis('off')
# plt.imshow(hor)
# plt.show()