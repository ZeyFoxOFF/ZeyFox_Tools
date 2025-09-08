import requests
import subprocess
import time
from utils.utils import banner
while True:
    banner()
    adresse_mac = input("Enter a mac address (ex. 00:00:00:FF:FF:FF) or exit with Enter: ").strip()

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
    isfound = mac_info.get("found")


    if success:
        print("\033[32mValid MAC Address.\033[0m")
    else:
        print("\033[91mUnknown MAC Address.\033[0m")
        time.sleep(1)
        continue

    print(f"MAC Address: \033[95m{adresse_mac}\033[0m")
    if country:
        print(f"Country: \033[95m{country}\033[0m")
    if adresse:
        print(f"Address: \033[95m{adresse}\033[0m")
    if company:
        print(f"Company: \033[95m{company}\033[0m")
    if isfound == False:
        print(f"\033[38;5;214mMAC Address unknown\033[0m")
    input("Press a key to continue...")

