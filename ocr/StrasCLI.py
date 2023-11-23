from InquirerPy import prompt
import os
import cv2
from PIL import Image
import pytesseract
import utils.Messages as Messages
import utils.Prompt as Q
import utils.FilesHelper as FH
import utils.ImageManipulation as IM
import utils.Settings as Settings
import utils.OCR as OCR
import utils.DataCleaning as DC
import utils.GeoTreatment as GT
#https://github.com/UB-Mannheim/tesseract/wiki


def main():
    config = Settings.get_config()
    folder = ""
    while True:
        choice = prompt(Q.menu)
        match choice[0]:
            case 1:
                pages = prompt(Q.pages)
                FH.download(config["source"], pages["start"], pages["end"])
            case 2:
                folder = prompt(Q.choose_folder)
                pass
            case 3:
                folder = prompt(Q.choose_folder)
                pass
            case 4:
                folder = prompt(Q.choose_folder)
                IM.segmentation(folder)
            case 5:
                pass
            case 6:
                pass
            case 0:
                return 1
            case _:
                print("Option invalide")


if __name__ == '__main__':
    main()
