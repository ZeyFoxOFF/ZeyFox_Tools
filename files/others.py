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
        "[1] : Delete temporary files", 
        start_color=Color.magenta, 
        end_color=Color.yellow
    )
    gradient_print(
        "[2] : Check open ports", 
        start_color=Color.magenta, 
        end_color=Color.yellow
    )
    gradient_print(
        "[3] : Activate Windows", 
        start_color=Color.magenta, 
        end_color=Color.yellow
    )
    choix = input("Select an option, or Q to exit:").strip().lower()
    if not choix:
        reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
        if reponse.lower() == "y":
            subprocess.run(["python", "main.py"])
            break
        else:
            continue

    if choix == "1":
        os.system("del /q /f /s %TEMP%\\*")
        print("Temporary files deleted.")
        input("Press a key to continue...")
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
                "[1] : Your local IP", 
                start_color=Color.magenta, 
                end_color=Color.yellow
                )
            gradient_print(
                "[2] : Enter an IP address", 
                start_color=Color.magenta, 
                end_color=Color.yellow
            )
            choix = input("Select an option, or Q to exit: ").strip().lower()

            if not choix:
                reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
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
                port_range = '1-65535'
                scanner = PortScan(ip, port_range, thread_num=10000, show_refused=False, wait_time=0.5, stop_after_count=True)
                
                open_port_discovered = scanner.run()  # <----- actual scan
                if not open_port_discovered:
                    print("No open port was found.")
                input("Press a key to continue...")
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
                    choix_ip = input("Enter an ip address (ex. 80.100.200.60) or exit with Enter: ").strip()
                    if choix_ip:
                        port_range = '1-65535'
                        scanner = PortScan(choix_ip, port_range, thread_num=10000, show_refused=False, wait_time=1, stop_after_count=True)
                        
                        open_port_discovered = scanner.run()  # <----- actual scan
                        if not open_port_discovered:
                            print("No open port was found.")
                    else:
                        print("No ip address was entered.")
                    input("Press a key to continue...")
            elif choix == 3:
                while True:
                    kms_key = input("Enter a KMS key or exit with Enter: ").strip()

                    if not kms_key:
                        reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
                        if reponse.lower() == "y":
                            subprocess.run(["python", "main.py"])
                            break
                        else:
                            continue

                def activator():
                    os.system(f'slmgr /ipk {kms_key}')

                    # Configurer l'adresse du serveur KMS
                    os.system('slmgr /skms kms.digiboy.ir')

                    # Activer Windows
                    os.system('slmgr /ato')

                    # By Arizaki

                    # Windows 10:
                    # Windows 10 Pro : `W269N-WFGWX-YVC9B-4J6C9-T83GX`
                    # Windows 10 Home : `TX9XD-98N7V-6WMQ6-BX7FG-H8Q99`
                    # Windows 10 Pro N : `MH37W-N47XK-V7XM9-C7227-GCQG9`
                    # Windows 10 Home N : `3KHY7-WNT83-DGQKR-F7HPR-844BM`
                    # Windows 10 Education : `NW6C2-QMPVW-D7KKK-3GKT6-VCFB2`
                    # Windows 10 Enterprise : `NPPR9-FWDCX-D2C8J-H872K-2YT43`

                    # Windows 11:
                    # Windows 11 Pro : `VK7JG-NPHTM-C97JM-9MPGT-3V66T`
                    # Windows 11 Home : `T96YJ-W9QGK-WBK44-2WQBR-BXJDY`
                    # Windows 11 Pro N : `9FNHH-K3HBT-3W4TD-6383H-6XYWF`
                    # Windows 11 Enterprise : `FPHH3-HNDR3-M8RMG-7DZFW-VV2TR`
                    activator()
            elif choix == "q":
                break
            else:
                print("Invalid choice. Select an option or Q to exit.")

    elif choix == "q":
        subprocess.run(["python", "main.py"])
        break
    else:
        print("Invalid choice. Select an option or Q to exit.")




