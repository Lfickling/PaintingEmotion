import csv as csv
import os.path
from Image_processing.painting import Painting

"""
    This Python file will create the data we will need for the future model. It calls 
    the image processing features and tags on image name and emotion. The image name will be used for checkpoints
    during this process and the emotion will be used as a machine learning label.
    - Daniel Martinez -
"""


def checkpointCheck(current_image):
    """
    @param current_image: Name of the image from directory
    @type current_image: String
    @return: True or False, based on if the image name already exists in the CSV
    @rtype: Boolean
    """
    with open("csvTraining.csv", "r", encoding='UTF-8') as currentCsv:
        reader = csv.reader(currentCsv)
        if any(current_image in item for item in reader):
            return True
    return False


listOfDir = os.listdir('../ArtSamples-300 each')
for emotion in listOfDir:
    filesList = os.listdir('../ArtSamples-300 each/' + emotion)
    for image in filesList:
        if not checkpointCheck(image):
            with open('csvTraining.csv', 'a', newline='', encoding='UTF-8') as edit:
                painting1 = Painting("currentImage", '../ArtSamples-300 each/' + emotion + '/' + image)
                painting1.preprocessing()
                painting1.calculateProperties()
                data = painting1.getPropertiesList()  # Retrieve Data from Image Processing features
                data.append(image)  # Adding name for checkpointCheck
                data.append(emotion)  # Label for future training
                writer = csv.writer(edit)
                writer.writerow(data)
