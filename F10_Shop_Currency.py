def display_items(agent, item_type):
    """
    Menampilkan item yang tersedia untuk dibeli.

    Parameters:
        agent (dict): Data agen yang berisi monster, potion, OC, dan inventory.
        item_type (str): Tipe item yang akan ditampilkan, "monster" atau "potion".
    """
    if item_type == "monster":
        print("ID | Type | ATK Power | DEF Power | HP | Stok | Harga")
        for monster in agent['monsters']:
            print(f"{monster['id']} | {monster['type']} | {monster['atk_power']} | {monster['def_power']} | {monster['hp']} | {monster['stock']} | {monster['price']}")
    elif item_type == "potion":
        print("ID | Type | Stok | Harga")
        for potion in agent['potions']:
            print(f"{potion['id']} | {potion['type']} | {potion['stock']} | {potion['price']}")

def buy_item(agent, item_type, item_id, quantity=1):
    """
    Membeli sebuah item.

    Parameters:
        agent (dict): Data agen yang berisi monster, potion, OC, dan inventory.
        item_type (str): Tipe item yang akan dibeli, "monster" atau "potion".
        item_id (int): ID dari item yang akan dibeli.
        quantity (int, optional): Jumlah item yang akan dibeli. Defaultnya 1.
    """
    if item_type == "monster":
        # Cari monster yang sesuai dengan item_id
        monster = next((m for m in agent['monsters'] if m['id'] == item_id), None)
        # Jika monster ditemukan, cek apakah jumlah item yang tersedia lebih dari 0
        # dan OC agen cukup
        if monster and monster['stock'] > 0 and agent['oc'] >= monster['price']:
            # Jika benar, kurangi OC agen dan stok monster
            agent['oc'] -= monster['price']
            monster['stock'] -= 1
            # Tambahkan monster yang dibeli ke inventory agen
            agent['inventory'].append(monster)
            print(f"Berhasil membeli monster {monster['type']} dengan ID {monster['id']}. Monster sudah masuk ke inventorymu!")
        else:
            # Jika salah, berikan pesan error
            if not monster:
                print(f"Monster dengan ID {item_id} tidak ditemukan.")
            elif monster['stock'] <= 0:
                print(f"Monster {monster['type']} dengan ID {monster['id']} tidak tersedia.")
            else:
                print(f"OC-mu tidak cukup untuk membeli monster {monster['type']} dengan ID {monster['id']}.")

    elif item_type == "potion":
        # Cari potion yang sesuai dengan item_id
        potion = next((p for p in agent['potions'] if p['id'] == item_id), None)
        # Jika potion ditemukan, cek apakah jumlah item yang tersedia cukup
        # dan OC agen mencukupi
        if potion and potion['stock'] >= quantity and agent['oc'] >= potion['price'] * quantity:
            # Jika benar, kurangi OC agen dan stok potion
            agent['oc'] -= potion['price'] * quantity
            potion['stock'] -= quantity
            # Tambahkan potion yang dibeli ke inventory agen
            agent['inventory'].extend([potion] * quantity)
            print(f"Berhasil membeli {quantity} {potion['type']} dengan ID {potion['id']}. Potions sudah masuk ke inventorymu!")
        else:
            # Jika salah, berikan pesan error/
            if not potion:
                print(f"Potion dengan ID {item_id} tidak ditemukan.")
            elif potion['stock'] < quantity:
                print(f"Stok potion {potion['type']} dengan ID {potion['id']} tidak mencukupi.")
            else:
                print(f"OC-mu tidak cukup untuk membeli {quantity} {potion['type']} dengan ID {potion['id']}.")

def main():
    """
    Fungsi utama untuk menjalankan sistem tampilan dan pembelian item.
    """
    agent = {
        'monsters': [
            {
                'id': 1,
                'type': 'Charizard',
                'atk_power': 100,
                'def_power': 80,
                'hp': 150,
                'stock': 3,
                'price': 100000
            },
            {
                'id': 2,
                'type': 'Pikachu',
                'atk_power': 70,
                'def_power': 60,
                'hp': 100,
                'stock': 5,
                'price': 50000
            },
            {
                'id': 3,
                'type': 'Balbu',
                'atk_power': 60,
                'def_power': 50,
                'hp': 80,
                'stock': 4,
                'price': 30000
            },
            {
                'id': 4,
                'type': 'Wilbu',
                'atk_power': 50,
                'def_power': 40,
                'hp': 60,
                'stock': 6,
                'price': 20000
            }
        ],
        'potions': [
            {
                'id': 1,
                'type': 'Strength Potion',
                'stock': 5,
                'price': 30
            },
            {
                'id': 2,
                'type': 'Resilience Potion',
                'stock': 8,
                'price': 50
            }
        ],
        'oc': 1000000,
        'inventory': []
    }

    while True:
        action = input(">>> Pilih aksi (lihat/beli/keluar): ")
        if action not in ["lihat", "beli", "keluar"]:
            print("Input salah! Masukkan yang benar!")
        elif action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ")
            if item_type not in ["monster", "potion"]:
                print("Input salah! Masukkan yang benar!")
            else:
                display_items(agent, item_type)
        elif action == "beli":
            item_type = input(">>> Mau beli apa? (monster/potion): ")
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {agent['oc']}")
            if item_type not in ["monster", "potion"]:
                print("Input salah! Masukkan yang benar!")
            else:
                item_id = int(input(f"Masukkan id {item_type}: "))
                if item_type == "potion":
                    quantity = int(input(">>> Masukkan jumlah: "))
                    buy_item(agent, item_type, item_id, quantity)
                else:
                    buy_item(agent, item_type, item_id)
        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break

if __name__ == "__main__":
    main()
