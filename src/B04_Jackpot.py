from src.F00_RNG import *
from src.A_Functions import *
import time

def PlayJackpot():
    print("""

        ░▀▀█░█▀█░█▀▀░█░█░█▀█░█▀█░▀█▀
        ░░░█░█▀█░█░░░█▀▄░█▀▀░█░█░░█░
        ░▀▀░░▀░▀░▀▀▀░▀░▀░▀░░░▀▀▀░░▀░
    =========== DAFTAR ITEM ============
    1. Topi: 50 OC
    2. Pedang: 100 OC
    3. Koin: 200 OC
    4. Potion: 300 OC
    5. Monster: 500 OC 
    """)
    
    choice = "Y"
    while choice == ("Y"):
        choice = input("Mulai bermain (Y/N): ").upper()
        if choice == "Y":
            Jackpot()
        elif choice == "N":
            return

def Jackpot():
    jackpot_item = {
        'topi'   : 50,
        'pedang' : 100,
        'koin'   : 200,
        'potion' : 300,
        'monster': 500,
    }

    ClearScreen()
    item_1 = PickItem()
    
    print("---------------------------------------")
    print(f"---- {item_1} |         |         -----")
    print("---------------------------------------")

    time.sleep(RNG(2))
    ClearScreen()
    item_2 = PickItem()
    print("---------------------------------------")
    print(f"---- {item_1} | {item_2} |        -----")
    print("---------------------------------------")

    time.sleep(RNG(2))
    ClearScreen()
    item_3 = PickItem()
    
    print("---------------------------------------")
    print(f"---- {item_1} | {item_2} |  {item_3} -----")
    print("---------------------------------------")
    
    if item_1 == item_2 == item_3:
        print("you get pokemon")
    else:
        oc = jackpot_item[item_1] + jackpot_item[item_2] + jackpot_item[item_3]
        print(oc)
        return oc

def PickItem():
    item = RNG(5)
    if item == 1:
        return "topi"
    elif item == 2:
        return "pedang"
    elif item == 3:
        return "koin"
    elif item == 4:
        return "potion"
    elif item == 5:
        return "monster"

PlayJackpot()