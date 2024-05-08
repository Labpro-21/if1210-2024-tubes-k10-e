from F01_Register import *

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
