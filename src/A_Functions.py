import typing
import os


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
            if row[columns].isdigit():
                keys[lists[0][columns]] = int(row[columns])
            else: keys[lists[0][columns]] = row[columns]
        dictionary += [keys]
    
    return dictionary


def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ManualIsDigit(var: str) -> bool:
    if not var:
        return False
    for char in var:
        if not 48 <= ord(char) <= 57:
            return False
    return True


def InputVerifier(message: str) -> int:
    while True:
        # Print message
        print(message)
        var = input(">>> ")
        # Mengecek apakah digit atau bukan
        if ManualIsDigit(var):
            var = int(var)
            return var
        else:
            print("Oops, input salah!\n")

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

# MonsterBattle(monster_ascii['Pikachow'], monster_ascii['Zuko'])


def ManualJoin(words: list, separator: str) -> str:
    result = ""
    for index, item in enumerate(words):
        if index > 0:
            result += separator
        result += item
    return result


def Coloredtext(text: str, color_code: int) -> str:
    return f"\033[1;{color_code}m{text}\033[0m"