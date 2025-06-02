# 1. BUAT DATA AWAL
file = open("inventaris_buku.txt", "w")
file.write("ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual\n")
data_buku = [
    ["9780001", "kalkulus", "Purcell", 10, 20000, 35000],
    ["9780002", "Atomic Habits", "James Clear", 5, 22000, 36000],
    ["9780003", "laskar pelangi", " Andrea Hirata", 3, 18000, 30000],
    ["9780004", "real analysis", "Walter Rudin", 2, 25000, 40000],
    ["9780005", "dilan 1990", "Pidi Baiq", 8, 19000, 31000],
    ["9780006", "Dongeng Islami", "Fajar", 6, 21000, 33000],
    ["9780007", "Dare to Lead", "Brene Brown", 4, 23000, 35000],
    ["9780008", "Dongeng Legenda", "Hana", 7, 24000, 36000],
    ["9780009", "Ayah", "Tere Liye", 1, 55000, 65000],
    ["9780010", "Bumi Manusia", "Pramoedya Ananta Toer", 12, 26000, 39000]
]
for buku in data_buku:
    baris = str(buku[0]) + "," + buku[1] + "," + buku[2] + "," + str(buku[3]) + "," + str(buku[4]) + "," + str(buku[5]) + "\n"
    file.write(baris)
file.close()

# 2. BACA & SIMPAN DATA DARI FILE
inventaris = []
file = open("inventaris_buku.txt", "r")
file.readline()  # Skip header
for line in file:
    karakter = []
    for huruf in line:
        if huruf != '\n':
            karakter.append(huruf)
    line_baru = ""
    for huruf in karakter:
        line_baru = line_baru + huruf
    koma = []
    kata = ""
    for huruf in line_baru:
        if huruf == ",":
            koma.append(kata)
            kata = ""
        else:
            kata = kata + huruf
    koma.append(kata)
    buku = {
        "ISBN": koma[0],
        "Judul Buku": koma[1],
        "Penulis": koma[2],
        "Stok": int(koma[3]),
        "Harga Beli": int(koma[4]),
        "Harga Jual": int(koma[5])
    }
    inventaris.append(buku)
file.close()

# 3. HITUNG POTENSI KEUNTUNGAN & SIMPAN KE FILE BARU
file = open("laporan_inventaris.txt", "w")
file.write("ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
for buku in inventaris:
    keuntungan = (buku['Harga Jual'] - buku['Harga Beli']) * buku['Stok']
    buku['Potensi Keuntungan'] = keuntungan
    baris = buku['ISBN'] + "," + buku['Judul Buku'] + "," + buku['Penulis'] + "," + str(buku['Stok']) + "," + str(buku['Harga Beli']) + "," + str(buku['Harga Jual']) + "," + str(keuntungan) + "\n"
    file.write(baris)
file.close()

# 4. ANALISIS INVENTARIS

# a. Buku dengan potensi keuntungan tertinggi & terendah
tertinggi = inventaris[0]
terendah = inventaris[0]
for buku in inventaris:
    if buku['Potensi Keuntungan'] > tertinggi['Potensi Keuntungan']:
        tertinggi = buku
    if buku['Potensi Keuntungan'] < terendah['Potensi Keuntungan']:
        terendah = buku

# b. Total nilai inventaris berdasarkan harga beli
total_nilai = 0
for buku in inventaris:
    total_nilai = total_nilai + (buku['Stok'] * buku['Harga Beli'])

# c. Daftar buku stok < 5
restock = []
for buku in inventaris:
    if buku['Stok'] < 5:
        restock.append(buku)

# TAMPILKAN HASIL ANALISIS
print("\n=== LAPORAN ANALISIS INVENTARIS ===")
print("Buku dengan Potensi Keuntungan Tertinggi: " + tertinggi['Judul Buku'] + " (" + str(tertinggi['Potensi Keuntungan']) + ")")
print("Buku dengan Potensi Keuntungan Terendah : " + terendah['Judul Buku'] + " (" + str(terendah['Potensi Keuntungan']) + ")")
print("Total Nilai Inventaris (berdasarkan harga beli): Rp " + str(total_nilai))
print("\nBuku yang perlu restock (< 5 stok):")
for buku in restock:
    print("- " + buku['Judul Buku'] + " (Stok: " + str(buku['Stok']) + ")")