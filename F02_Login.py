from F01_Register import BerikanData

# Fungsi untuk mendapatkan role
def get_user_role(username):
    # Memuat data pengguna dari file CSV
    user_data = BerikanData("user.csv")

    # Mencari peran pengguna berdasarkan username
    for user in user_data:
        if len(user) >= 4:  # Pastikan ada cukup banyak kolom dalam baris pengguna
            if username == user[1]:
                return user[3]  # Mengembalikan peran pengguna

    # Jika username tidak ditemukan, kembalikan None
    return None

# Fungsi untuk login
def login():
    print("Selamat datang di Sistem Login Pengguna!")
    usernamePengguna = input("Masukkan username : ")
    passwordPengguna = input("Masukkan password : ")

    matriks_user = BerikanData("user.csv")

    check_username = False
    check_pw = False
    
    for user in matriks_user:
        if len(user) >= 3:  # Pastikan ada cukup banyak kolom dalam baris data yang diberikan
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
