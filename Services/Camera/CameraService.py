import time
import os
from datetime import datetime


import numpy as np
import cv2


# """
# no parameters needed for startup -> sends to database images -> currently being saved in the temp folder
# """
from PIL import Image

from Services.OCR.OCRService import OCRService


class CameraService:
    def __init__(self, cap):
        self.camera_port = 0
        self.path_directory = ""
        self.cap = cap

    def change_camera(self):
        # select camera VideoCapture(0) - notebook camera
        # select camera VideoCapture(1) - external camera (USB)
        self.camera_port = 0 if self.camera_port != 0 else 1

    def connect(self):
        pass
    def disconnect(self):
        pass

    def capture_image_zoom_mono(self, image_name: str, path_directory: str, zoom: int):
        self.cap = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if not ret:
                break

            # zoom
            # img = Image.fromarray(frame)
            # img = img.convert("L")
            # img = img.convert("1")
            # w, h = img.size
            # img = img.resize((w * zoom, h * zoom))

            img = np.array(frame)
            img = cv2.resize(img, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)

            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR5552BGRA)
            # kernel = np.ones((1, 1), np.uint8)
            # img = cv2.dilate(img, kernel, iterations=1)
            # img = cv2.erode(img, kernel, iterations=1)
            # img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            # img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            # img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            img = Image.fromarray(img)
            img.save(os.path.join(path_directory, image_name), "JPEG", dpi=(300, 300))
            # cv2.imwrite(os.path.join(path_directory, image_name), img)
            # self.cap.release()
            # cv2.destroyAllWindows()
            return os.path.join(path_directory, image_name)

    def capture_image_zoom(self, image_name: str, path_directory: str, zoom: int):
        # self.cap = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        # self.cap.set(3, 853)  # set the resolution
        # self.cap.set(4, 640)
        # self.cap.set(3, 1706)  # set the resolution
        # self.cap.set(4, 1280)
        # self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
        # self.cap.set(cv2.CAP_PROP_FOCUS, 40)
        # self.cap.set(cv2.CAP_PROP_ZOOM, 220)
        # self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        # self.cap.set(cv2.CAP_PROP_AUTO_WB, 0)
        # self.cap.set(cv2.CAP_PROP_BRIGHTNESS, 5)
        # self.cap.set(cv2.CAP_PROP_CONTRAST, 10)

        # self.cap.set(40, focus)
        # cv2. or cv2.
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if not ret:
                break

            # zoom
            # img = Image.fromarray(frame)
            # img = img.convert("L")
            # img = img.convert("1")
            # w, h = img.size
            # img = img.resize((w * zoom, h * zoom))

            img = np.array(frame)

            # auto_result, alpha, beta = self.automatic_brightness_and_contrast(img)
            img = self.adjust_gamma(img)
            cv2.imwrite(os.path.join(path_directory, image_name), img)
            # if True:
            #     return os.path.join(path_directory, image_name)


            img = cv2.resize(img, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)

            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            kernel = np.ones((1, 1), np.uint8)
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)

            # img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            # img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            # img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            # img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            img = Image.fromarray(img)
            img.save(os.path.join(path_directory, image_name), "JPEG", dpi=(600, 600))
            # cv2.imwrite(os.path.join(path_directory, image_name), img)
            # self.cap.release()
            # cv2.destroyAllWindows()
            return os.path.join(path_directory, image_name)

    def take_snapshot(self, filename: str, path_directory: str, vs):
        # grab the current timestamp and use it to construct the
        # output path
        ts = datetime.now()
        p = os.path.sep.join((path_directory, filename))
        img = np.array(vs.read().copy())
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
        self.cap.set(cv2.CAP_PROP_FOCUS, 40)

        # save the file
        cv2.imwrite(os.path.join(path_directory, image_name), img)
        # cv2.imwrite(p, vs.read().copy())
        # print("[INFO] saved {}".format(filename))

    def take_snapshot_zoom(self, image_name: str, path_directory: str, vs, zoom: int):
        # grab the current timestamp and use it to construct the
        # output path
        img = np.array(vs.read().copy())
        img = cv2.resize(img, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = Image.fromarray(img)
        img.save(os.path.join(path_directory, image_name), "JPEG", dpi=(600, 600))
        # cv2.imwrite(os.path.join(path_directory, image_name), img)
        # self.cap.release()
        cv2.destroyAllWindows()

        # p = os.path.sep.join((path_directory, filename))
        # # save the file
        # cv2.imwrite(p, vs.read().copy())
        # print("[INFO] saved {}".format(path_directory))

    def capture_image(self, image_name: str, path_directory: str):
        # self.cap = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        # self.cap.set(3, 853)  # set the resolution
        # self.cap.set(4, 640)
        # self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # turn the autofocus off
        # self.cap.set(cv2.CAP_PROP_FOCUS, 50)
        # self.cap.set(cv2.CAP_PROP_FOCUS, 40)
        # self.cap.set(cv2.CAP_PROP_ZOOM, 220)
        # self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        # self.cap.set(cv2.CAP_PROP_AUTO_WB, 0)
        # self.cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)
        # self.cap.set(cv2.CAP_PROP_CONTRAST, 10)
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if not ret:
                break

            title = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            cv2.imwrite(os.path.join(path_directory, image_name), frame)
            # self.cap.release()
            # cv2.destroyAllWindows()
            return os.path.join(path_directory, image_name)

    def convert_scale(self, img, alpha, beta):
        """Add bias and gain to an image with saturation arithmetics. Unlike
        cv2.convertScaleAbs, it does not take an absolute value, which would lead to
        nonsensical results (e.g., a pixel at 44 with alpha = 3 and beta = -210
        becomes 78 with OpenCV, when in fact it should become 0).
        """

        new_img = img * alpha + beta
        new_img[new_img < 0] = 0
        new_img[new_img > 255] = 255
        return new_img.astype(np.uint8)

    # Automatic brightness and contrast optimization with optional histogram clipping
    def automatic_brightness_and_contrast(self, image, clip_hist_percent=25):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate grayscale histogram
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist_size = len(hist)

        # Calculate cumulative distribution from the histogram
        accumulator = []
        accumulator.append(float(hist[0]))
        for index in range(1, hist_size):
            accumulator.append(accumulator[index - 1] + float(hist[index]))

        # Locate points to clip
        maximum = accumulator[-1]
        clip_hist_percent *= (maximum / 100.0)
        clip_hist_percent /= 2.0

        # Locate left cut
        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1

        # Locate right cut
        maximum_gray = hist_size - 1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        # Calculate alpha and beta values
        alpha = 255 / (maximum_gray - minimum_gray)
        beta = -minimum_gray * alpha

        '''
        # Calculate new histogram with desired range and show histogram 
        new_hist = cv2.calcHist([gray],[0],None,[256],[minimum_gray,maximum_gray])
        plt.plot(hist)
        plt.plot(new_hist)
        plt.xlim([0,256])
        plt.show()
        '''

        auto_result = self.convert_scale(image, alpha=alpha, beta=beta)
        return auto_result, alpha, beta

    def adjust_gamma(self, image, gamma=1.0):
        # build a lookup table mapping the pixel values [0, 255] to
        # their adjusted gamma values
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")
        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)


if __name__ == "__main__":
    run = CameraService()
    path_directory = r"C:\UL\Projetos\orchestrator\LocalMemory\CameraTemp"
    image_name = '{}.png'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    print(run.capture_image(image_name, path_directory))

    run = OCRService()
    print(run.recognize_image(path_directory, image_name))

