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
    adresse_ip = input("Enter an ip address (ex.. 80.100.200.60) or exit with Enter: ").strip()

    if not adresse_ip:
        reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
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
        print("\033[32mValid IP Address.\033[0m")
    elif status == "fail":
        print("\033[91mUnknown IP Address.\033[0m")
        time.sleep(1)
        continue

    print(f"IP Address: {query}")
    # print(f"Request Status: \033[32m{status}\033[0m")
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
    if organization != "N/A" and organization != "":
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