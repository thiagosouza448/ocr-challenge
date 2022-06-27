from findKey import Receipts
from Services.OCR.OCRService import OCRService




ocr = OCRService(r"OCR\Tesseract-OCR\tesseract.exe")
# LIST IMAGE MOCK THAT GOING RECEIV
list_image = ['2022-06-27-10-20-46.jpg','2022-06-27-10-20-58.jpg', '2022-06-27-10-21-01.jpg', '2022-06-27-10-21-13.jpg']
path_directory = r"D:\ESTUDO\PYTHON\OCR\ocr-challenge\receipts\CV\CV645"
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
