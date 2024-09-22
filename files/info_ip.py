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
    adresse_ip = input("Entrez une adresse ip (ex. 80.100.200.60) ou quitter avec Entrer : ").strip()

    if not adresse_ip:
        reponse = input("Rien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue


    geo_info2 = requests.get(f"https://ipinfo.io/{adresse_ip}/json").json()
    geo_info = requests.get(f"http://ip-api.com/json/{adresse_ip}?fields=query,status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse").json()

    # Extrait les données
    query = geo_info.get("query", "N/A")
    status = geo_info.get("status", "N/A")
    country = geo_info.get("country", "N/A")
    country_code = geo_info.get("countryCode", "N/A")
    region = geo_info2.get("region", "N/A")
    city = geo_info2.get("city", "N/A")
    postal = geo_info2.get("postal", "N/A")
    loc = geo_info2.get("loc", "N/A")
    google_maps_link = f"https://www.google.com/maps/place/{loc}"
    timezone = geo_info2.get("timezone", "N/A")
    isp = geo_info.get("isp", "N/A")
    organization = geo_info.get("org", "N/A")
    as_number = geo_info.get("as", "N/A")
    as_name = geo_info.get("asname", "N/A")
    reverse_dns = geo_info.get("reverse", "N/A")


    if status == "success":
        print("\033[32mAdresse IP valide.\033[0m")
    elif status == "fail":
        print("\033[91mAdresse IP inconnu.\033[0m")
        time.sleep(1)
        continue


    print(f"Adresse IP : {query}")
    # print(f"Statut de la requête : \033[32m{status}\033[0m")
    if country != "N/A":
        print(f"Pays : {country}")
    if country_code != "N/A":
        print(f"Code du pays : {country_code}")
    if region != "N/A":
        print(f"Région : {region}")
    if city != "N/A":
        print(f"Ville : {city}")
    if postal != "N/A":
        print(f"Code postal : {postal}")
    if loc != "N/A":
        print(f"Localisation : {loc}")
        print(f"Coordonnée gps : \033[95m{google_maps_link}\033[0m")
    if timezone != "N/A":
        print(f"Fuseau horaire : {timezone}")
    if isp != "N/A":
        print(f"Fournisseur d'accès a internet : {isp}")
    if organization != "N/A" and organization != "":
        print(f"Organisation : {organization}")
    if as_number != "N/A":
        print(f"Numéro AS : {as_number}")
    if as_name != "N/A":
        print(f"Nom de l'AS : {as_name}")
    if reverse_dns != "N/A" and reverse_dns != "":
        print(f"Nom d'hôte : {reverse_dns}")


    if keyboard.is_pressed("enter"):
        break