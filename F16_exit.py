import F15_save
def exit(bigdata):
    valid = False
    while valid == False:
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan.lower() == 'y':
            F15_save.save(bigdata)
            valid = True
        elif simpan.lower() == 'n' :
            valid = True
        else:
            valid = False