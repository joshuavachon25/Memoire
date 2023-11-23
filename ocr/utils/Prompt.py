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
                Separator(),
                Choice(3, name="Améliorer les images"),
                Choice(4, name="Segmenter les images"),
                Choice(5, name="Océriser"),
                Choice(6, name="Nettoyer les données"),
                Choice(0, name="Quitter")
            ],
            "default": None,
        },
]

pages = [
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
