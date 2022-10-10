import cv2

class image:
    #ratings by catagory 
    properties_list = []
    color_matrix = [[]]

    # init method or constructor
    def __init__(self, name):
        self.name = name
    
    def preprocessing(self):
        return



def processImage(imageAddress):
    #input image
    img = cv2.imread('img.jpg', 1)

    cv2.imshow("Title", img)
    cv2.waitKey(0)

    hsvimg = cv2.cvtColor(img, cv2.COLOR)

    print(img[0][200])

    #pre-processesing to produce matrix of color (or whatever)
    #call various methods for calculating emphasis, harmony, etc with the image color matrix as input.

    #return image.properties_list
