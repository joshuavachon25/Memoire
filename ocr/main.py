import configparser
import scripts.FilesHelper as FH
import scripts.ImageManipulation as IM
import scripts.OCR as OCR
import scripts.DataCleaning as DC
import scripts.GeoTreatment as GT


def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read('data/env.ini')
    choice = "0"
    while choice != "-1":
        print("Choix disponibles:\n")
        print("\t1. Télécharger un fichier en tuile")
        print("\t2. Améliorer les images")
        print("\t3. Océriser")
        print("\t4. Nettoyer les données")
        choice = input("\nQuel option souhaitez-vous choisir?  ")
        match choice:
            case "1":
                page_start = input("\n\tA partir de quel page?  ")
                page_end = input("\n\tJusqu'a la page?  ")
                FH.download(config["source"], page_start, page_end)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "-1":
                pass
            case _:
                choice = "0"


if __name__ == '__main__':
    main()
