import cv2
import numpy as np
# from balance import calcBalance
# from emphasis import calcEmphasis
from harmony import calcHarmony

# from variety import calcVariety
# from gradation import calcGradation
# from movement import calcMovement

img_size_x = 300
img_size_y = 300


class Painting:

    # init method or constructor
    def __init__(self, name, imageAddress):
        self.name = name
        self.imageAddress = imageAddress
        self.properties_list = [0] * 6
        self.img = np.zeros((1, 1, 1), dtype=np.int32)
        self.hsv_img = np.zeros((1, 1, 1), dtype=np.int32)

    def preprocessing(self):
        # pre-processesing on image

        # input image
        self.img = cv2.imread(self.imageAddress, 1)

        self.hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        # hsv_img is a 3d numpy array with the inner array having values:
        # HUE = 0 - 180 (179?)
        # SATURATION = 0 - 255
        # VALUE = 0 - 255

        # TODO: any additional preprocessing? scaling?
        self.hsv_img = cv2.resize(self.hsv_img, (img_size_x, img_size_y))
        # maybe try to scale it proportionally?

        print("preprocessing complete")
        return

    def calculateProperties(self):
        # call all feature algorithms and return a list of feature scores normalized from 0 to 1

        # TODO: remove once a feature is complete and integrated into driver
        # self.properties_list = [0.5]*6

        # call balance
        # self.properties_list[0] = calcBalance(self.hsv_img)

        # call emphasis
        # self.properties_list[1] = calcEmphasis(self.hsv_img)

        # call harmony
        self.properties_list[2] = calcHarmony(self.hsv_img)

        # call variety
        # self.properties_list[3] = calcVariety(self.hsv_img)

        # call gradation
        # self.properties_list[4] = calcGradation(self.hsv_img)

        # call movement
        # self.properties_list[5] = calcMovement(self.hsv_img)
        print("properties calculations complete")
        return

    def getImage(self):
        return self.img

    def getHSVImage(self):
        return self.hsv_img

    def getPropertiesList(self):
        return self.properties_list
