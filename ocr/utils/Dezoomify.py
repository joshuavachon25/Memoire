from InquirerPy import prompt
import utils.Prompt as Q
from Settings import get_config
import subprocess
import time
import os


class Dezoomify:
    def __init__(self):
        self.config = get_config()
        self.url = self.config["archives"]["Template"]
        self.choice = 0
        self.params = []
        self.dezoomify = os.path.join(os.getcwd(), "utils", "dezoomify-rs.exe")
        self.p1 = 0
        self.p2 = 0
        self.folder = prompt(Q.choose_folder)
        self.output_path = str(int(time.time()))
        self.menu()

    def menu(self):
        while int(self.choice[0]) != -1:
            self.params = prompt(Q.dezoomify)
            self.p1 = int(self.params["start"])
            self.p2 = int(self.params["end"])
            if self.params["folder_name"] != "":
                self.output_path = self.params["folder_name"]
            self.output_path = os.path.join(os.getcwd(), "output", self.output_path)
            self.start()
            self.choice = prompt(Q.encore)

    def start(self):
        os.mkdir(os.path.join(os.getcwd(), "output", self.output_path))
        print("⚪ Début des téléchargements")
        for page in range(self.p1, self.p2 + 1):
            self.download(page)
        print("⚫ Fin des téléchargements")

    def download(self, page):
        page = str(page).rjust(4, "0")

        url = self.url.replace("||Page||", page)
        output_path = os.path.join(self.output_path, page + ".jpg")
        command = [self.dezoomify, "-l", url, output_path]

        process = subprocess.run(command, capture_output=True, text=False)
        print(f"▪️ ✅ {page}.jpg créé avec succès") if process.returncode == 0 else print(
            f"▪️ ❌ ERREUR: {process.stderr}")