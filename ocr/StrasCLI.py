import configparser
import os
import cv2
from PIL import Image
import pytesseract
import utils.FilesHelper as FH
import utils.ImageManipulation as IM
import utils.OCR as OCR
import utils.DataCleaning as DC
import utils.GeoTreatment as GT

#https://github.com/UB-Mannheim/tesseract/wiki

def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read('data/env.ini')
    choice = "0"
    folder = ""
    while choice != "-1":
        print("Choix disponibles:")
        print("\t1. Télécharger un fichier en tuile")
        print("\t2. Segmenter les images")
        print("\t3. Améliorer les images")
        print("\t4. Océriser")
        print("\t5. Nettoyer les données")
        print("\t6. Quitter")
        choice = input("Quel option souhaitez-vous choisir?  ")
        match choice:
            case "1":
                page_start = input("\tA partir de quel page?  ")
                page_end = input("\tJusqu'a la page?  ")
                folder = FH.download(config["source"], page_start, page_end)
            case "2":
                tmp_response = ""
                if folder != "":
                    while tmp_response.lower() != "y" or tmp_response.lower() != "n":
                        tmp_response = input(f"\tVoulez-vous utiliser {folder}? (Y/N) ")
                        if tmp_response.lower() == "n":
                            folder = tmp_response
                if folder == "":
                    while tmp_response != 42:
                        tmp_response = input("Quel dossier souhaitez-vous utiliser? ./input/")
                        if os.path.isdir("./input/" + tmp_response):
                            folder = tmp_response
                            tmp_response = 42
                IM.segmentation(folder)
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                return 1
            case "-1":
                pass
            case _:
                choice = "0"


if __name__ == '__main__':
    main()
