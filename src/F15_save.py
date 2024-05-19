import A_Functions
import os
import time
def tulis_csv (data,folder,file):
    f = open(folder + '/' + file, "w")
    f.write(data)
    f.close
def save(bigdata : dict):
    address = input('Masukkan nama folder: ')
    print()
    for i in range(4):
        print('Saving' + '.' * i, end='\r')
        time.sleep(0.5)
    if not os.path.isdir(address):
        os.mkdir(address)
        for i in range(4):
            print('Membuat folder data' + address + '.' * i, end='\r')
            time.sleep(0.5)
    # menyimpan data ke file
    tulis_csv((bigdata['user']),address,'user.csv')
    tulis_csv((bigdata['monster']),address,'monster.csv')
    tulis_csv((bigdata['monster_shop']),address,'monster_shop.csv')
    tulis_csv((bigdata['monster_inventory']),address,'monster_inventory.csv')
    tulis_csv((bigdata['item_shop']),address,'item_shop.csv')
    tulis_csv((bigdata['item_inventory']),address,'item_inventory.csv')
    print('\nData telah disimpan pada folder ' + address + '!')