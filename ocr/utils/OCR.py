from InquirerPy import prompt
import utils.Prompt as Q
from utils.Settings import get_config

# Module-level variables
reset = get_config()
config = reset
choice = 0


def menu():
    global choice, config, reset
    while choice != -1:
        folder = prompt(Q.choose_folder)
        choice = prompt(Q.ocr)
        if choice[0] == 1:
            print(1)
