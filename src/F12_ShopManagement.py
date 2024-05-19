from src.A_Functions import *
from src.F10_Shop_Currency import *

def ShopManagement(bigdata):
    while True:
    
        action = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar)\n>>> ")
        if action == 'lihat':
            item_type = input("monster / potion: ")
            DisplayItems(bigdata, item_type)
        elif action == 'tambah':
            available_id = []
            item_type = input("monster / potion: ")
            if item_type == 'monster':
                for i in range(len(bigdata['monster_shop'][1:])):
                    available_id.append(bigdata['monster_shop'][i+1]['monster_id'])

                print("ID | Type           | ATK Power | DEF Power | HP   ")
                print("====================================================")
                for monster in bigdata['monster'][1:]:
                    # Displaying unavailable monster
                    if monster['id'] not in available_id:
                        print(f"{monster['id']:>2} | {monster['type']:<14} | {monster['atk_power']:>9} | {monster['def_power']:>9} | {monster['hp']:>4}")
                monster_id = int(input("Masukkan id monster: "))
                if monster_id in available_id:
                    print("ID telah ada di shop")
                else:
                    monster_stock = int(input("Masukkan stock awal: "))
                    monster_price = int(input("Masukkan harga: "))
                    add_monster = {
                        'monster_id'    : monster_id,
                        'stock'         : monster_stock,
                        'price'         : monster_price
                    }
                    bigdata['monster_shop'].append(add_monster)
            elif item_type == 'potion':
                # PEER
                # PEER
                # PEER
                continue
        elif action =='ubah':
            item_type = input("monster / potion:")
            if item_type == 'monster':
                DisplayItems(bigdata, item_type)
                monster_id = int(input("id: "))
                monster_stock = int(input("stock: "))
                monster_price = int(input("price: "))
                bigdata['monster_shop'][monster_id]['stock'] = monster_stock
                bigdata['monster_shop'][monster_id]['price'] = monster_price
            elif item_type == 'potion':
                DisplayItems(bigdata, item_type)
                item_id = int(input("id: "))
                item_stock = int(input("stock: "))
                item_price = int(input("price: "))
                bigdata['item_shop'][item_id]['stock'] = item_stock
                bigdata['item_shop'][item_id]['price'] = item_price
        elif action == 'hapus':
            item_type = input("monster / potion:")
            DisplayItems(bigdata, item_type)
            if item_type == 'monster':
                monster_id = int(input("id: "))
                delete_monster = next((monster for monster in bigdata['monster_shop'] if monster['monster_id'] == monster_id), None)
                if delete_monster:
                    confirmation = input(f"apakah anda yakin ingin menghapus: ")
                    if confirmation == 'y':
                        bigdata['monster_shop'] = [monster for monster in bigdata['monster_shop'] if monster != delete_monster]
                elif not delete_monster:
                    print("Tidak ada id")
                continue
            elif item_type == 'potion':
                item_id = int(input("id: "))
                bigdata['item_shop'][item_id]['stock'] = 0
        elif action == 'keluar':
            return
