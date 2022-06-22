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


class ReceiptsUtils:
    def __init__(self):
     
        self.aute_list = []
        self.list_except = {"/": "7", "?": "9"}



    def find_list_key(self, path_directory, image_name, ocr, key):
        path_image = ocr.recognize_image(path_directory, image_name)
        list_image1 = re.split('\n|:| ', path_image)
        str_dict = []
        for item in list_image1:
            if item != '' and item != None and item != '|' and item != '-':
                str_dict.append(item.upper())
        # print(str_dict)
        index = 0
        for a in str_dict:
            index += 1
            if a == key:
                aute = str(str_dict[index])
                aute_with_bar = aute.__contains__('/')
                aute_with_interrogation = aute.__contains__('?')

                if aute_with_bar:
                    aute_rp = aute.replace('/', '7')
                    return aute_rp
                elif aute_with_interrogation:
                    aute_rp = aute.replace('?', '9')
                    return aute_rp
                else:
                    return aute

    def most_frequent(self, List):
        if List:
            return max(set(List), key=List.count)
        else:
            print('nenhum item encontrado na lista')

    def find_key(self, path_directory , images, ocr, key):
        for image in images:
            aute = self.find_list_key(path_directory, image, ocr, key)
            if aute != None:
                self.aute_list.append(aute)
        return self.aute_list





if __name__ == "__main__":
        # INSTANCE OCR FOR USING IN FIND_KEY
    ocr = OCRService(r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")
    # LIST IMAGE MOCK THAT GOING RECEIV
    list_image = ['2022-06-08-11-55-00.jpg','2022-06-08-11-55-26.jpg', '2022-06-08-12-09-17.jpg', '2022-06-08-12-09-21.jpg']
    path_directory = r"D:\PROJETOS\UL\ocr-challenge\comprovantes\validate"
    # MOCK KWORDS
    key = 'AUTE'
    # INSTANCE CLASS
    find = ReceiptsUtils()
    # FIND KEY
    keys = find.find_key(path_directory, list_image, ocr,  key)
    print(keys)
    # FIND KEY MORE FREQUENT IN LIST
    key_more_frequent = find.most_frequent(keys)
    print(key_more_frequent)