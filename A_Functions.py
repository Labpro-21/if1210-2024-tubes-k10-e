import typing

def ManualSplit(list: list, separator: str) -> list[str]:
    new_list: list[str] = []
    item: str = ''
    for i in list:
        if i == separator:
            new_list.append(item)
            item = ''
        else:
            item += i

    new_list.append(item)

    return new_list

def AmbilData(data: str) -> list[dict]:
    file: TextIO = open(data, "r")
    lists: list[str] = []

    for row in file:
        row = row[:-1]
        new_list = ManualSplit(row, ";")
        lists.append(new_list)

    dictionary: list[str] = []
    for row in lists:
        keys: dict = {}
        for columns in range(len(lists[0])):
            keys[lists[0][columns]] = row[columns]
        dictionary += [keys]
    
    return dictionary