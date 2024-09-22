import requests
import keyboard
import subprocess
import time
from rgbprint import gradient_print, Color
while True:
    subprocess.run("cls", shell=True)

    gradient_print(
        r"""
            ███████╗███████╗██╗   ██╗███████╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
            ╚══███╔╝██╔════╝╚██╗ ██╔╝██╔════╝██╔═══██╗╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
              ███╔╝ █████╗   ╚████╔╝ █████╗  ██║   ██║ ╚███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
             ███╔╝  ██╔══╝    ╚██╔╝  ██╔══╝  ██║   ██║ ██╔██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
            ███████╗███████╗   ██║   ██║     ╚██████╔╝██╔╝ ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
            ╚══════╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                                                            V1.0
    """, 
        start_color=Color.yellow, 
        end_color=Color.magenta
    )
    adresse_mac = input("Entrez une adresse mac (ex. 00:00:00:FF:FF:FF) ou quitter avec Entrer : ").strip()

    if not adresse_mac:
        reponse = input("Rien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue


    mac_info = requests.get(f"https://api.maclookup.app/v2/macs/{adresse_mac}").json()

    # Extrait les données
    success = mac_info.get("success")
    adresse = mac_info.get("adresse")
    country = mac_info.get("country")
    company = mac_info.get("company")
    aleatoire = mac_info.get("isRand")


    if success:
        print("\033[32mAdresse MAC valide.\033[0m")
    else:
        print("\033[91mAdresse MAC inconnue.\033[0m")
        time.sleep(1)
        continue



    print(f"Adresse MAC : {adresse_mac}")
    if country:
        print(f"Pays : {country}")
    if adresse:
        print(f"Adresse : {adresse}")
    if company:
        print(f"Company : {company}")
    if aleatoire:
        print(f"\033[38;5;214mAdresse MAC genérer\033[0m")
    input("Appuyer sur une touche pour continuer...")

    if keyboard.is_pressed("enter"):
        break