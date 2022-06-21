from ast import Break
from cgitb import text
from gettext import find
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



class Aute:
    def __init__(self):
        self.ocr = OCRService(r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")
        self.path_directory = r"C:\Users\thiag\OneDrive\Área de Trabalho\CLIENTES\UL\COMPROVANTE_OCR_UL\comprovantes\validate"
        self.aute_list = []
        self.list_except= {"/":"7", "?":"9"}

    def FindAute(self, path_directory, image_name ):
        path_image = self.ocr.recognize_image(path_directory,image_name)
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


    def most_frequent(self, List):
        return max(set(List), key = List.count)

    def AuteRecz(self):
        images = [f for f in listdir(self.path_directory) if isfile(join(self.path_directory, f))]
        for image in images:
            aute= self.FindAute(self.path_directory, image)
            if aute != None:
                self.aute_list.append(aute)
        print(self.aute_list)
        print(self.most_frequent(self.aute_list))


find = Aute()
find.AuteRecz()