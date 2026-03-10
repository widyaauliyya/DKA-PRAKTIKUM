def isKabisat(tahun): #func untuk memeriksa tahun kabisat atau tidak
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

#memanggil fungsi dan memeriksa hasilnya
tahun_input = int(input("Masukkan tahun: "))

if isKabisat(tahun_input): #check apakah tahun kabisat atau tidak
    print("Tahun", tahun_input, "adalah tahun kabisat.") #jika benar
else:
    print("Tahun", tahun_input, "bukan tahun kabisat.") #jika salah