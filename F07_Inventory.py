from A_Functions import *

def InventoryUser(user_id):
    data_monster = AmbilData("monster_inventory.csv")
    data_item = AmbilData("item_inventory.csv")
    inventory = []
    for i in range(1, len(data_monster)):
        if int(data_monster[i]['user_id']) == user_id:
            inventory.append(data_monster[i])
    
    for i in range(1, len(data_item)):
        if int(data_item[i]['user_id']) == user_id:
            inventory.append(data_item[i])
    return inventory

# masih banyak testing untuk jenis inventory supaya mudah utk dipanggil
def ShowInventory(user_id):
    inventory = (InventoryUserDict(user_id))
    data_monster = inventory['monster']
    data_item = inventory['item']
    counter = 1
    print(data_monster)

    inventory_2 = []
    for i in range(len(data_monster)):
        temp = ['monster']
        for values in inventory['monster'][i].values():
            if values != 'user_id':
                temp.append(values)
        inventory_2.append(temp)

    for i in range(len(data_item)):
        temp = ['item']
        for values in inventory['item'][i].values():
            if values != 'user_id':
                temp.append(values)
        inventory_2.append(temp)


    print(f"====== Inventory {user_id} ======")
    banyak_monster = len(inventory['monster'])
    for i in range(banyak_monster):
        print(counter, end=") ")
        for key, values in inventory['monster'][i].items():
            if key != 'user_id':
                print(key, ':', values, end=" ")
        print()
        counter += 1

    banyak_item = len(inventory['item'])
    for i in range(banyak_item):
        print(counter, end=") ")
        for key, values in inventory['item'][i].items():
            if key != 'user_id':
                print(key, ':', values, end=" ")
        print()
        counter += 1

    # checking to show detail item
    print("Ketikkan id untuk menampilkan item:")
    id = input(">>> ")

    while id != "KELUAR":
        DetailItem(int(id), inventory_2)
        print("Ketikkan id untuk menampilkan item:")
        id = input(">>> ")
    return

def DetailItem(item_id, inventory):
    # Mencari value dari tiap item/monster
    banyak_id = len(inventory)
    if item_id <= banyak_id:
        if inventory[item_id-1][0] == 'monster':
            print(inventory[item_id-1][1], inventory[item_id-1][2])
        elif inventory[item_id-1][0] == 'item':
            print(inventory[item_id-1][1], inventory[item_id-1][2])
    else:
        print("ID tidak tersedia")
    return

def InventoryUserDict(user_id: int) -> dict:
    data_monster: list = AmbilData("monster_inventory.csv")
    data_item: list = AmbilData("item_inventory.csv")
    inventory: dict = {'monster' : [], 'item' : [],}
    for i in range(1, len(data_monster)):
        if int(data_monster[i]['user_id']) == user_id:
            inventory['monster'].append(data_monster[i])
    
    for i in range(1, len(data_item)):
        if int(data_item[i]['user_id']) == user_id:
            inventory['item'].append(data_item[i])

    return inventory

print(ShowInventory(3))