import requests
import subprocess
import socket

while True:


    
    def get_public_ipv4():
        try:
            response = requests.get('https://api.ipify.org?format=json')
            data = response.json()
            return data['ip']
        except Exception as e:
            return str(e)
    print(f"Your public IPV4 address is: \033[32m{get_public_ipv4()}\033[0m")

    def get_public_ipv6():
        try:
            response = requests.get('https://api64.ipify.org/?format=json')
            data = response.json()
            return data['ip']
        except Exception as e:
            return str(e)
    adresse_ip = get_public_ipv6()
    print(f"Your public IPv6 address is: \033[32m{get_public_ipv6()}\033[0m")

    def get_local_ip():
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    local_ip = get_local_ip()
    print(f"Your local IP is: {local_ip}")



    geo_info2 = requests.get(f"https://ipinfo.io/{get_public_ipv4()}/json").json()
    geo_info = requests.get(f"http://ip-api.com/json/{get_public_ipv4()}?fields=query,status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse").json()

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

    # print(f"IP Address: {query}")
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
    if reverse_dns != "N/A":
        print(f"Hostname: {reverse_dns}")
    input("Press a key to continue...")

    subprocess.run(["python", "main.py"])
    break

