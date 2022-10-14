import cv2
#from balance import calcBalance
#from emphasis import calcEmphasis
#from harmony import calcHarmony
#from variety import calcVariety
#from gradation import calcGradation
#from movement import calcMovement


class Painting: 
    properties_list = [0]*6
    img = [[[]]]
    hsv_img = [[[]]]

    # init method or constructor
    def __init__(self, name, imageAddress):
        self.name = name
        self.imageAddress = imageAddress
    
    def preprocessing(self):
        #pre-processesing on image
        
        #input image
        self.img = cv2.imread(self.imageAddress, 1)

        self.hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        #hsv_img is a 2d array with the inner array having values:
            #HUE = 0 - 180 (179?)
            #SATURATION = 0 - 255
            #VALUE = 0 - 255

        #TODO: any additional preprocessing? scaling?
        print("preprocessing complete")
        return

    def calculateProperties(self):
        #call all feature algorithms and return a list of feature scores normalized from 0 to 1

        #TODO: remove once a feature is complete and integrated into driver
        self.properties_list = [0.5]*6

        #call balance
        #self.properties_list[0] = calcBalance(self.hsv_img)

        #call emphasis
        #self.properties_list[1] = calcEmphasis(self.hsv_img)
        
        #call harmony
        #self.properties_list[2] = calcHarmony(self.hsv_img)

        #call variety
        #self.properties_list[3] = calcVariety(self.hsv_img)

        #call gradation
        #self.properties_list[4] = calcGradation(self.hsv_img)

        #call movement
        #self.properties_list[5] = calcMovement(self.hsv_img)
        print("properties calculations complete")
        return

    def getImage(self):
        return self.img

    def getHSVImage(self):
        return self.hsv_img

    def getPropertiesList(self):
        return self.properties_list
