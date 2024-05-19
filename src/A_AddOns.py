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
                                   
                           LDrd.   
               .irjj2KPqbqE52JBB   
             :MqjY7Ub21JvYv7:IB7   
    .jIKv.:..BQ1X1jPEYir7vvri5QQ   
    RYi7:irjPSi7vi::iMrrr7i7jPMMD  
   sZ. .PRBBB1i::irirZS7u2XqdXbgZg 
  :2::5L2gXY:iiirr::rIBdXPqqKq2QSR:
  SKR7QL.7s:77rrBBb.jsDSDSI5X5UdZ25
 s:Erv::KBB.rY: B BgsYSuQBgXLUXX2SS
7i Br:iiiuL:r2  B DQ7YUuMQBQBREI5KZ
IgU5i.:i:::::J  bPqPj211vRQBBgZKDB:
 :BQgI7rvir7Y7U12X5I5dSU1LUU57jBb. 
   .XBQQqq5qKZQBb1jq1viiiuuL:r7b7  
     U7IdddPEqEISPB::2i::dQsKBIJQ  
     dudP7KQDQRPIgI7SQ7:rRrEBBPjB7 
     rBQM7LjBrYBBBXBv.:7BB7sMQIuB. 
      Xg2XbB:  rBBMX.rXM:vQd2uSBX  
       ::::      r::vLr   .r7r7.   
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
                          ████                                                 █████            
                         ░░███                                                ░░███             
 █████ ███ █████  ██████  ░███   ██████   ██████  █████████████    ██████     ███████    ██████ 
░░███ ░███░░███  ███░░███ ░███  ███░░███ ███░░███░░███░░███░░███  ███░░███   ░░░███░    ███░░███
 ░███ ░███ ░███ ░███████  ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████      ░███    ░███ ░███
 ░░███████████  ░███░░░   ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░       ░███ ███░███ ░███
  ░░████░████   ░░██████  █████░░██████ ░░██████  █████░███ █████░░██████      ░░█████ ░░██████ 
   ░░░░ ░░░░     ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░        ░░░░░   ░░░░░░  
   
   
    ███████    █████   ███   █████   █████████    █████████  
  ███░░░░░███ ░░███   ░███  ░░███   ███░░░░░███  ███░░░░░███ 
 ███     ░░███ ░███   ░███   ░███  ███     ░░░  ░███    ░███ 
░███      ░███ ░███   ░███   ░███ ░███          ░███████████ 
░███      ░███ ░░███  █████  ███  ░███          ░███░░░░░███ 
░░███     ███   ░░░█████░█████░   ░░███     ███ ░███    ░███ 
 ░░░███████░      ░░███ ░░███      ░░█████████  █████   █████
   ░░░░░░░         ░░░   ░░░        ░░░░░░░░░  ░░░░░   ░░░░░ 
   
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
"""

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

def MonsterBattle(ascii_1, ascii_2):
    def SplitRow(ascii_art):
      lines = []
      current_line = []
      
      for char in ascii_art:
          if char == '\n':
              lines.append(''.join(current_line))
              current_line = []
          else:
              current_line.append(char)
      
      # Append the last line if there's no trailing newline
      if current_line:
          lines.append(''.join(current_line))
      return lines
    
    ascii_1 = SplitRow(ascii_1)
    ascii_2 = SplitRow(ascii_2)
    vs_ascii = SplitRow(text_ascii['vs'])
    if ascii_1[0] == '':
        ascii_1 = ascii_1[1:]
    if ascii_2[0] == '':
        ascii_2 = ascii_2[1:]
    if vs_ascii[0] == '':
        vs_ascii = vs_ascii[1:]

    if len(ascii_1) > len(ascii_2):
        length = len(ascii_2)
    else:
        length = len(ascii_1)

    for i in range(length):
        print((ascii_1[i]), (vs_ascii[i]), (ascii_2[i]))
    
    return

MonsterBattle(monster_ascii['Pikachow'], monster_ascii['Zuko'])