from InquirerPy import prompt
import os
import cv2
from PIL import Image
import pytesseract
import utils.Messages as Messages
import utils.Prompt as Prompt
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
        Messages.Menu()
        choice = input("Quel option souhaitez-vous choisir?  ")
        match choice:
            case "1":
                pages = prompt(Prompt.pages)
                folder = FH.download(config["source"], pages["start"], pages["end"])
            case "2":
                folder = prompt(Prompt.choose_folder)
                pass
            case "3":
                folder = prompt(Prompt.choose_folder)
                pass
            case "4":
                folder = prompt(Prompt.choose_folder)
                IM.segmentation(folder)
            case "5":
                pass
            case "6":
                pass
            case "0":
                return 1
            case "-1":
                pass
            case _:
                print("Option invalide")


if __name__ == '__main__':
    main()
