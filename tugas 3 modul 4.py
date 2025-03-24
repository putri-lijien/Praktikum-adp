# Memasukkan ukuran bioskop dengan validasi minimal 4x4
while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r >= 4 and c >= 4:
        break
    print("Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.")

# Menyimpan kursi yang sudah dipesan
tiket_terpesan = set()

# Menampilkan layout awal
print("\nLayout Kursi Bioskop:")
for i in range(1, r + 1):
    for j in range(1, c + 1):
        nomor_kursi = (i - 1) * c + j
        print(nomor_kursi, end="\t")
    print()
print()

# Loop pemesanan kursi
while True:
    nomor = int(input("Masukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai): "))
    if nomor == 0:
        print("Terima kasih telah memesan tiket!")
        break
    
    if nomor in tiket_terpesan:
        print("Kursi sudah dipesan! Pilih kursi lain.")
    elif 1 <= nomor <= r * c:
        tiket_terpesan.add(nomor)
        print(f"Kursi {nomor} berhasil dipesan!")
    else:
        print("Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia.")
    
    # Menampilkan layout terbaru
    print("\nLayout Kursi Bioskop:")
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            nomor_kursi = (i - 1) * c + j
            if nomor_kursi in tiket_terpesan:
                print("X", end="\t")
            else:
                print(nomor_kursi, end="\t")
        print()
    print()
