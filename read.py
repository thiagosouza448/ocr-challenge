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



# TODO: IMPROVE THIS SERVICE OCR, TRY ADD BASE DIR AND CONCAT WITH NAME APPLICATION, CREATE JSON WITH BASEDIR

# ADD BASEDIR TESSERACT.EXE
ocr = OCRService(
    r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")

path_directory = r"C:\Users\thiag\OneDrive\Área de Trabalho\CLIENTES\UL\COMPROVANTE_OCR_UL\comprovantes\validate"

# path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")
# path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")


# path images
images = [f for f in listdir(path_directory) if isfile(join(path_directory, f))]


# dictionary for save all numbers
aute_list = []



# TODO: create a list exception with itens that ocr not recognize, with wrong value and correct option
list_except= {"/":"7", "?":"9"}


def most_frequent(List):
    return max(set(List), key = List.count)


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
        aute_list.append(aute)
print(aute_list)
print(most_frequent(aute_list))