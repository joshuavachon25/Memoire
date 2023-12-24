from InquirerPy import prompt
import utils.Prompt as Q
from utils.Settings import get_config

config = get_config()
choice = 0


def menu():
    global choice
    while choice != -1:
        folder = prompt(Q.choose_folder)
        choice = prompt(Q.pretraitement)
        match choice[0]:
            case 1:
                print(1)
