from InquirerPy.validator import EmptyInputValidator, PathValidator
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

menu = [
        {
            "type": "list",
            "message": "Sélection d'une étape",
            "choices": [
                Choice(1, name="Télécharger une tuile"),
                Choice(2, name="Tester des paramètres"),
                Choice(3, name="Découpage de photos"),
                Separator(),
                Choice(4, name="Améliorer les images"),
                Choice(5, name="Segmenter les images"),
                Choice(6, name="Océriser"),
                Choice(7, name="Nettoyer les données"),
                Choice(0, name="Quitter")
            ],
            "default": None,
        },
]

dezoomify = [
    {
        "type": "number",
        "message": "Page de départ: ",
        "min_allowed": 0,
        "max_allowed": 100000,
        "validate": EmptyInputValidator(),
        "name": "start"
    },
    {
        "type": "number",
        "message": "Page de fin: ",
        "min_allowed": 0,
        "max_allowed": 100000,
        "validate": EmptyInputValidator(),
        "name": "end"
    },
    {
        "type": "input",
        "message": "Nom du dossier de sortie: ",
        "name": "folder_name"
    },
]

choose_folder = [
    {
        "type": "filepath",
        "message": "Choisissez le dossier contenant les images:",
        "validate": PathValidator(is_dir=True, message="Pas un dossier"),
        "name": "src",
        "only_directories": True,
    },
]

sandbox = [
    {
         "type": "list",
            "message": "Quel ensemble de paramères voulez-vous tester?",
            "choices": [
                Choice(1, name="Threshold"),
                Choice(2, name="Kernel"),
                Choice(3, name="Iterations"),
                Choice(4, name="Blur"),
                Choice(-1, name="Sortir"),
            ],
            "default": None,
    },
]

pretraitement = [
    {
         "type": "list",
            "message": "Quel ensemble de paramères voulez-vous tester?",
            "choices": [
                Choice(1, name="Découpage"),
                Choice(2, name="Enlever les bordures"),
                Choice(3, name="Binarisation"),
                Choice(4, name="Créer des box"),
                Choice(4, name="Extraire les box"),
                Choice(-1, name="Sortir"),
            ],
            "default": None,
    },
]

ocr = [
    {
         "type": "list",
            "message": "Que souhaitez-vous faire?",
            "choices": [
                Choice(1, name="Océriser"),
                Choice(-1, name="Sortir"),
            ],
            "default": None,
    },
]

encore = [
    {
         "type": "list",
            "message": "Voulez-vous utiliser encore Dezoomify?",
            "choices": [
                Choice(1, name="Oui"),
                Choice(-1, name="Non, retour au menu"),
            ],
            "default": None,
    },
]