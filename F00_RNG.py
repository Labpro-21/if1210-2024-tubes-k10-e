def RNG():
    # Fungsi untuk menghasilkan bilangan acak dalam rentang 1-5
    # seed, a, c, m, random_number = integer
    import datetime as time
    a = 16523
    c = 19623
    m = 10923
    
    # Definisikan seed dengan nilai awal waktu (timestamp)
    seed = int(time.datetime.now().timestamp())
    # Menggunakan algoritma LCG untuk menghasilkan bilangan acak dalam rentang 1-5
    random_number = (((a * seed + c) % m) % 5) + 1
    return random_number