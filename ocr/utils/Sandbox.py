from InquirerPy import prompt
import utils.Prompt as Q
from Settings import get_config


class Sandbox:
    def __init__(self, config):
        self.reset = get_config()
        self.config = self.reset
        self.choice = 0
        self.menu()

    def menu(self):
        while self.choice != -1:
            folder = prompt(Q.choose_folder)
            choice = prompt(Q.sandbox)
            match choice[0]:
                case 1:
                    print(1)
