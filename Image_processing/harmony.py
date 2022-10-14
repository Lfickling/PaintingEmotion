#harmony calculation: written initially by Nicole and Lettie
import math
import numpy as np
from scipy.signal import argrelextrema

#HUE = 0 - 180 (179?)
#SATURATION = 0 - 255
#VALUE = 0 - 255

#TODO: Does this need to be generalized? right now it is specific to hue
#if so the '22.5' needs to be changed to the range of the new metric / 8
def genNeighborhoodHistogram(neighborhoodMatrix):
    neighborhoodHistogram = [0]*8
    shape = neighborhoodMatrix.shape
    # for each pixel in neighborhood:
    for x in range(shape[0]):
        for y in range(shape[1]):
            # grab first number in tuple at (x, y) which is the hue, determine which 'bucket' it belongs to
            hue = int(neighborhoodMatrix[x,y,0].tolist() // 22.5)
            # increment count for bucket
            neighborhoodHistogram[hue] += 1
    return neighborhoodHistogram

# calc max modes OPT 1
# check edge cases for histogram
# calculate local maxima and minima
# partition histogram array into c and I\c 
# determine value (count) of maximum, and index of location

def calcPixelHarmony(neighborhoodHistogram):
    modes = [[0,0],[0,0]]
    #find the maxima and minima
    maxima = argrelextrema(np.array(neighborhoodHistogram), np.greater, mode= 'wrap')
    #print(maxima)
    #minima = argrelextrema(neighborhoodHistogram, np.less)
    modes[0][1] = max(neighborhoodHistogram)
    modes[0][0] = neighborhoodHistogram.index(modes[0][1])
    for i in maxima[0]:
        secondMaxValue = neighborhoodHistogram[i]
        if secondMaxValue > modes[1][1]:
            modes[1][0], modes[1][1] = i, secondMaxValue

    return calcModeHarmony(modes)
"""
# calc max modes OPT 2
# consider all possible values of c (splitting histogram in all possible ways?)
# harmony intensity will calculated 56 times per pixel to find lowest possible value (why lowest??)
def calcPixelHarmony(neighborhoodHistogram):
    minHarmony = 1
    modes = [[0,0],[0,0]]
    for i in range(len(neighborhoodHistogram)-1):
        for j in range(i, len(neighborhoodHistogram)):
            if i%7 == j%7:
                continue
            c, ic = neighborhoodHistogram[i:j], neighborhoodHistogram[j:] + neighborhoodHistogram[:i]
            #print(f"i: {i} j: {j}")
            modes[0][1], modes[1][1] = max(c), max(ic)
            modes[0][0], modes[1][0] = c.index(modes[0][1]), ic.index(modes[1][1])
            pixelHarmony = calcModeHarmony(modes)
            if pixelHarmony < minHarmony:
                minHarmony = pixelHarmony
            modes[0], modes[1] = modes[1], modes[0]
            pixelHarmony = calcModeHarmony(modes)
            if pixelHarmony < minHarmony:
                minHarmony = pixelHarmony
    return minHarmony
"""

#calculate the individual pixel harmony based on a tuple of the two max modes 
#modes[colorcatagory, quantity]
def calcModeHarmony(modes):
    pixelHarmony = math.exp(-abs(modes[0][1] - modes[1][1])) * abs(modes[0][0] - modes[1][0])
    return pixelHarmony

#main function / driver of harmony calculation
def calcHarmony(hsvImg):
    # sum of each pixel's harmony intensity
    totalHarmony = 0
    neighborhood_dimension = 9 #grid must be odd!!
    xy_init = neighborhood_dimension // 2 # 4

    img_wid = hsvImg.shape[1] # left to right
    img_len = hsvImg.shape[0] # up to down


    # anchor coords represented by x, y. x goes lengthwise, y goes widthwise
    for x in range(xy_init, (img_len - xy_init)):  #img_len - xy_init should be 4 less than the end of line

        for y in range(xy_init, (img_wid - xy_init)):
            # pull out submatrix surrounding anchor
            neighMatrix = hsvImg[(x - xy_init):(x + xy_init) + 1, (y - xy_init):(y + xy_init) + 1]
            histogram = genNeighborhoodHistogram(neighMatrix)
            totalHarmony += calcPixelHarmony(histogram)

    return totalHarmony



