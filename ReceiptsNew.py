from ast import Break
from cgitb import text
from gettext import find
from operator import contains
import time
from datetime import datetime
import re
from os import listdir
from os.path import isfile, join
import json
from Services.Camera.CameraService import CameraService
from Services.OCR.OCRService import OCRService




class ReceiptsUtils:
    def __init__(self):

        self.list_key = []
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
                keyFind = str(str_dict[index])
                key_with_bar = keyFind.__contains__('/')
                key_with_interrogation = keyFind.__contains__('?')
                key_cv_treatment = key == "CV"

                if key_with_bar:
                    key_repl = keyFind.replace('/', '7')
                    return key_repl
                elif key_with_interrogation:
                    key_repl = keyFind.replace('?', '9')
                    return key_repl
                elif key_cv_treatment:
                    if keyFind.isnumeric():
                        return keyFind
                    else:
                        CV = keyFind[4:]
                        key_repl = "0000" + CV
                    return key_repl
                else:
                    return keyFind

    def most_frequent(self, List):
        if List:
            return max(set(List), key=List.count)
        else:
            print('nenhum item encontrado na lista')

    def find_key(self, path_directory, images, ocr, key):
        for image in images:
            key_word = self.find_list_key(path_directory, image, ocr, key)
            if key_word != None and key_word.isnumeric():
                self.list_key.append(key_word)
        return self.list_key


if __name__ == "__main__":
    # INSTANCE OCR FOR USING IN FIND_KEY
    ocr = OCRService(r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")
    # LIST IMAGE MOCK THAT GOING RECEIV
    list_image = ['2022-06-08-11-55-04.jpg', '2022-06-08-11-55-08.jpg', '2022-06-08-11-55-30.jpg',
                  '2022-06-08-11-55-11.jpg']
    path_directory = r"receipts\recp"
    # MOCK KWORDS
    key = 'AUTE'
    # INSTANCE CLASS
    find = ReceiptsUtils()
    # FIND KEY
    keys = find.find_key(path_directory, list_image, ocr, key)
    print(keys)
    # FIND KEY MORE FREQUENT IN LIST
    key_more_frequent = find.most_frequent(keys)
    print(key_more_frequent)
