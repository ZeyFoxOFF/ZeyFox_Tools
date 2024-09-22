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

    gradient_print(
        "\n \n \n[1] : Website Information\n[2] : IP Address Information\n[3] : MAC Address Information\n[4] : My IP\n[5] : Info phone number\n[6] : Other Options", 
        start_color=Color.yellow, 
        end_color=Color.magenta
    )

    choix = input("Select an option, or Q to exit: ").strip().lower()
    if not choix:
        response = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
        if response.lower() == "y":
            exit()
        else:
            continue

    if choix == "1":
        subprocess.run(["python", "files/info_site.py"])
        break
    elif choix == "2":
        subprocess.run(["python", "files/info_ip.py"])
        break
    elif choix == "3":
        subprocess.run(["python", "files/info_mac.py"])
        break
    elif choix == "4":
        subprocess.run(["python", "files/my_ip.py"])
        break
    elif choix == "5":
        subprocess.run(["python", "files/info_num.py"])
        break
    elif choix == "6":
        subprocess.run(["python", "files/others.py"])
        break
    elif choix == "q":
        exit()
    else:
        print("Invalid choice.")
        time.sleep(1)
        continue