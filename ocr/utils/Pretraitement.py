from InquirerPy import prompt
import utils.Prompt as Q
from Settings import get_config

class Pretraitement:
    def __init__(self):
        self.config = get_config()
        self.choice = 0
        self.menu()

    def menu(self):
        while self.choice != -1:
            folder = prompt(Q.choose_folder)
            choice = prompt(Q.pretraitement)
            match choice[0]:
                case 1:
                    print(1)
