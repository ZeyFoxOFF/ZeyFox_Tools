import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import subprocess
import time
from utils.utils import banner
while True:
    banner()

    phone_number = input("Enter a phone number (ex. +33623456789) or exit with Enter: ").replace(" ", "")

    if not phone_number:
        response = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
        if response.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue

    try:
        if not phone_number.startswith("+"):
            phone_number = "+" + phone_number

        parsed_number = phonenumbers.parse(phone_number, None)

        if phonenumbers.is_valid_number(parsed_number):
            country_code = phone_number[1:3]
            operator = carrier.name_for_number(parsed_number, "en")
            number_type = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else "Unknown"
            country = phonenumbers.region_code_for_number(parsed_number)
            region = geocoder.description_for_number(parsed_number, "en")
            status = "Valid"

            if not region:
                region = "Unknown"
            if not timezone_info:
                timezone_info = "Unknown"
            if not country:
                country = "Unknown"
            if not country_code:
                country_code = "Unknown"
            if not operator:
                operator = "Unknown"
            if not number_type:
                number_type = "Unknown"

            print(f"""Phone : \033[95m{phone_number}\033[0m
Country Code : \033[95m+{country_code}\033[0m
Country : \033[95m{country}\033[0m
Region : \033[95m{region}\033[0m
Timezone : \033[95m{timezone_info}\033[0m
Operator : \033[95m{operator}\033[0m
Number Type : \033[95m{number_type}\033[0m
            """)

    except Exception as e:
        print(f"\033[91mUnknown phone number.\033[0m")
        time.sleep(1)
        continue

    input("Press a key to continue...")
