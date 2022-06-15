from ast import Break
from cgitb import text
from operator import contains
import time
from datetime import datetime
import re
from os import listdir
from os.path import isfile, join

import cv2
import json
from Services.Camera.CameraService import CameraService
from Services.OCR.OCRService import OCRService




# ADD BASEDIR TESSERACT.EXE
ocr = OCRService( r"")

path_directory = r""

# path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")
path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")


# path images
images = [f for f in listdir(path_directory) if isfile(join(path_directory, f))]


# dictionary for save all numbers
aute_dict = []




def FindAute(path_directory, image_name ):
    path_image = ocr.recognize_image(path_directory,image_name)
    list_image1 = re.split('\n|:| ', path_image)
    str_dict = []
    for item in list_image1:
        if item != '' and item != None and item != '|' and item != '-':
            str_dict.append(item.upper())
    # print(str_dict)
    index = 0
    for a in str_dict:
        index+=1
        if a == "AUTE":
            aute = str(str_dict[index])

            # vars for bolean returns about validation 
            aute_with_bar = aute.__contains__('/')
            aute_with_interrogation = aute.__contains__('?')


            if aute_with_bar:
               aute_rp=  aute.replace('/', '7')
               return aute_rp
            elif aute_with_interrogation:
                aute_rp=  aute.replace('?', '9')
                return aute_rp
            else: 
                return aute


for image in images:
    aute= FindAute(path_directory, image)
    if aute != None:
        aute_dict.append(aute)
print(aute_dict)