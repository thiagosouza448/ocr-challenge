import pathlib
import pytesseract
import os

try:
    from PIL import Image
except ImportError:
    import Image

# """
# |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|
# |   |TerminalType|dt_ImageRetrival  |                          Path      URL                               |<--|CSS Element|ImageText|
# |Ex:|Move 5000  | 07/08/2020        |"https://xd.adobe.com/view/526f0354-4677-7331-5b73b72a4112-245e/grid" |   |...       | "1.crédito ...|
# |   |TEXT       |DATETIME           |TEXT                                                                  |   |TEXT      |TEXT       |
# |                                                                                                               |...       |           |
#
# """


class OCRService:
    def __init__(self, tesseract_path):
        # content_root = pathlib.Path(__file__).parent.parent.parent.absolute()
        # print(content_root)
        # tesseract_path = r"Services\Utilities\Engine\Tesseract-OCR\tesseract.exe"
        print(tesseract_path)
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self.image_local = None
        self.screen_id = None

    def recognize_image(self, images_rep, screen_id):
        image_path = os.path.join(images_rep, screen_id)
        try:
            custom_config = r'-l por --oem 3 --psm 6 '
            string = pytesseract.image_to_string(Image.open(image_path), timeout=30, lang='por', nice=0, config=custom_config)
            return self.format_string(string)
        except RuntimeError as timeout_error:
            print(timeout_error)

    def recognize_image_custom(self, images_rep, screen_id, custom_config):
        image_path = os.path.join(images_rep, screen_id)
        try:
            string = pytesseract.image_to_string(Image.open(image_path), timeout=60, lang='por', nice=0, config=custom_config)
            return self.format_string(string)
        except RuntimeError as timeout_error:
            print(timeout_error)

    def build_custom_config(self, key: str):
        whitelist_set = set(key)
        whitelist = ""
        for c in whitelist_set:
            whitelist += c

        custom_config = r'-l por --oem 3 --psm 6 -c tessedit_char_whitelist={0} '.format(whitelist.replace(" ", ""))
        return custom_config


    def format_string(self, string):
        if '%' in string:
            s=string.split('%')
            return s[1]
        else:
            return string

    @staticmethod
    def find_in_substring(img1: str, list_image2_lower):
        index = img1.index("%")
        if index == 0:
            img1 = ''.join(img1[1:])
        else:
            img1 = ''.join(img1[:index])
        for word in list_image2_lower:
            tmp = ''.join(word)
            if tmp.find(img1) >= 0:
                return True

    def compare_image(self, string):
        for screen in os.listdir(self.temp_path):
            if string == self.print_string(self.temp_path, screen):
                return screen

    @staticmethod
    def compare_image_perc(image1: str, image2: str, percent: int, log=True):
        """
        Compara o conteúdo em texto de duas imagens.
        Separa as palavras de cada imagem, dividindo em duas listas
        Procura cada palavra encontrada na imagem1, dentro da imagem2
        Obtem o percentual de palavras encontradas e retorna True se o percentual estiver de acordo com o
        percntual esperado (parâmetro)
        """
        if image2 is None:
            return False

        list_image1 = image1.split()
        list_image1_lower = [[w.lower() for w in line] for line in list_image1]
        list_image2 = image2.replace("|", "").replace(".", " ").replace(":", "").split()
        list_image2_lower = [[w.lower() for w in line] for line in list_image2]
        acertos = 0
        total = len(list_image1)
        for img1 in list_image1_lower:
            if img1 in list_image2_lower:
                acertos += 1
            elif "%" in img1:
                if OCRService.find_in_substring(img1, list_image2_lower):
                    acertos += 1

        if total == 0:
            return False

        percentual = (acertos / total) * 100
        if log:
            print("palavras esperadas: ", list_image1)
            print("palavras reconhecidas: ", list_image2)
            print("{}%".format(percentual))

        return percentual >= percent, list_image1, list_image2, percentual


if __name__ == "__main__":
    run = OCRService()
    path_directory = r"C:\BK"
    image_name = "a.jpg"
    print(run.recognize_image(images_rep=path_directory, screen_id=image_name))


