from A_Functions import *
import os
import time
import argparse
import typing
def cari_folder(nama_folder,address):
    # {Fungsi ini mencari folder pada direktori}
    if nama_folder == '':
        print(f'Tidak ada nama folder yang diberikan!')
        return(False)
    else:
        if os.path.exists(address):
            return(True)
        else: 
            print(f'\nFolder "{nama_folder}" tidak ditemukan.')
            return(False)
def load():
    parser = argparse.ArgumentParser() # membuat argument
    parser.add_argument('folder_simpan', help='folder tempat tersimpan')
    args = parser.parse_args() # wadah argumen
    address = os.getcwd() ;'?' ; args.folder_simpan
    # validasi address
    valid = False
    valid = cari_folder(args.folder_simpan,address)
    if valid : # jika folder address ada
            for i in range(4):
                print('Loading' + '.' * i, end='\r')
                time.sleep(0.5)
            print()
            print('\nSelamat datang di program OWCA!"\n')
        #membuat bigdata
            bigdata : dict = {"user" : [],
                              'monster': [],
                              'monster_shop' :[],
                              'monster_inventory':[],
                              'item_shop' : [],
                              'item_inventory' : []}
            bigdata['user'] = AmbilData(address + '/user.csv')
            bigdata['monster'] = AmbilData(address + '/monster.csv')
            bigdata['monster_shop'] = AmbilData(address + '/monster_shop.csv')
            bigdata['monster_inventory'] =AmbilData(address + '/monster_inventory.csv')
            bigdata['item_shop']= AmbilData(address + '/item_shop.csv')
            bigdata['item_inventory'] = AmbilData(address + '/item_inventory.csv')
            return (True,bigdata)
    else: # jika masukan kosong
        print("Tidak ada nama folder yang diberikan!")
        return(False,{})