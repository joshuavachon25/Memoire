import os
import utils.Dezoomify as Dezoomify
import utils.Sandbox as Sandbox
import utils.Pretraitement as Pretraitement
import utils.Cutter as Cutter
import utils.Prompt as Q
import utils.OCR as OCR
import utils.DataCleaning as DataCleaning
import utils.GeoTreatment as Geo
from InquirerPy import prompt
# https://github.com/UB-Mannheim/tesseract/wiki


def main():
    actions = {
        1: Dezoomify.menu,
        2: Sandbox.menu,
        3: Cutter.menu,
        4: Pretraitement.menu,
        5: lambda: None,  # Placeholder for future functionality
        6: OCR.menu,
        7: DataCleaning.menu,
        8: Geo.menu
    }

    while True:
        os.system('cls')
        choice = prompt(Q.menu)[0]

        if choice == 0:
            return 1
        elif choice in actions:
            actions[choice]()
        else:
            print("Option invalide")


if __name__ == '__main__':
    main()
