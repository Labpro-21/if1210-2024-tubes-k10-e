from F02_Login import login, get_user_role

# Fungsi untuk menampilkan bantuan
def help():
    if login():
        username = input("Username: ")  # Hanya meminta username jika pengguna sudah login
        role = get_user_role(username)  # Mendapatkan peran pengguna berdasarkan username
    else:
        role = "belum login"  # Jika pengguna belum login, inisialisasi peran sebagai "belum login"

    # Menampilkan bantuan sesuai peran pengguna
    while True:
        if role == "belum login":
            print("=========== HELP ===========")
            print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
            print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
            print("2. Register: Membuat akun baru")
        else:
            print(f"=========== HELP ===========\nHalo {role} {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print("1. Logout: Keluar dari akun yang sedang digunakan")
            if role == "agent":
                print("2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
            elif role == "admin":
                print("2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        # Input dari player (Decision/Keputusan)
        decision = int(input())
        if decision == 1 and role == "belum login":
            print("Dialihkan ke login.py")
            break
        if decision == 2 and role == "belum login":
            print("Dialihkan ke register.py")
            break
        if (decision == 1 and role == "admin") or (decision == 1 and role == "agent"):
            print("Apakah ingin keluar? (y/n)")
            choice = input()
            if choice.lower() == "y":
                break
        if decision == 2 and role == "admin":
            print("Dialihkan ke shop.py")
            break
        if decision == 2 and role == "agent":
            print("Dialihkan ke monster.py")
            break


# Testing
#if __name__ == "__main__":
#    is_logged_in = login()  # Memanggil fungsi login untuk memeriksa apakah pengguna sedang login atau tidak
#    help(is_logged_in)  # Memanggil fungsi help dengan memberikan status login
