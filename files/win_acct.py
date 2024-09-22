import os
import subprocess

while True:
    kms_key = input("Entrez une clé KMS ou quitter avec Entrer : ").strip()

    if not kms_key:
        reponse = input("Rien n'a été saisi. Voulez-vous quitter le programme ? (Y/N) : ")
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

if __name__ == "__main__":
    activator()

# By Arizaki

## Windows 10
# Windows 10 Pro : `W269N-WFGWX-YVC9B-4J6C9-T83GX`
# Windows 10 Home : `TX9XD-98N7V-6WMQ6-BX7FG-H8Q99`
# Windows 10 Pro N : `MH37W-N47XK-V7XM9-C7227-GCQG9`
# Windows 10 Home N : `3KHY7-WNT83-DGQKR-F7HPR-844BM`
# Windows 10 Education : `NW6C2-QMPVW-D7KKK-3GKT6-VCFB2`
# Windows 10 Enterprise : `NPPR9-FWDCX-D2C8J-H872K-2YT43`

### Windows 11
# Windows 11 Pro : `VK7JG-NPHTM-C97JM-9MPGT-3V66T`
# Windows 11 Home : `T96YJ-W9QGK-WBK44-2WQBR-BXJDY`
# Windows 11 Pro N : `9FNHH-K3HBT-3W4TD-6383H-6XYWF`
# Windows 11 Enterprise : `FPHH3-HNDR3-M8RMG-7DZFW-VV2TR`