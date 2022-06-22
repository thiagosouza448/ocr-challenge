from findKey import Receipts
from Services.OCR.OCRService import OCRService

ocr = OCRService(r"C:\AUT_RPA_V2\Services\Utilities\Engine\Tesseract-OCR\tesseract.exe")


list_image = ['2022-06-08-11-55-00.jpg','2022-06-08-11-55-26.jpg', '2022-06-08-12-09-17.jpg', '2022-06-08-12-09-21.jpg']
key = 'AUTE'

find = Receipts()
keys = find.find_key(list_image, ocr,  key)
key_more_freq = find.most_frequent(keys)

print(keys)
print(key_more_freq)

