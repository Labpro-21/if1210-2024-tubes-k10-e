from A_Functions import *
from F00_RNG import *
import typing

def NaikLevel(monster_data: dict) -> dict:
    attack = int(monster_data['atk_power'] * 11/10)
    defense = int(monster_data['def_power'] * 11/10)
    hp = int(monster_data['hp'] * 11/10)

    monster_data["atk_power"] = attack
    monster_data["def_power"] = defense
    monster_data["hp"] = hp
    return monster_data


def Attack(monster_id: dict) -> int:
    damage = monster_id['atk_power'] * (130-RNG(60))/100
    # Mengeluarkan damage dealt oleh monster
    return damage


def Defend(monster_id: dict) -> float:
    damage_reduction = RNG(monster_id)/100
    # Mengeluarkan presentase damage reduction
    return damage_reduction