#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Wenxuan Liu 805152602
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
if __name__ == "__main__":
    img1 = mpimg.imread('a.jpg')
    img2 = mpimg.imread('b.jpg')
    img3 = img1.copy()
    img3[250:650, 100:500] = img2.view()
    plt.imshow(img3)
    plt.axis('off')
    mpimg.imsave('c.jpg', img3)
    plt.show()
