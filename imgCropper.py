# Crops image files.
# 23 Feb 2021
# Intended for use for cropping contact image files.

## implemented with Python3 on Anaconda.

## import basic modules
import numpy as np
import scipy as sp
import os
import pandas as pd
import cv2
from PIL import Image

folder='.'

tag='.png'

## set folders
path1=folder+'/rawImg/'
os.makedirs(path1, exist_ok=True) 
path2=folder+'/croppedImg/'
os.makedirs(path2, exist_ok=True)
path3=folder+'/filteredImg/'
os.makedirs(path3, exist_ok=True)
path4=folder+'/filteredCroppedImg/'
os.makedirs(path4, exist_ok=True)

## gather list of files
def fileSearch(pathway,tag):
    results=list()
    results += [each for each in os.listdir(pathway) if each.endswith(tag)]
    results=np.asarray(results)
    results=np.sort(results)
    print(results)
    return(results)



## import and process files

def loadImage(img):
    I1=np.asarray(img)

    # filter the array

    I=np.where(I1 < 99, 255, 0)
    ## convert array to image for export

    I8 = (((I - I.min()) / (I.max() - I.min())) * 255.9).astype(np.uint8)

    I8 = cv2.bitwise_not(I8)
    return(I8,I1,I)


def exportFilteredImg(I8,fileName,path3):

    img = Image.fromarray(I8) 
    outName='mugu.png'
    outName=path3+'filtered_'+fileName
    img.save(outName)
    print(outName)
    return(outName)



def findCenterLine(I8):

## find the needle and center the calculations relative to it
    arr=I8[0,:]
    arr=arr.flatten()
    cond = np.diff(arr, append=-1) == 255
    indices = np.argwhere(cond)
    rights=int(np.max(indices))

    cond = np.diff(arr, append=1) == -255
    indices = np.argwhere(cond)
    lefters=int(np.min(indices))
    topVal=int(np.floor(.5*(rights+lefters)))

    print(topVal)
    return(topVal)



def findEndLine(I8,topVal):
# calculate bottom of droplet
    row,col=np.shape(I8)
    endLine=int(row-1)
    for ix in range(topVal,(row-1)):
        testLine=I8[ix,:]
        testLine=testLine.flatten()
        darkZones=np.where(testLine==0)
        darkZones=darkZones[0]
        darkZones.tolist()
        darkPoints=int(len(darkZones))
        liteZones=np.where(testLine!=0)
        liteZones=liteZones[0]
        liteZones.tolist()
        litePoints=int(len(liteZones))

        if darkPoints>litePoints:
            print(ix)
            endLine=int(ix)
            break
   # break
    return(endLine,row,col)



def findDropletEdge(I8,endLine,topVal):

    arr=I8[0:endLine,topVal]
    arr=arr.flatten()
#print(arr)
    cond = np.diff(arr, append=1) == -255
#cond = np.diff(arr, append=-1) == 255
    indices = np.argwhere(cond)
#changePoint=np.where(testVector==[255])
#print(indices)
    topPoint=int(indices[0])
    ratchetScore=int(0)
    if topPoint < int(150):
        topPoint=int(indices[1])
        ratchetScore=int(1)
    if topPoint < int(150):
        topPoint=int(222)

    #if topPoint < int(150):
    #    topPoint=int(indices[2])
#
    #if topPoint < int(150):
    #    topPoint=int(indices[3])

#    if topPoint > endLine:
 #       topPoint=int(abs(endLine-topPoint))

    #print(topPoint)
    try:
        centerPoint=int(indices[1+ratchetScore])

    except:
        centerPoint=int(np.round((topPoint+endLine)/2))
## scanning for left and right points
    print(centerPoint)
    arr=I8[centerPoint,:]
    arr=arr.flatten()
    cond = np.diff(arr, append=-1) == 255
    indices = np.argwhere(cond)
   # print(indices)
    rights=int(np.max(indices))

    cond = np.diff(arr, append=1) == -255
    indices = np.argwhere(cond)
    lefters=int(np.min(indices))
   # print(indices)
    bellyBeast=int(abs(lefters-rights))
    if bellyBeast < 50:
        lefters=int(250)
        rights=int(420)
    
    return(rights,lefters,topPoint,centerPoint)


def finalCropLines(topPoint,endLine,lefters,rights,row):
## shifting for error and selecting final cropping index
    leftPoint=abs(int(lefters-20))
    ritePoint=abs(int(rights+20))
    left = leftPoint
    top = int(topPoint)
    right = ritePoint
    bottom = int(endLine+20)

  #  print(top)
   # print(bottom)

#    print(left)
 #   print(right)
    print(topPoint)
    return(top,bottom,left,right)



def exportfilteredCroppedImg(I8,fileName,path4,top,bottom,left,right):
# export cropped and filtered image
    I2=I8[top:bottom,left:right]
    img = Image.fromarray(I2)
    outName2='filteredCropped_'+fileName
    outName=path4+outName2
#outName='mugu2.png'
    print(outName)
    img.save(outName)

    return(I2,outName)



def exportCroppedImg(I1,fileName,path2,top,bottom,left,right):
# export cropped image
    I32=I1[top:bottom,left:right]
    img3 = Image.fromarray(I32)
    outName33='cropped_'+fileName
    outName=path2+outName33
    print(outName)
    img3.save(outName)
    return(I32,outName)

## main looped commands


# set list
results=fileSearch(path1,tag)

# loading phase
#fileName=results[0]

for oy in range(0,len(results)):
    fileName=results[oy]
    print(fileName)
#img=Image.open(fileName)
    img=Image.open(path1+fileName)

    I8,I1,I=loadImage(img)
# calculation phase
    topVal=findCenterLine(I8)
    endLine,row,col=findEndLine(I8,topVal)
    rights,lefters,topPoint,centerPoint=findDropletEdge(I8,endLine,topVal)
    top,bottom,left,right=finalCropLines(topPoint,endLine,lefters,rights,row)

# export files
    outName=exportFilteredImg(I8,fileName,path3)
    I2,outName=exportfilteredCroppedImg(I8,fileName,path4,top,bottom,left,right)
    I32,outName=exportCroppedImg(I1,fileName,path2,top,bottom,left,right)
