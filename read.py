from cgitb import text
from email.policy import default
import time
from datetime import datetime
import re

import cv2
import json
from Services.Camera.CameraService import CameraService
from Services.OCR.OCRService import OCRService

ocr = OCRService(r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")

path_directory = r"C:\Users\thiag\OneDrive\Área de Trabalho\CLIENTES\UL\COMPROVANTE_OCR_UL\comprovantes\validate"

# path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")
path_image = ocr.recognize_image(path_directory, "2022-06-08-12-09-06.jpg")

def FindAute(path_image):
    list_image1 = re.split('\n|:| ', path_image)
    str_dict = []
    for item in list_image1:
        if item != '' and item != None and item !='|' and item !='-':
            str_dict.append(item.upper())     
    # print(str_dict)
    index_aute = str_dict.index('AUTE')     
    find_aute = str_dict[index_aute+1]  
    print(str_dict[index_aute+1])
    return find_aute


aute = FindAute(path_image)