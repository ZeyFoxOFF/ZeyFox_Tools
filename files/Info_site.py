import requests
import socket
import whois
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
    url = input("Entrez le lien du site web (ex. https://example.com) ou quitter avec Entrer : ").strip()

    if not url:
        reponse = input("Aucun lien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue

    site_web_http = url

    if not url.startswith("http://") and not url.startswith("https://"):
        print(f"L'URL '{url}' n'est pas valide car elle ne commence ni par 'http://' ni par 'https://'.")
        time.sleep(1)
        continue

    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"\033[32mLe site est en ligne.\033[0m")
        elif response.status_code == 301:
            print(f"\033[32mLe site est en ligne.\033[0m")
        elif response.status_code == 403:
            pass
        elif response.status_code == 404:
            print(f"\033[31mLe site n'existe pas.\033[0m")
        elif response.status_code == 405:
            pass
        elif response.status_code == 503:
            print(f"\033[31mLe site est hors ligne (Service Unavailable).\033[0m")
        elif response.status_code == 504:
            print(f"\033[31mLe site est hors ligne (Gateway Timeout).\033[0m")
        else:
            print(f"Le site est hors ligne. Code de statut : {response.status_code}")
    except requests.ConnectionError:
        print("\033[31mLe site n'existe pas.\033[0m")
        time.sleep(1)
        continue

    # Pour connaître l'IP
    domaine = url.split("//")[-1].split("/")[0]
    try:
        adresse_ip = socket.gethostbyname(domaine)
        print(f"IP: {adresse_ip}")
    except socket.gaierror:
        print(f"Impossible de résoudre l'IP de {domaine}")

    # Connaitre le DNS
    try:
        info = whois.whois(site_web_http)
        if info.status:
            dns = info.name_servers[0] if info.name_servers else "DNS non disponible"
            print(f"DNS: {dns}")
        else:
            print(f"Le site ou le domaine '{site_web_http}' n'existe pas.")
    except requests.exceptions.ConnectionError:
        print(f"Erreur de connexion : Impossible de se connecter au site {site_web_http}")
    except socket.timeout:
        print("Erreur de délai d'attente : La connexion a pris trop de temps à s'établir.")
    except Exception as e:
        print(f"Une erreur s'est produite avec le site '{site_web_http}' : {e}")


    # Pour connaitre l'hébergeur
    try:
        info = whois.whois(site_web_http)
        if info.status:
            herbergeur = info.registrar if info.registrar else "Hébergeur non disponible"
            print(f"Hébergeur: {herbergeur}")
    except Exception as e:
        print(f"Impossible de résoudre les informations de l'hébergeur de {site_web_http}")

    geo_info2 = requests.get(f"https://ipinfo.io/{adresse_ip}/json").json()
    geo_info = requests.get(f"http://ip-api.com/json/{adresse_ip}?fields=query,status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse").json()

    query = geo_info.get("query", "N/A")
    status = geo_info.get("status", "N/A")
    country = geo_info.get("country", "N/A")
    country_code = geo_info.get("countryCode", "N/A")
    region = geo_info2.get("region", "N/A")
    city = geo_info.get("city", "N/A")
    postal = geo_info2.get("postal", "N/A")
    loc = geo_info2.get("loc", "N/A")
    google_maps_link = f"https://www.google.com/maps/place/{loc}"
    timezone = geo_info.get("timezone", "N/A")
    isp = geo_info.get("isp", "N/A")
    organization = geo_info.get("org", "N/A")
    as_number = geo_info.get("as", "N/A")
    as_name = geo_info.get("asname", "N/A")
    reverse_dns = geo_info.get("reverse", "N/A")

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
        print(f"Fournisseur de services Internet : {isp}")
    if organization != "N/A":
        print(f"Organisation : {organization}")
    if as_number != "N/A":
        print(f"Numéro AS : {as_number}")
    if as_name != "N/A":
        print(f"Nom de l'AS : {as_name}")
    if reverse_dns != "N/A" and reverse_dns != "":
        print(f"Nom d'hôte : {reverse_dns}")
    input("Appuyer sur une touche pour continuer...")

    if keyboard.is_pressed("enter"):
        break
