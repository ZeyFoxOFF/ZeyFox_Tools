import os
import subprocess
import socket
from portscan import PortScan
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
        "[1] : Supprimer les fichiers temporaires", 
        start_color=Color.magenta, 
        end_color=Color.yellow
    )
    gradient_print(
        "[2] : Vérifier les ports ouverts", 
        start_color=Color.magenta, 
        end_color=Color.yellow
    )
    choix = input("Sélectionner une option, ou Q pour quitter : ").strip().lower()
    if not choix:
        reponse = input("Rien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue

    if choix == "1":
        os.system("del /q /f /s %TEMP%\\*")
        print("Fichiers temporaires supprimés.")
        # C:\Users\Username\AppData\Local\Temp
    elif choix == "2":
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
                "[1] : Votre IP locale", 
                start_color=Color.magenta, 
                end_color=Color.yellow
                )
            gradient_print(
                "[2] : Entrer une adresse ip", 
                start_color=Color.magenta, 
                end_color=Color.yellow
            )
            choix = input("Sélectionner une option, ou Q pour quitter : ").strip().lower()

            if not choix:
                reponse = input("Rien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
                if reponse.lower() == "y":
                    subprocess.run(["python", "main.py"])
                    break
                else:
                    continue
            if choix == "1":
                def get_local_ip():
                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)
                    return local_ip
                
                ip = get_local_ip()
                port_range = '5555,37000-44000'
                scanner = PortScan(ip, port_range, thread_num=500, show_refused=False, wait_time=1, stop_after_count=True)
                
                open_port_discovered = scanner.run()  # <----- actual scan
                input("Appuyer sur une touche pour continuer...")
            elif choix == "2":       
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
                    choix_ip = input("Entrez une adresse ip (ex. 80.100.200.60) ou quitter avec Entrer : ").strip()
                    if choix_ip:
                        port_range = '5555,37000-44000'
                        scanner = PortScan(choix_ip, port_range, thread_num=500, show_refused=False, wait_time=1, stop_after_count=True)
                        
                        open_port_discovered = scanner.run()  # <----- actual scan
                        
                    else:
                        print("Aucune adresse ip n'a été saisie.")
                    input("Appuyer sur une touche pour continuer...")
            elif choix == "q":
                break
            else:
                print("Choix non valide. Sectionnez une option ou Q pour quitter.")

    elif choix == "q":
        subprocess.run(["python", "main.py"])
        break
    else:
        print("Choix non valide. Sectionnez une option ou Q pour quitter.")




