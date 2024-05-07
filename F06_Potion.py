import typing

def StrengthPotion(monster_data: dict) -> dict:
    monster_data['atk_power'] = int(monster_data['atk_power'] * 1.05)
    return monster_data

def ResiliencePotion(monster_data: dict) -> int:
    monster_data['def_power'] = int(monster_data['def_power'] * 1.05)
    return monster_data

def HealingPotion(current_monster_data: dict, monster_data: dict) -> int:
    current_monster_data['hp'] = current_monster_data['hp'] * 1.25
    if current_monster_data['hp'] > monster_data['hp']:
        current_monster_data['hp'] = monster_data['hp']
    return current_monster_data
