# Data Diri
nama = input("Masukkan nama anda: ")
umur = input("Masukkan umur anda: ")
jenis_kelamin = input("Masukkan jenis kelamin (P/L): ")

# Pilih kode maskapai
print("\nKode maskapai yang tersedia:")
print("1. 3012 - Padang - Jakarta")
print("2. 4015 - Padang - Batam")
print("3. 4050 - Padang - Bandung")

kode_maskapai = input("Masukkan kode maskapai: ")

# Menentukan Tujuan dan Harga
if kode_maskapai == "3012":
    tujuan = "Padang - Jakarta"
    harga = {"Ekonomi": 800000, "Bisnis": 850000, "First Class": 900000}
elif kode_maskapai == "4015":
    tujuan = "Padang - Batam"
    harga = {"Ekonomi": 500000, "Bisnis": 550000, "First Class": 700000}
elif kode_maskapai == "4050":
    tujuan = "Padang - Bandung"
    harga = {"Ekonomi": 700000, "Bisnis": 750000, "First Class": 850000}
else:
    print("Kode maskapai tidak valid!")
    exit()

# Memilih kelas pesawat
print("\nKelas tiket pesawat:")
print("1. Ekonomi")
print("2. Bisnis")
print("3. First Class")

pilihan_kelas = input("Masukkan jenis kelas (Ekonomi, Bisnis, First Class): ")

if pilihan_kelas not in harga:
    print("Jenis kelas tidak valid!")
    exit()

# Input jumlah tiket
jumlah_tiket = int(input("Masukkan jumlah tiket: "))
total_harga = harga[pilihan_kelas] * jumlah_tiket

# Diskon jika membeli lebih dari 3 tiket
if jumlah_tiket > 3:
    diskon = total_harga * 0.2
    total_harga -= diskon
else:
    diskon = 0

# Struk Pemesanan
print("\n=== Struk Pemesanan Tiket ===")
print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Jenis Kelamin: {jenis_kelamin}")
print("-----------------------------")
print(f"Kode Maskapai: {kode_maskapai}")
print(f"Tujuan: {tujuan}")
print(f"Jenis Kelas: {pilihan_kelas}")
print(f"Jumlah Tiket: {jumlah_tiket}")
print(f"Total Harga: Rp{total_harga:,}")
if diskon > 0:
    print(f"(Diskon 20%: Rp{diskon:,})")
print("==============================")