from src.F00_RNG import *

monster_ascii = {
    'Pikachow'  : """
          =.                                 
         +%-                                 
        :#+:                                 
        :-=:                                 
        --+...::..::--::::-.                 
        :-=--------=---=+#**=                
        :-------==+-    .                    
        .=#*-----*===:----          ..::.    
        :===-*###--##----     .::-------     
    .=--=#=--=**+--==-=-   :-=---------      
     :-=--==---+=----=-    +++++++==--:      
        .--=---==------.   ++:..             
           :-----++=---- +=++                
           :------+==+++#%-                  
           -------=+++==.                    
           :---====:.                        
            -++=-.                           
            .==                              
             -                                

    """,

    'Bulbu'     :"""
                                 .-==-.      
                   ...::-:::::--========     
                 .::-=====---::::-====*=     
       :::.     .:-====--:-----======+*+.    
      :::-:..:----::::..:::==========+*++.   
    ..::::-=++++=-:::::::::-=========++*++.  
    .:::---===-:::::::::::::++======++++*++  
   .:+-:+-::--::::::=+*=::::-=++++++++++*++= 
  . +-=::::=+-:::::.*+.*=:::-:-=+*++++++*+++ 
  ..*:=::::::::::: .*=.**-::::=+++**++**++++ 
 :-:==-:::::::::::  +*+++-:::::=++++=++++++. 
  --=:-:::-:::::::::::--::::::::====-:=++-   
   .:=**+===++++***+=+=::::::::::::::::-.    
      :-========+++=-::---:::::--:----:::    
        :--------------:::-:::::---+++::::   
        -+=::---:::::::.--+-:::--:++++--::   
       ::+=::::::.:---:++:::::--:::==--::.   
        :-::::::   :-:=+=:::::..:::::::::    
        .::-::.     .:::::::.   .:-:::::     
                      .....                  
    """,

    'Zeze'      :"""
                               
                 7i                
               iUiLu               
               QuYJM:              
        si:  :X51j1UZ..i7P.        
        iQMgEdSuJ1JjjEdXBY         
         :MjvrSP12I122B2I          
          K7rYBBggZRBBQXv          
     .    ELsLUSdqKI5uriq  rB.     
     BZUiiP2U1YY7L7vvuJYJIIEB.     
     :BZQQSsjJ1j11ujjJ1j1ZEMd      
      :BZPUJJujusuJuj1122Igd       
        5SII51IIS5K5XSKS5jg.       
        BgXUuSSK5SISII1uJ2bB.      
       QBBBZ2suYU25ssJEQBBBBBr     
     .BBRRRBQbSPgBQQgQQBQQMQQBQ.   
   .RBBBBRQQBBBBQRQBBQBQQMRBBBBBS  
   SBBBgQBQBBBBBRRgQQBBBBBBBB ..   
        jBBBBgrBBQgDBB:rU5XPu      
         v.     .uXbP   
                    
    """,

    'Zuko'      : """
                                          
                .          .       
               BqBBBQvSKEBB7       
               BJP vBIr.           
             7v:j2j  1EXddv        
             BZiRDR:    ..         
             i:uQQL                
               .BBg         .: .   
  :....:. r.   :uuB.    i.. ..  u  
  J.  .   .  7.MuSQ5 r  .       v7 
 .v.         : vv :              r 
  U:.:                       .  :J 
  :17u:.                    .rLP1. 
    .r22Ui::.5SM    sBRZ i::KSui   
        71uJqBBBB.::sBBBXPJJ:      
             iPBIIvsv2jX7          
                 BBBBB             
                XBBBBBB            
              vb217v7:B2           
                                   
    """,

    'Chacha'    : """
                                        
             rj7iv:                
      .i7uI  .XqqIdj7:     ::      
    :qMgDB5     .1U7        Bq.    
  .BQP5sKgR.     iUu       BBBBu   
  BQEZbX5bSDr    .7X:     BQZRjbD2 
 BBr.  sQgZQBBBJ.:i7u :UBQB7DBgUSB:
jB.     dB:.JBQEL7:rvPQBBBI5BM uEQP
ri       . .. :P7:..:sP  . 2M  L sB
         :U7: :7.    :L  77s   r. Q
            .i7.     .r.  .   :.i..
       iJ5v:iir.    :::K:      i.. 
     rKUIKS.::Ui::::..ir7r    Yr   
    :BqXSPvi7Xviirr77ISr:rIqbP:    
     :IIu2JuPr:::..:7sjIKKd:       
         ..i              .        
    """,


}

text_ascii = {
    'battle'    : None,
    'login'     : 
"""
██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
""",

    'register'  : 
"""
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗██████╗  █████╗ ███████╗██╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   ██████╔╝███████║███████╗██║
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══██╗██╔══██║╚════██║██║
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ██║  ██║██║  ██║███████║██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
"""
    ,

    'logout'    : 
"""
██╗      ██████╗  ██████╗  ██████╗ ██╗   ██╗████████╗██╗
██║     ██╔═══██╗██╔════╝ ██╔═══██╗██║   ██║╚══██╔══╝██║
██║     ██║   ██║██║  ███╗██║   ██║██║   ██║   ██║   ██║
██║     ██║   ██║██║   ██║██║   ██║██║   ██║   ██║   ╚═╝
███████╗╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝   ██║   ██╗
╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚═╝
""",

    'vs'        : 
"""
                       
                        
                        
                        
                        
                        
                        
                        
   █████ █████  █████   
  ░░███ ░░███  ███░░    
   ░███  ░███ ░░█████   
   ░░███ ███   ░░░░███  
    ░░█████    ██████   
     ░░░░░    ░░░░░░    
                            
                            
                            
                            
                            
                            
                            
                            
""",

    'welcome':
    """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗      ████████╗ ██████╗  
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝      ╚══██╔══╝██╔═══██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗           ██║   ██║   ██║   
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝           ██║   ██║   ██║   
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗         ██║   ╚██████╔╝  
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝         ╚═╝    ╚═════╝  
                                                                
 ██████╗ ██╗    ██╗ ██████╗ █████╗ 
██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║   ██║██║ █╗ ██║██║     ███████║
██║   ██║██║███╗██║██║     ██╔══██║
╚██████╔╝╚███╔███╔╝╚██████╗██║  ██║
 ╚═════╝  ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝
   
   """,
   
    'shop'  :
"""
░█▀▀░█░█░█▀█░█▀█
░▀▀█░█▀█░█░█░█▀▀
░▀▀▀░▀░▀░▀▀▀░▀░░
""",

    'battle' :
"""
░█▀▄░█▀█░▀█▀░▀█▀░█░░░█▀▀
░█▀▄░█▀█░░█░░░█░░█░░░█▀▀
░▀▀░░▀░▀░░▀░░░▀░░▀▀▀░▀▀▀
""",

    'arena' :
"""
░█▀█░█▀▄░█▀▀░█▀█░█▀█
░█▀█░█▀▄░█▀▀░█░█░█▀█
░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀
""",

    'minigame':
"""
░█▄█░▀█▀░█▀█░▀█▀░█▀▀░█▀█░█▄█░█▀▀
░█░█░░█░░█░█░░█░░█░█░█▀█░█░█░█▀▀
░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀
""",

    'jackpot':
"""
░▀▀█░█▀█░█▀▀░█░█░█▀█░█▀█░▀█▀
░░░█░█▀█░█░░░█▀▄░█▀▀░█░█░░█░
░▀▀░░▀░▀░▀▀▀░▀░▀░▀░░░▀▀▀░░▀░""",

    'hangman':
"""
░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█
░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█
░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀"""

}

grass_ascii ={
    1   : """
     /\^     /\        /\          /\ 
  _./  \/\_./  \_^/\/\/  \_/\_/\^^/  \._
""",

    2   :"""
        /\     /\      /\     /\ 
  _._/\/  \_/\/  \_/-^-  \_/\/  \_./\__
""",

    3   :"""
""",
}

def PrintTerrain(type: str):
    if type == "grass":
        print(grass_ascii[RNG(len(grass_ascii))])
    return


hangman_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

hangman_words = [
    "buku", "meja", "kursi", "lampu", "pintu", "jendela", "rumah", "kamar",
    "dapur", "taman", "mobil", "sepeda", "motor", "jalan", "jalanan", "toko",
    "pasar", "sekolah", "kantor", "gedung", "apartemen", "hotel", "penginapan",
    "wisata", "pantai", "gunung", "hutan", "sungai", "danau", "laut", "samudra",
    "pulau", "negara", "kota", "desa", "kampung", "perpustakaan", "museum",
    "teater", "bioskop", "restoran", "kafe", "warung", "makanan", "minuman",
    "buah", "sayur", "daging", "ikan", "roti", "kue", "permen", "es krim",
    "teh", "kopi", "susu", "air", "jus", "soda", "olahraga", "sepakbola",
    "basket", "tenis", "bulutangkis", "renang", "lari", "bersepeda", "senam",
    "yoga", "buku", "majalah", "koran", "novel", "komik", "cerita", "puisi",
    "dongeng", "cerpen", "drama", "musik", "lagu", "instrumen", "piano",
    "gitar", "biola", "drum", "suling", "saxofon", "orkestra", "band",
    "kesenian", "tari", "lukis", "gambar", "fotografi", "film", "video",
    "teater", "drama", "komedi", "tragedi", "aksi", "petualangan", "fiksi",
    "ilmiah", "romantis", "horor", "misteri", "thriller", "fantasi",
    "sejarah", "biografi", "otobiografi", "perjalanan", "pesawat", "kereta",
    "bis", "kapal", "kereta api", "helikopter", "bandara", "stasiun", "terminal",
    "pelabuhan", "tiket", "koper", "paspor", "visa", "bagasi", "penginapan",
    "kamar hotel", "wisatawan", "turis", "panduan", "peta", "petualangan",
    "ekspedisi", "pengalaman", "cerita", "kenangan", "suvenir", "cendera mata",
    "belanja", "oleh-oleh", "pemandangan", "landmark", "monumen", "patung",
    "bangunan", "sejarah", "kebudayaan", "tradisi", "festival", "pesta",
    "perayaan", "ulang tahun", "karnaval", "parade", "upacara", "ritual",
    "adat", "kebiasaan", "warisan", "tradisional", "modern", "kontemporer"
]