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
        reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
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
        print("\033[32mValid MAC Address.\033[0m")
    else:
        print("\033[91mUnknown MAC Address.\033[0m")
        time.sleep(1)
        continue

    print(f"MAC Address: {adresse_mac}")
    if country:
        print(f"Country: {country}")
    if adresse:
        print(f"Address: {adresse}")
    if company:
        print(f"Company: {company}")
    if aleatoire:
        print(f"\033[38;5;214mGenerated MAC Address\033[0m")
    input("Press a key to continue...")

    if keyboard.is_pressed("enter"):
        break