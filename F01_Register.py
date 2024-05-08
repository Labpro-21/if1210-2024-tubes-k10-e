# KAMUS
# user.csv = [
#    ["id","username","password","role","oc"],
#    [1,"Mr_Monogram","monogrammer77","admin",0],
#    [2,"Asep_Spakbor","asepwow123","agent",9999],
#    [3,"Agen_P","platypus123","agent",0],
#    [4,"B4ngk1dd0ssss","bangkitganteng","agent",1337],
#    [5,"Kenny_agen_rahasia","kribogeming55","agent",6699]
# ]

# monster. csv = [
#    ["id", "type", "atk_power", "def_power", "hp"],
#    [1, "Pikachow", 125, 10, 600],
#    [2, "Bulbu", 50, 50, 1200],
#    [3, "Zeze", 300, 10, 100],
#    [4, "Zuko", 100, 25, 800],
#    [5, "Chacha", 80, 30, 700]
#]


# UNTUK MEMEPERMUDAH AKSES
# 0 = id
# 1 = username
# 2 = password
# 3 = role
# 4 = oc

def BerikanData(informasi):
    data = []
    with open(informasi, "r", newline="") as csvfile:
        next(csvfile)  # Lewati baris header
        line = ""  # String kosong untuk menyimpan setiap baris
        char = csvfile.read(1)  # Baca karakter pertama dari file
        while char:  # Loop sampai karakter terakhir terbaca
            if char == "\n":  # Jika karakter adalah newline
                fields = []  # Inisialisasi list untuk menyimpan data tiap baris
                field = ""  # String kosong untuk menyimpan setiap field
                for c in line:
                    if c == "\r":  # Lewati karakter "\r"
                        continue
                    elif c == ";":
                        fields.append(field)
                        field = ""
                    else:
                        field += c
                if field:  # Jika masih ada field yang belum ditambahkan
                    fields.append(field)
                data.append(fields)  # Menambahkan data ke list utama
                line = ""  # Reset string line
            else:
                line += char  # Tambahkan karakter ke string line
            char = csvfile.read(1)  # Baca karakter selanjutnya dari file
    return data

# Fungsi untuk menyimpan data ke CSV dengan menambahkan satu kolom dari belakang setiap kali dapat data baru
def SimpanData(data):
    # Tulis data yang sudah diperbarui ke file CSV
    with open("user.csv", "w") as csvfile:
        for row in data:
            # Konversi setiap elemen dalam list menjadi string
            row = [str(item) for item in row]
            csvfile.write(";".join(row) + "\n")




# Registrasi
def Registrasi(data, monster_data):
    print()
    print(

"""
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗██████╗  █████╗ ███████╗██╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   ██████╔╝███████║███████╗██║
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══██╗██╔══██║╚════██║██║
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ██║  ██║██║  ██║███████║██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
"""

)
    print('{:^80s}'.format("="*80))
    print()
    while True:
        usernamePendaftar = input("Masukkan username : ")
        passwordPendaftar = input("Masukkan password : ")
        if PeriksaUsernameUnik(data, usernamePendaftar) == False:
            # Memeriksa ketentuan username
            print("Username", usernamePendaftar, "sudah terpakai! Silakan isi ulang form dengan username lain.")
            print()
        else:
            PeriksaKPassword(usernamePendaftar, passwordPendaftar, monster_data, data)
            break

# Fungsi untuk memeriksa apakah username sudah terpakai
def PeriksaUsernameUnik(data, usernamePendaftar):
    for row in data:
        if len(row) >= 2 and usernamePendaftar == row[1]: # Kolom 1 untuk username
            return False  # Tandai bahwa username tidak unik
    return True  # Tandai bahwa username unik


# Fungsi untuk memeriksa ketentuan username
def PeriksaKUsername(usernamePendaftar, passwordPendaftar, monster_data, data):
    # Memeriksa apakah username mengandung karakter yang diizinkan
    if all(char.isalnum() or char in '_-' for char in usernamePendaftar):
        # Menambahkan akun baru
        TambahAkunBaru(usernamePendaftar, passwordPendaftar, monster_data, data)
    else:
        print("Username hanya dapat mengandung huruf alfabet (A-Za-z), underscore (_), strip (-), dan angka (0-9). Silakan isi ulang form dengan username yang sesuai.")
        Registrasi(data, monster_data)

# Fungsi untuk memeriksa ketentuan password
def PeriksaKPassword(usernamePendaftar, passwordPendaftar, monster_data, data):
    # Memeriksa apakah password memiliki panjang minimal 8 karakter
    if len(passwordPendaftar) >= 8:
        # Memeriksa apakah password mengandung setidaknya satu huruf besar, satu huruf kecil, dan satu angka
        if any(char.isupper() for char in passwordPendaftar) and any(char.islower() for char in passwordPendaftar) and any(char.isdigit() for char in passwordPendaftar):
            # Memeriksa apakah password tidak mengandung username
            if usernamePendaftar not in passwordPendaftar:
                # Memeriksa apakah password mengandung karakter yang diizinkan
                if all(char.isalnum() or char in '_-' for char in passwordPendaftar):
                    # Memeriksa apakah password tidak berisi spasi
                    if ' ' not in passwordPendaftar:
                        # Menjalankan fungsi untuk memeriksa username
                        PeriksaKUsername(usernamePendaftar, passwordPendaftar, monster_data, data)
                    else:
                        print("Password tidak boleh mengandung spasi. Silakan isi ulang form dengan password yang sesuai.")
                        Registrasi(data, monster_data)
                else:
                    print("Password hanya dapat mengandung huruf alfabet (A-Za-z), underscore (_), strip (-), dan angka (0-9). Silakan isi ulang form dengan password yang sesuai.")
                    Registrasi(data, monster_data)
            else:
                print("Password tidak boleh mengandung username. Silakan isi ulang form dengan password yang sesuai.")
                Registrasi(data, monster_data)
        else:
            print("Password harus terdiri dari setidaknya satu huruf besar (A-Z), satu huruf kecil (a-z), dan satu angka (0-9). Silakan isi ulang form dengan password yang sesuai.")
            Registrasi(data, monster_data)
    else:
        print("Password harus memiliki panjang minimal 8 karakter. Silakan isi ulang form dengan password yang sesuai.")
        Registrasi(data, monster_data)


# Fungsi untuk memilih monster
def PilihMonster(monster_data):
    while True:
        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
        print("1. Pikachow")
        print("2. Bulbu")
        print("3. Zeze")
        print("4. Zuko")
        print("5. Chacha")
        pilihan = ""
        while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
          pilihan = input("Monster Pilihanmu: ")
          if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
            print("Ulangi Input!") 
        b = int(pilihan)
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(monster_data) - 1:
          monster_id = int(pilihan)
          monster_type = monster_data[monster_id][1]
          monster_atk_power = monster_data[monster_id][2]
          monster_def_power = monster_data[monster_id][3]
          monster_hp = monster_data[monster_id][4]
          if b == 1:
            print("""

                @@
               @@@@
              @@@@@
             @@@@@@
            @@@...@                                                       @.@
            @.....@                                      @@@            @....
           @......@                           @@.@@@@@@@@@@@         @.......@
           .......@                      @.......@@@@@@@@@         @..........
           .......                   @..........@@@@@@@@         @............@
          @......@ @@@@@@        @@............@@@@@@          @...............
           ....................@..............@@@@           @.................
           ..................................@              ...................@
         @............@..@@............@@                 @....................@
        .@@...........@@@@@..........                   @.......................
       .@@@...........................                @......................@
      .@@@.............................              .....................@
     @@....@@@@@@@@@............@......@            ...................@
     @........@@@@@@......@.....@.......@           @...............@
      @.@......@@@.@...........@.........@           @...........@
       @.@......@.........................            @.......@
        @..................................            @....@
          @.....................@..@@.......            @...@
       @@.......................@.....@......         @......@
 @@@...........................@.............@@     @........@
@..............................................@  @.......@
@................................................  @....@
 .@...............................................@  @.@.@
            @@@@..................................@@   @@@@@
                @...................................@@@@@@@.@
                @....................................@@@@
                 ....................................@@@
                 ......................................@.@
                 @....................................
                 @....................................
                  ...................................@
                   @.................................
                     @........@         @@..........@
                         ....@                 @....@
                         @@..@                  @@.@.
                           @.                     @.@

""")
          if b == 2:
              print("""

                                                              #:
                                                            .=-=@.===@
                                                           .#=-==%-=+.
                                      ...=@@@@@@@@%@@@@#=====--=---=@+++.
                                   .@----------=-===========-@----==+++.
                                .%--------===-==-===-@==--=------==+++@
                              :+====---===----@--------=====-----==@++@
           .....             @++===--------=@==-------==--===-=====%+++.
          *------@.    .. ...+++==-===-=--@@:-@--===----==-==----==++++@
         =------@-::::-------------+@@:--::---=@-====-=--===----==++++++@
        @----:::-:::::------------------------==-====-====----===+++*+++=@.
       :----:::::::::::@+++++++---------------==%=--=====-====+++++++@++==#.
       @@--:::::::-+++++++*-----------------============+++++++++++++++=+#
      ------:----@+++++*++@-------------------===%+++++++++++++++++++++++++=@.
     @----:--------#+++#----------------------===*+++++++++++++++++++++@====+@
    @--@-----*+------------------------------======++++++++++++++++++++++=====.
   #-=:@@----%+--------------------@:*@-----=====%=+++++++++++++++++++++=+++@
  .-:.%+#------------#+------:---@:.+++**@--======@===@+++++++++++++++++++++++=.
  @@ .++.-=--------++-----#---@. %++..==============@++++++++++++++++++++++.
 .-  =+.---------@+++@--------@  .++  -===========+++++++++++++++++++++.
 %-  %:.------------#%-------+.  .*  ++==========+**+@++++++++++++++++#
.--. .++:---------------------@   ..+++%===========#*+@+++++++++++++@
.----@+@---------------------%    @++++++++=============*=@+++++++++++.
.==---------------------------@@...%@===================+**%==@+++++++@.
 @==@==----:---------------------------====@=================+%#======++++#@
  .@====@===----------------------====#%===============================#%=
     .@===#+#+@@@=**###@@@@@#+++++++@%=========@========================%
       ..+===@++=============++++=============-------=======%----=======
          *=%====@===========%@==========+%==-----------====%----@+=======
          %----+@===================#@++++=------------===+*--@++++-======#
          @------======++%@%++++++++++++=----++------===@-%+++++*@======%
          .---@+++=====++++++++++++++++++---=--++#----===@---+++@======.
           %@==++++=======%==++++++++++%===+---------====----@+**#======%
           .+==++++==========.@+==++++++===+%--------===@=======@%========@
            #++++===========.    =++++@+++++--------===%+=================:
             @---==========       #++++++++@------====-  @===============@
              @==========@.       .@.@-+@+------====+.   .+=============%.
             --+::==.@===            @-------======@       @:==#@======@.
              ..   ....             .::-@.===.@==..        .. .+@+.+@.
                                        .#. .@

""")
          if b == 3:
            print("""

                                       =
                                     @---
                                    @-----
                                   @----==-
                                  @-=====--=
                                  ===.---==+@
                                 =+++++++++++
                                @++++++++++++=
                                ++++++++++++++@        @+=#
                  ---==@   @=++++++++++++++++++++%@=======
                  @--=++++@+++++++++++++++++++++====*=++=@
                   @+++++++++++++++++++++++++====%*++=++@
                    @++++++====@+=++++++==#=====+@
                     @++========++++==@**+++++@====
                      ==========+@++++++++++++++++=@@==
                      ========%@@@++++++++++++@@@@@====@
                      =========+++#@@@%#####@%=++++=====        *
                     @+======+++++++++++++++++++++======      @++@
          @@         @++++++++++++++++++++===++++++=====    @++++@
          @+++++@    @++++++++++++++++++++++++++++++====* @+++++=@
           ++++++++++@+++++++++++++++++++++++++++++++++++++++++++
           @++=++++++++++++++++++++++++++++++++++++++++++@++++++#
            @+++++++++++++++++++++++++++++++++++++++++++++++++++
              +++++++++++++++++++++++++++++++++++++++++++++++++@
               ++++++++++++++++++++++++++++++++++++++++++++@++@
                @++++++++++++++++++++++++++++++++++++++++++++
                  @++++++++++++++++++++++++++++++++++++++++++
                  +++++++++++++++++++++++++++++++++++++++++++*
                 #*+++++++++++++++++++++++++++++++++++++++#
                @######+++++++++++++++++++++++++++++++*#####
               @#########+++++++++++++++++++++++++############*@
              @###########++++++++++++++++++++++################*
             ###############+++++++###########################@
            ###################################################*@
          #####################################################*
        @*###################################################**@
       *#############################################@**#@
       #*##########################################*
                  @*########################**@
                  @*####@ ###*#@  @@**#
                  @*%     **@
                   *%@          ***@
                                      @*@
                                         @**@

""")
          if b == 4:
           print("""

                    ;x+++++++x;
                 :;;;++:.  .:;++x;
               :;;;;            ;x+
              :+;;+++++++xxx     ;X
           +::+X+:.        :+XX  :X
         ;;:: ;::::            ;X+
        ;;;;  ;;;;;           ;++;::;
        ;+++   ;;;++        :++;;:::::
        ;+++;   ++++x;    :+x+++;;;;;x
        .+++x;   :++xxX:+++;;+XX+$+++;.
          +xxxX     +XXx+;;;::+:+;;:.:
           ;XXXX::.::+++;;;:.
           ..+XXxX:::xx++;:+x+x:.    ..
       :.......xxx+++xx++;;:;x;+;;; .:::....
      ;..........:+++++Xx++;;++;;+;::+::::.  .
   :............  :::++;;;;x+;;;x:;;;+:;::..   .
  :..................  xXX;:;+++;+++++;+;x:.....
  ....:..............  .  $XX+;x++x+;;;::;++
   .::::.::..........     .XXXX++xxX;;::::.++       .
 :::.:.::::............     :. .x+X;;;::::.:.+        .              .;;+++;:
:;;;:::::::::.........  .   .   .:;;......... :                   .::;;;;;
:;;;;::.:::::......... .... .  ....+:.....           ..         .;;::::
;;;;;;::::::::.::..........   ......x..                        ;;;;::
 :;;;;;;;:::;::::::........      +  ..     ;::;;     ...      ++;;;
   +:;;;;;;;;;;;::............. ;; +:.   :;X;+.       ...    +++++          +
   ;;;;;;;;;;;;;;::::........;+:;;x+:.  .++++xx   .. ...   :++++;        .X:
   ;;;;;;;;;;;;;;::......:::..+++++++. .+x+x;  . ....:.   x+++;         XX.
   :;;;;;;;;;;;;;:::::.:.......:++xxX...+X$..:......:. ;x++++:+X+.     xX+
     ;:;;;;;;;;;;;;;:..:::::..:::..+x+:..+..::::..::::xxxx+x+;       .xx;
      +;;;;;;;;;;;;:::::;:;:::::::::...::..:::;;::::;xXxx++;         xx++
       :;;;;;;;;+;;:+;;;;:;;;;;;;;::..:::::::::;;:;Xx++;+:          x+++
        .;;;;;;;++++;++;;;;;;;;;;;::::;;::;::::X$;;;;;;;+++++++xXXx++++;
          .:;;;;+++;+++++++;;;;;++++;++;x;;;;;;::;:+XX           .xXXx+
               ;:;;+;;+++++;;;;+;;X++++;;;::::+X;::+            :+++++:
                   +:;;;:;X+;;;;;X++++;;:+X+::::+. ++++++xxxxxXXX++++.
                    XX +XXXX;+;;;++XXx++;;;+;.+++++++++:     :XX+xX+
                    :XX. ;xxx++++;+++;;::;;;;;;;++:        ;;;;+++ +;
                     ;XXX   ;;++;;;;:::::;;;;+:         ;;;;;;;;.    :
                      .xxxx;       :::.             :;;;;;;::+       .
                        ;++++++;.            .:;;:::::::;:;.
                          .;++++++++;;;;;;;;;;::::::::;:
                               .+;++;;;;;;;;:::;;:

""")
          if b == 5:
            print("""



                              =
                            **#@@#
                      #*    ### @######@                   *#
               #*#      ###########=###               **
            =*@%%%%@@        *########%                   ###%
         @@%%%%%%%%@%@           %#####                  ##@@@@#=
        %%%%%%%%%%@%%%@           *#####                #@@%@%%%%#
       %%%%%%%%%%%@%%%%%           *####               #%%%%@@%%%%@:
      %%%%%%%%%%%%@@%%%%*          %####             #@@%%%@%%%%%%%
     %%%%%%%%%%%%%%%%%%%%@#%        *###@           #@@%%%@@@@%%%%%%%%
    @%%%%%%%%%%%%%%@%%%%%%@@@@##%    **##       ###@@@%%%%@@@@%%%%%%%%@
    #@%%%%%       %%@%%%%%%%@@@@@@###.*#@####@@@@@@@@%%%@@@@@  @%%%%%%@
    #@@%%          %@%%%@   -++#=*####@@@@@@@@@%%%@@@    ++ *%%@@#
     #@@            %     %@#*=#######%*  .%%@     -*    @@*
      @              @  =*     @@@=#@@      %*.  @      =-...   @@
      %                #%@     *: .:::#       %*%:       .::.:   @
                         #  %    **:   ::::::#      % @#        .:..-    %
                                @=::   :::::::@                 .:..
                                **@::::::::::::::+                 .....
                               *::::::::::::::::                   @+
                  ##########@*%::::::::::::::=##               =%
               -#####@####@==##::::::::::::::#*#=          ##-
              #############=###:::::::::::::%*    %###::
             %####################:::::::::::::####**#######:::%
              ########%::#######:::::::*:%-:::::::%######:::
               #:::::::::#######::@                ######
                  ::+-  @*@###%#                   ########
                         .+.#- *                      :. ..



""")
          print("Anda memilih monster dengan detail sebagai berikut:")
          print("Type:", monster_type)
          print("ATK Power:", monster_atk_power)
          print("DEF Power:", monster_def_power)
          print("HP:", monster_hp)
          a = input("Kamu yakin memilih monster ini? (y/n) ")
          if a == "y":
            return int(pilihan)
          else:
            print("Silakan pilih lagi!")
        else:
            print("ID monster tidak valid. Silakan pilih lagi!")


# Fungsi untuk menambahkan akun baru ke dalam data
def TambahAkunBaru(usernamePendaftar, passwordPendaftar, monster_data, data):
    # Menemukan ID terakhir dan menambahkannya satu angka di atasnya
    id_akhir = data[-1]
    last_id = int(data[-1][0])
    new_id = last_id + 1

    # Menambahkan data baru ke dalam list
    data.append([new_id, usernamePendaftar, passwordPendaftar, "agent", 0])  # Menambahkan role "agent" dan oc 0

    # Memilih monster
    monster_id = PilihMonster(monster_data)
    monster_type = monster_data[monster_id][1]

    # Menampilkan informasi registrasi
    print("Registrasi berhasil untuk username", usernamePendaftar, "dengan monster", monster_type)

    # Menyimpan perubahan ke file CSV
    SimpanData(data)


# Testing (Untuk pengecekan)
#if __name__ == "__main__":
#  data = BerikanData("user.csv")
#  monster_data = BerikanData("monster.csv")
#  Registrasi(data, monster_data)
