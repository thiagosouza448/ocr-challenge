from cgitb import text
import time
from datetime import datetime

import cv2
import json
from Services.Camera.CameraService import CameraService
from Services.OCR.OCRService import OCRService

from matplotlib import pyplot as plt


def mostrar(img):
    fig= plt.gcf()
    fig.set_size_inches(16,8)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.show()






img =  cv2.imread("comprovantes\validate\2022-06-08-11-55-04.jpg")
(H,W) = img.shape=[:2]

