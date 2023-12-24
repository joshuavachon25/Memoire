from InquirerPy import prompt
import utils.Prompt as Q
from utils.Settings import get_config
import subprocess
import time
import os

# Module-level variables to maintain state
config = get_config()
url = config["archives"]["Template"]
choice = 0
params = []
dezoomify_executable = os.path.join(os.getcwd(), "utils", "dezoomify-rs.exe")
p1 = 0
p2 = 0
folder = ""
output_path = ""


def menu():
    global choice, folder, params, p1, p2, output_path
    params = prompt(Q.dezoomify)
    p1 = int(params["start"])
    p2 = int(params["end"])
    if params["folder_name"] != "":
        output_path = params["folder_name"]
    output_path = os.path.join(os.getcwd(), "output", output_path)
    start()


def start():
    global output_path
    os.mkdir(os.path.join(os.getcwd(), "output", output_path))
    print("⚪ Début des téléchargements")
    for page in range(p1, p2 + 1):
        download(page)
    print("⚫ Fin des téléchargements")


def download(page):
    global url, output_path, dezoomify_executable
    page_str = str(page).rjust(4, "0")

    page_url = url.replace("||Page||", page_str)
    page_output_path = os.path.join(output_path, page_str + ".jpg")
    command = [dezoomify_executable, "-l", page_url, page_output_path]

    process = subprocess.run(command, capture_output=True, text=False)
    if process.returncode == 0:
        print(f"▪️ ✅ {page_str}.jpg créé avec succès")
    else:
        print(f"▪️ ❌ ERREUR: {process.stderr}")
