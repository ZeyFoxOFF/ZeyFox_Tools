import subprocess
from rgbprint import gradient_print, Color

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
    "\n \n \n[1] : Info Site Web\n[2] : Info Adresse IP\n[3] : Info Adresse MAC\n[4] : My IP\n[5] : Activer Windows\n[6] : Autres", 
    start_color=Color.yellow, 
    end_color=Color.magenta
)

while True:
    choix = input("Sélectionner une option, ou Q pour quitter : ").strip().lower()

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
        subprocess.run(["python", "files/win_acct.py"])
        break
    elif choix == "6":
        subprocess.run(["python", "files/others.py"])
        break
    elif choix == "q":
        break
    else:
        print("Choix non valide. Sectionnez une option ou Q pour quitter.")
