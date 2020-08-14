# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:41:04 2019

@author: Rishabh Jain
"""

# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='..'
dataType='val2017'
annFile='C:/Users/Rishabh Jain/Downloads/annotations_trainval2017/annotations/instances_val2017.json'.format(dataDir,dataType)

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['person','dog','skateboard']);
imgIds = coco.getImgIds(catIds=catIds );
imgIds = coco.getImgIds(imgIds = [324158])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]


# load and display image
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# use url to load image
I = io.imread(img['coco_url'])
plt.axis('off')
plt.imshow(I)

plt.show()

Ri = input("Enter the side = ")
# load and display instance annotations
plt.imshow(I); plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
coco.showAnns(anns)

# initialize COCO api for person keypoints annotations
annFile = 'C:/Users/Rishabh Jain/Downloads/annotations_trainval2017/annotations/person_keypoints_train2017.json'.format(dataDir,dataType)
coco_kps=COCO(annFile)


# load and display keypoints annotations
plt.imshow(I); plt.axis('off')
ax = plt.gca()
annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco_kps.loadAnns(annIds)
coco_kps.showAnns(anns)