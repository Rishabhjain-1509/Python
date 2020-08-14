# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:03:40 2019

@author: Rishabh Jain
"""

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread('A:/Rishi.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()