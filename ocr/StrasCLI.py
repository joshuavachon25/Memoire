from InquirerPy import prompt
import os
import cv2
from PIL import Image
import pytesseract
import utils.Messages as Messages
import utils.Cutter as Cutter
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
        os.system('cls')
        choice = prompt(Q.menu)
        match choice[0]:
            case 1:
                pages = prompt(Q.pages)
                FH.download(config["archives"], pages["start"], pages["end"])
            case 2:
                folder = prompt(Q.choose_folder)
                pass
            case 3:
                folder = prompt(Q.choose_folder)
                for filename in os.listdir(folder["src"]):
                    if filename.endswith((".png", ".jpg", ".jpeg")):
                        image_path = os.path.join(folder["src"], filename)
                        cropped_images = Cutter.draw_polygon_and_crop(image_path)
                        for idx, img in enumerate(cropped_images):
                            if not os.path.exists(os.path.join(os.getcwd(), folder["src"], "cropped")):
                                os.mkdir(os.path.join(os.getcwd(), folder["src"], "cropped"))
                            img.save(f"{folder['src']}/cropped/{filename.split('.')[0]}_{idx}.jpg")
            case 4:
                folder = prompt(Q.choose_folder)
                IM.enhance(folder, config)
            case 5:
                folder = prompt(Q.choose_folder)
                IM.segment(folder, config)
            case 6:
                pass
            case 7:
                pass
            case 0:
                return 1
            case _:
                print("Option invalide")


if __name__ == '__main__':
    main()
