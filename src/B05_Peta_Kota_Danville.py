from src.A_Functions import *
from src.F00_RNG import *

# Fungsi untuk inisialisasi agen
def create_agent(name, position):
    return {"name": name, "position": position}

# Fungsi untuk inisialisasi peta
def create_map(map_data):
    agent = create_agent("Purry", (1, 1))  # Agen dimulai dari posisi (1, 1)
    return {"map_data": map_data, "agent": agent}

# Fungsi untuk mencetak peta
def print_map(map_data, agent_position):
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if (i, j) == agent_position:
                print('P', end=' ')  # Cetak 'P' jika posisi sama dengan posisi agen
            else:
                print(map_data[i][j], end=' ')  # Cetak karakter peta
        print()

# Fungsi untuk memindahkan agen
def move_agent(map_data, agent_position, direction):
    x, y = agent_position
    direction = direction.lower()
    # Periksa batasan peta dan rintangan sebelum memindahkan agen
    if direction == "w" and x > 0 and map_data[x - 1][y] not in ['*', 'X', 'L', 'A', 'S']:
        return x - 1, y
    elif direction == "s" and x < len(map_data) - 1 and map_data[x + 1][y] not in ['*', 'X', 'L', 'A', 'S']:
        return x + 1, y
    elif direction == "a" and y > 0 and map_data[x][y - 1] not in ['*', 'X', 'L', 'A', 'S']:
        return x, y - 1
    elif direction == "d" and y < len(map_data[0]) - 1 and map_data[x][y + 1] not in ['*', 'X', 'L', 'A', 'S']:
        return x, y + 1
    else:
        return agent_position

# Fungsi untuk memeriksa lokasi sekitar agen
def check_location(map_data, agent_position):
    x, y = agent_position
    places = {'S': 'Shop', 'A': 'Arena', 'L': 'Laboratorium', 'X': 'Semak', 'M': 'Minigame'}
    adjacent_places = []
    # Periksa lokasi sekitar agen untuk area khusus
    if y + 1 < len(map_data[0]) and map_data[x][y + 1] in places:
        adjacent_places.append(map_data[x][y + 1])
    if y - 1 >= 0 and map_data[x][y - 1] in places:
        adjacent_places.append(map_data[x][y - 1])
    if x + 1 < len(map_data) and map_data[x + 1][y] in places:
        adjacent_places.append(map_data[x + 1][y])
    if x - 1 >= 0 and map_data[x - 1][y] in places:
        adjacent_places.append(map_data[x - 1][y])

    if adjacent_places:
        print(f"Agen Purry akan mengakses {', '.join([places[place] for place in adjacent_places])}, karena berada pada posisi yang bersebelahan dengan {', '.join(adjacent_places)}")
        if places[adjacent_places[0]].upper() == 'SEMAK':
            if RNG(5) == 5:
                return places[adjacent_places[0]]
            else:
                return "nothing"
        else:
            return places[adjacent_places[0]]
    else:
        print("Agen Purry tidak berada di area khusus!")
        return "nothing"
# Fungsi utama untuk menjalankan permainan
def peta_kota_danville(agent_position: type = (1, 1)):
    # Membaca data peta
    map_string = """
************
*          *
*   S  X   *
*      X   *
*      X L *
* X  XXX   *
* X        *
* X        *
* XXX   A  *
*          *
* M  XXXXX *
************
"""
    map_data = [list(line) for line in ManualSplit(map_string, '\n') if line]

    while True:
        location = "nothing"
        # Cetak peta
        ClearScreen()
        print_map(map_data, agent_position)
        print()

        # Cetak posisi agen
        print(f"Agen Purry di posisi: {agent_position}")

        # Periksa apakah agen berada di area khusus
        location = check_location(map_data, agent_position)
        
        # Dapatkan input dari pengguna untuk navigasi
        direction = input("Mau ke arah mana? (W/S/A/D/STOP)\n>>> ")

        if direction.upper() == "INVENTORY":
            return "Inventory", agent_position
        if direction.upper() == "MONSTER":
            return "Monster", agent_position
        if location.upper() == 'SEMAK':
            return location, agent_position
        if location.upper() == direction.upper():
            return location, agent_position

        # Pindahkan agen
        if direction.upper() != "STOP":
            agent_position = move_agent(map_data, agent_position, direction)
        
        # Periksa apakah pengguna ingin mengakhiri permainan
        else:
            action = input("Mau melakukan apa? (HELP/LOGOUT) ")
            if action.upper() == "LOGOUT":
                return "Logout", agent_position
            elif action.upper() == "HELP":
                print("W: Ke atas (Utara)\nS: Ke bawah (Selatan)\nA: Ke kiri (Barat)\nD: Ke kanan (Timur)\nEND: Keluar dari permainan")
            else:
                print("Melanjutkan perjalanan.")

# Pengujian
# if __name__ == "__main__":
#     peta_kota_danville()
