import numpy as np
import pandas as pd

from PIL import Image
#import cv2
import os, glob
#import dir

tag='.tif'
folder='.'
outTag='.png'

results=list()
results += [each for each in os.listdir(folder) if each.endswith(tag)]


print(results)

nameList=list()
vpaList=list()
areaList=list()
totalAreaList=list()

nameFile=results[0]
#it = cv2.imread(nameFile)
#img = cv2.imread(nameFile, -1)
#img = np.array(it, dtype = np.uint16)

#print(img)
#cv2.imwrite('test.png', img)
for iy in range(0,len(results)):
        nameFile=results[iy]

        im = Image.open(nameFile).convert('RGBA')
        outName=nameFile+outTag
        print(outName)
        im.save(outName)
