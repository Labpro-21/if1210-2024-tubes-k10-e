# KAMUS
# user.csv = [
#    ["id","username","password","role","oc"],
#    [1,"Mr_Monogram","monogrammer77","admin",0],
#    [2,"Asep_Spakbor","asepwow123","agent",9999],
#    [3,"Agen_P","platypus123","agent",0],
#    [4,"B4ngk1dd0ssss","bangkitganteng","agent",1337],
#    [5,"Kenny_agen_rahasia","kribogeming55","agent",6699]
# ]

# monster. csva = [
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

# Memuat data monster dari CSV
def BerikanMonster():
    monster_data = []
    with open("monster.csv", "r", newline="") as csvfile:
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
            monster_data.append(fields)
    return monster_data


# Fungsi untuk menyimpan data ke CSV
def SimpanData(data):
    with open("user.csv", "w") as csvfile:
        for row in data:
            # Konversi setiap elemen dalam row menjadi string sebelum digabungkan
            row_as_string = [str(item) for item in row]
            csvfile.write(";".join(row_as_string) + "\n")

# Fungsi untuk mengenkripsi kata sandi
def encrypt_password(password):
    encrypted_password = ""
    vowel_chars = 'aiueo'
    consonant_chars = 'bcdfghjklmnpqrstvwxyz'
    substitution_table = {'a': '@', 'i': '#', 'u': '$', 'e': '%', 'o': '&'}

    for char in password:
        if char.lower() in vowel_chars:
            encrypted_password += substitution_table.get(char.lower(), char.lower())
        elif char.lower() in consonant_chars:
            encrypted_password += consonant_chars[(consonant_chars.index(char.lower()) + 1) % len(consonant_chars)]
        else:
            encrypted_password += char

    return encrypted_password

# Fungsi untuk mendekripsi kata sandi
def decrypt_password(encrypted_password):
    decrypted_password = ""
    vowel_chars = 'aiueo'
    consonant_chars = 'bcdfghjklmnpqrstvwxyz'
    substitution_table = {'@': 'a', '#': 'i', '$': 'u', '%': 'e', '&': 'o'}

    for char in encrypted_password:
        if char.lower() in substitution_table:
            decrypted_password += substitution_table[char.lower()]
        elif char.lower() in consonant_chars:
            decrypted_password += consonant_chars[(consonant_chars.index(char.lower()) - 1) % len(consonant_chars)]
        else:
            decrypted_password += char

    return decrypted_password

# Registrasi
#registrasi
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
    usernamePendaftar = input("Masukkan username : ")
    passwordPendaftar = input("Masukkan password : ")
    PeriksaUsernameUnik(data, usernamePendaftar, passwordPendaftar, monster_data)
    
# Fungsi untuk memeriksa apakah username sudah terpakai
def PeriksaUsernameUnik(data, usernamePendaftar, passwordPendaftar, monster_data):
    for row in data[1:]:
        if len(row) >= 2 and usernamePendaftar == row[1]: # Kolom 1 untuk username
            print("Username", usernamePendaftar, "sudah terpakai! Silakan isi ulang form dengan username lain.")
            Registrasi(data, monster_data)
            return
    PeriksaKetentuanUsername(usernamePendaftar, passwordPendaftar, monster_data)

# Fungsi untuk memeriksa ketentuan username
def PeriksaKetentuanUsername(usernamePendaftar, passwordPendaftar, monster_data):
    # Memeriksa apakah username mengandung karakter yang diizinkan
    if all(char.isalnum() or char in '_-' for char in usernamePendaftar):
        TambahAkunBaru(usernamePendaftar, passwordPendaftar, monster_data)
    else:
        print("Username hanya dapat mengandung huruf alfabet (A-Za-z), underscore (_), strip (-), dan angka (0-9). Silakan isi ulang form dengan username yang sesuai.")
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
        pilihan = input("Monster Pilihanmu: ")
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
def TambahAkunBaru(usernamePendaftar, passwordPendaftar, monster_data):
    data.append([len(data), usernamePendaftar, passwordPendaftar, "agent", 0])  # Menambahkan role "agent" dan oc 0

    # Memilih monster
    monster_id = PilihMonster(monster_data)
    monster_type = monster_data[monster_id][1]
    monster_atk_power = monster_data[monster_id][2]
    monster_def_power = monster_data[monster_id][3]
    monster_hp = monster_data[monster_id][4]
    data[-1].extend([monster_id, monster_type, monster_atk_power, monster_def_power, monster_hp])

    SimpanData(data)
    print("Registrasi berhasil untuk username", usernamePendaftar, "dengan monster", monster_type)

# Testing (Untuk pengecekan)
#if __name__ == "__main__":
#  data = BerikanData()
#  monster_data = BerikanMonster()
#  Registrasi(data, monster_data)