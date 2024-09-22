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
            choix = input("Select an option, or Q to exit:").strip().lower()

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
                    choix_ip = input("Enter an ip address (ex.. 80.100.200.60) or exit with Enter: ").strip()
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

    elif choix == "q":
        subprocess.run(["python", "main.py"])
        break
    else:
        print("Invalid choice. Select an option or Q to exit.")




