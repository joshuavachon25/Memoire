import subprocess
import time
import os


def download(config, p1, p2):
    folder = str(int(time.time()))
    os.mkdir(os.path.join(os.getcwd(), "input", folder))
    print("⚪ Début des téléchargements")
    for p in range(int(p1), int(p2) + 1):
        dezoomify_path = os.path.join(os.getcwd(), "utils", "dezoomify-rs.exe")
        page = str(p).rjust(4, "0")

        url = config["Template"].replace("||Page||", page)
        output_path = os.path.join(os.getcwd(), "input", folder, page + ".jpg")
        command = [dezoomify_path, "-l", url, output_path]

        process = subprocess.run(command, capture_output=True, text=False)
        print(f"▪️ ✅ {page}.jpg créé avec succès") if process.returncode == 0 else print(f"▪️ ❌ ERREUR: {process.stderr}")
    print("⚫ Fin des téléchargements")
    print(f"Le dossier de sorti est /input/{folder}")
    return folder