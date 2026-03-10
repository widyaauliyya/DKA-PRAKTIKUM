import numpy as np  #menggunakan NumPy agar bisa menyimpan data terstruktur, mirip tabel

#membuat struktur data untuk barang
dtype_barang = np.dtype([
    ('NamaBarang', 'U50'),
    ('KodeBarang', 'U20'),
    ('Jumlah', 'i4'),
    ('HargaPerUnit', 'f8')
])

data = []  #tempat sementara untuk menyimpan semua input sebelum jadi array

#input banyak barang yang akan dimasukkan
n = int(input("Masukkan jumlah barang: "))

#loop sesuai jumlah barang yang dimasukkan
for i in range(n):
    print(f"\nData barang ke-{i+1}")
    nama = input("Nama Barang: ")
    kode = input("Kode Barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga per unit: "))

    #setiap record dimasukkan jadi tuple, lalu ditaruh ke dalam list
    data.append((nama, kode, jumlah, harga))

#mengubah list jadi array NumPy dengan tata letak yang sudah ditentukan
barang = np.array(data, dtype=dtype_barang)

#menampilkan semua data yang sudah diinput
print("\n=== Data Inventaris Barang ===")
for b in barang:
    print(f"Nama: {b['NamaBarang']}, Kode: {b['KodeBarang']}, Jumlah: {b['Jumlah']}, Harga: {b['HargaPerUnit']}")

#menghitung nilai total setiap item dan total keseluruhan
print("\n=== Total Nilai Inventaris ===")
total_nilai = 0
for b in barang:
    nilai = b['Jumlah'] * b['HargaPerUnit']
    print(f"{b['NamaBarang']} : {nilai}")
    total_nilai += nilai

print("Total seluruh nilai inventaris:", total_nilai)

#cari barang berdasar nama atau kode
cari = input("\nMasukkan Nama Barang atau Kode Barang yang dicari: ")

#jika nama atau kode cocok, masukin ke hasil
hasil = barang[(barang['NamaBarang'] == cari) | (barang['KodeBarang'] == cari)]

if len(hasil) > 0:
    print("\nBarang ditemukan:")
    for b in hasil:
        print(f"Nama: {b['NamaBarang']}")
        print(f"Kode: {b['KodeBarang']}")
        print(f"Jumlah: {b['Jumlah']}")
        print(f"Harga per unit: {b['HargaPerUnit']}")
        print(f"Total nilai: {b['Jumlah'] * b['HargaPerUnit']}")
else:
    print("Barang tidak ditemukan.")