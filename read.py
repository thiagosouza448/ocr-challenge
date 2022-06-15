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









# teste = json.dumps(map_image, indent=4, separators=(". ", " = "))
# lowerText = teste.lower().replace("(c)\n", "")
# text_split = lowerText.split()

# # print(text_split)



# y = 0
# for x in text_split:
#     y += 1
#     try:
#         if x.__contains__("aute"):
#             i = y
#             concatenated = text_split[i-1]
#             concat_str = concatenated.replace("aute", "").split(":")

#             not_concatenated = text_split[i]

#             if len(concat_str[1]) == 6:
#                 print(concat_str[1])
#             elif len(not_concatenated) == 6:
#                 print(not_concatenated)

#     except:
#         print("nenhum Aute encontrado")
