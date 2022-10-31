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
        painting1 = Painting("currentImage", "PaintingEmotion/ExamplePaintings/test.jpg")
        painting1.preprocessing()
        painting1.calculateProperties()
        with open('fixedLists\\badList.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(painting1.getPropertiesList())

