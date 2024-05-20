from src.A_Functions import *
from src.F00_RNG import *
import typing

def MonsterBall(user_monster_pool: dict, user_id: int, monster_id: int, monster_level: int) -> dict:
    seed = RNG(100)
    temp = {'user_id'   : user_id,
            'monster_id': monster_id,
            'level'     : monster_level,}

    if monster_level == 1:
        if seed <= 75:
            user_monster_pool.append(temp)
            print("Kamu berhasil menangkap")
            return user_monster_pool
            
    elif monster_level == 2:
        if seed <= 50:
            user_monster_pool.append(temp)
            print("Kamu berhasil menangkap")
            return user_monster_pool
            
    elif monster_level == 3:
        if seed <= 25:
            user_monster_pool.append(temp)
            print("Kamu berhasil menangkap")
            return user_monster_pool
            
    elif monster_level == 4:
        if seed <= 10:
            user_monster_pool.append(temp)
            print("Kamu berhasil menangkap")
            return user_monster_pool
            
    elif monster_level == 5:
        if seed <= 5:
            user_monster_pool.append(temp)
            print("Kamu berhasil menangkap")
            return user_monster_pool

    print("Kamu tidak berhasil menangkap")
    return user_monster_pool