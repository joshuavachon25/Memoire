from InquirerPy.validator import EmptyInputValidator, PathValidator
import os

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
