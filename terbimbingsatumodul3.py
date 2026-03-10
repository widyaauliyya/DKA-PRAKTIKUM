import numpy as np  #menggunakan NumPy agar data bisa dikelola lebih gampang

#atur tipe data buat setiap kolom
dtype_mahasiswa = np.dtype([
    ('Nama', 'U50'),
    ('NIM', 'U20'),
    ('Nilai', 'f8'),
    ('TahunMasuk', 'i4')
])

data = []  #sementara simpan input di list biasa

#input jumlah mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

#input data mahasiswa satu per satu
for i in range(n):
    print(f"\nData mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = float(input("Nilai: "))
    tahun = int(input("Tahun Masuk: "))
    
    #memasukkan tuple data ke list
    data.append((nama, nim, nilai, tahun))

#ubah list jadi array NumPy dengan format yang sudah ditentukan
mahasiswa = np.array(data, dtype=dtype_mahasiswa)

#mencetak semua data mahasiswa
print("\n=== Data Mahasiswa ===")
for m in mahasiswa:
    print(f"Nama: {m['Nama']}, NIM: {m['NIM']}, Nilai: {m['Nilai']}, Tahun Masuk: {m['TahunMasuk']}")

#mengambil kolom nilai supaya bisa dihitung statistiknya
nilai = mahasiswa['Nilai']
print("\n=== Statistik Nilai ===")
print("Nilai Tertinggi :", np.max(nilai)) #nilai maksimum
print("Nilai Terendah  :", np.min(nilai)) #nilai minimum
print("Nilai Rata-rata :", np.mean(nilai)) #rata-rata nilai

#cari data berdasarkan nama atau NIM
cari = input("\nMasukkan Nama atau NIM yang ingin dicari: ")

#hasil akhir
hasil = mahasiswa[(mahasiswa['Nama'] == cari) | (mahasiswa['NIM'] == cari)]

if len(hasil) > 0:
    print("\nData Mahasiswa Ditemukan:")
    for m in hasil:
        print(f"Nama: {m['Nama']}, NIM: {m['NIM']}, Nilai: {m['Nilai']}, Tahun Masuk: {m['TahunMasuk']}")
else:
    print("Data mahasiswa tidak ditemukan.")