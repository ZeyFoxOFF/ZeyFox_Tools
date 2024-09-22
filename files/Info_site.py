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
    url = input("Enter the website link (e.g. https://example.com) or exit with Enter: ").strip()

    if not url:
        reponse = input("No link was entered. Do you want to leave the program? (Y/N): ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue

    site_web_http = url

    if not url.startswith("http://") and not url.startswith("https://"):
        print(f"The URL '{url}' is not valid because it does not start with 'http://' or 'https://'.")
        time.sleep(1)
        continue

    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"\033[32mThe website is online.\033[0m")
        elif response.status_code == 301:
            print(f"\033[32mThe website is online.\033[0m")
        elif response.status_code == 403:
            pass
        elif response.status_code == 404:
            print(f"\033[31mThe website does not exist.\033[0m")
        elif response.status_code == 405:
            pass
        elif response.status_code == 503:
            print(f"\033[31mThe website is offline (Service Unavailable).\033[0m")
        elif response.status_code == 504:
            print(f"\033[31mThe website is offline (Gateway Timeout).\033[0m")
        else:
            print(f"The website is offline. Status code: {response.status_code}")
    except requests.ConnectionError:
        print("\033[31mThe website does not exist.\033[0m")
        time.sleep(1)
        continue

    # Pour connaître l'IP
    domaine = url.split("//")[-1].split("/")[0]
    try:
        adresse_ip = socket.gethostbyname(domaine)
        print(f"IP: {adresse_ip}")
    except socket.gaierror:
        print(f"Unable to resolve {domaine} IP")

    # Connaitre le DNS
    try:
        info = whois.whois(site_web_http)
        if info.status:
            dns = info.name_servers[0] if info.name_servers else "DNS not available"
            print(f"DNS: {dns}")
        else:
            print(f"The website or domain '{site_web_http}' does not exist.")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error: Unable to connect to the website {site_web_http}")
    except socket.timeout:
        print("Timeout Error: The connection took too long to establish.")
    except Exception as e:
        print(f"An error occurred with the website '{site_web_http}': {e}")


    # Pour connaitre l'hébergeur
    try:
        info = whois.whois(site_web_http)
        if info.status:
            host = info.registrar if info.registrar else "Host not available"
            print(f"Host: {host}")
    except Exception as e:
        print(f"Unable to resolve host information for {site_web_http}")

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
        print(f"Country: {country}")
    if country_code != "N/A":
        print(f"Country Code: {country_code}")
    if region != "N/A":
        print(f"Region: {region}")
    if city != "N/A":
        print(f"City: {city}")
    if postal != "N/A":
        print(f"Postal Code: {postal}")
    if loc != "N/A":
        print(f"Location: {loc}")
        print(f"GPS Coordinates: \033[95m{google_maps_link}\033[0m")
    if timezone != "N/A":
        print(f"Timezone: {timezone}")
    if isp != "N/A":
        print(f"Internet Service Provider: {isp}")
    if organization != "N/A":
        print(f"Organization: {organization}")
    if as_number != "N/A":
        print(f"AS Number: {as_number}")
    if as_name != "N/A":
        print(f"AS Name: {as_name}")
    if reverse_dns != "N/A" and reverse_dns != "":
        print(f"Hostname: {reverse_dns}")
    input("Press a key to continue...")

    if keyboard.is_pressed("enter"):
        break
