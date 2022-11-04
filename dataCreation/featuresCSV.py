import pandas
import os, os.path
import fnmatch
import re
import csv
from Image_processing.painting import Painting

listOfDir = os.listdir('../ArtSamples-150_files_each')
for emotion in listOfDir:
    filesList = os.listdir('../ArtSamples-150_files_each/' + emotion)
    for image in filesList:
        with open('csvTraining.csv', 'a') as fd:
            if any(image in item for item in fd):
                break
            else:
                writer = csv.writer(fd)
                painting1 = Painting("currentImage", '../ArtSamples-150_files_each/' + emotion + '/' + image)
                painting1.preprocessing()
                painting1.calculateProperties()
                data = painting1.getPropertiesList()
                data.append(image)
                data.append(emotion)
                writer.writerow(data)
