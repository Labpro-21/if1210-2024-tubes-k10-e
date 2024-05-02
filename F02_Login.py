# Memuat data pengguna dari CSV
def BerikanData():
    user_data = []
    with open("user.csv", "r", newline="") as csvfile:
        next(csvfile)  # Lewati baris header
        for line in csvfile:
            fields = []
            field = ""
            for char in line.strip():
                if char == ";":
                    fields.append(field)
                    field = ""
                else:
                    field += char
            fields.append(field)  # Menambahkan field terakhir
            user_data.append(fields)
    return user_data

# Fungsi untuk login
def login():
    print("Selamat datang di Sistem Login Pengguna!")
    usernamePengguna = input("Masukkan username : ")
    passwordPengguna = input("Masukkan password : ")

    matriks_user = BerikanData()

    check_username = False
    check_pw = False
    
    for user in matriks_user:
        if len(user) >= 3:  # Pastikan ada cukup banyak kolom dalam baris pengguna
            if usernamePengguna == user[1]:
                check_username = True
                if passwordPengguna == user[2]:
                    check_pw = True
                    break

    if not check_username:
        print("Username salah")
        return False
    elif not check_pw:
        print("Password salah")
        return False
    else:
        print("Login berhasil!")
        return True

# Testing
#if __name__ == "__main__":
#    login()
