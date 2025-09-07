import subprocess
import re
import time
from rgbprint import gradient_print, Color
import winreg as wrg
from utils.utils import banner
while True:
    banner()
    
    gradient_print(
        "\n \n \n[1] : Change Drag Selection Color", 
        start_color=Color.magenta, 
        end_color=Color.yellow
            )
    
    choix = input("Select an option, or Q to exit: ").strip().lower()
    if not choix:
        response = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
        if response.lower() == "y":
            exit()
        else:
            continue
    elif choix == "q":
        subprocess.run(["python", "files/others.py"])
        break



    
    if choix == "1":
        while True:
            banner()

            def check_input(value: str) -> bool:
                pattern = r"^\d{1,3} \d{1,3} \d{1,3}$"
                if not re.match(pattern, value):
                    return False
                parts = value.split()
                return all(0 <= int(p) <= 255 for p in parts)

            
            color_rbg = input("Enter an rgb color (ex. 255 0 128) or enter \"default\" to reset the color or exit with Enter: ")
            if not color_rbg:
                reponse = input("Nothing was entered. Do you want to leave the program? (Y/N): ")
                if reponse.lower() == "y":
                    subprocess.run(["python", "files/windows_settings.py"])
                    break
                else:
                    continue
            elif color_rbg == "default":
                location = wrg.HKEY_CURRENT_USER
                soft = wrg.OpenKeyEx(location, r"Control Panel\\Color", 0, wrg.KEY_SET_VALUE)
                wrg.SetValueEx(soft, "Hilight", 0, wrg.REG_SZ, "0 120 212")
                wrg.SetValueEx(soft, "HotTrackingColor", 0, wrg.REG_SZ, "0 102 204")
                wrg.CloseKey(soft)
                print(f"Colors set to default")
                input("Press a key to continue...")
                subprocess.run(["python", "files/windows_settings.py"])
                break
            elif not check_input(color_rbg):
                print("Invalid format. Please enter like: 000 000 000 (numbers 0-255 only).")
                time.sleep(1)
                continue
            else:
                location = wrg.HKEY_CURRENT_USER
                soft = wrg.OpenKeyEx(location, r"Control Panel\\Colors", 0, wrg.KEY_SET_VALUE)
                wrg.SetValueEx(soft, "Hilight", 0, wrg.REG_SZ, color_rbg)
                wrg.SetValueEx(soft, "HotTrackingColor", 0, wrg.REG_SZ, color_rbg)
                wrg.CloseKey(soft)
                print(f"Colors set to {color_rbg}")
                input("Press a key to continue...")
                subprocess.run(["python", "files/windows_settings.py"])
                break


