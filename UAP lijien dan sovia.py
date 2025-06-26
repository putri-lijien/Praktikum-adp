import os
import time
from termcolor import colored
os.system("cls")
print ("\n SELAMAT DATANG DI PROGRAM SAKUKU ")
time.sleep(3)
os.system("cls")

print("=== Program Pengatur Keuangan Anak Kos ===")
uang_bulanan = int(input("Masukkan uang bulanan Anda (Rp): "))

pengeluaran = []  # 2D: [hari, jumlah, kategori]
pemasukan = []

data_kategori = {
    "makan": 0,
    "transport": 0,
    "hiburan": 0,
    "lainnya": 0
}

warna_kategori = {
    "makan": "yellow",
    "transport": "cyan",
    "hiburan": "magenta",
    "lainnya": "blue"
}

def tambah_data(tipe):
    hari = int(input("Hari ke berapa (1-30): "))
    jumlah = int(input("Jumlah (Rp): "))

    while True:
        kategori = input("Kategori (makan/transport/hiburan/lainnya): ")
        if kategori in data_kategori:
            break
        else:
            print(colored("Kategori tidak valid! Harap masukkan sesuai opsi.", "red"))

    if tipe == "keluar":
        pengeluaran.append([hari, jumlah, kategori])
        data_kategori[kategori] += jumlah
    else:
        pemasukan.append([hari, jumlah, kategori])

def hitung_sisa():
    total_keluar = sum([x[1] for x in pengeluaran])
    total_masuk = sum([x[1] for x in pemasukan])
    return uang_bulanan + total_masuk - total_keluar

def tampilkan_tabel(data, judul):
    if not data:
        print(f"\nBelum ada data {judul}.")
        return

    print(f"\nTabel {judul}:")
    print("+--------+--------------+-------------+")
    print("| Hari   | Jumlah (Rp)  | Kategori    |")
    print("+--------+--------------+-------------+")
    for row in data:
        hari, jumlah, kategori = row
        warna = warna_kategori.get(kategori, "white")
        row_text = f"| {hari:<6} | {jumlah:<12} | {kategori:<11} |"
        print(colored(row_text, warna))
    print("+--------+--------------+-------------+")

while True:
    print("\nMenu:")
    print("1. Tambah Pengeluaran")
    print("2. Tambah Pemasukan")
    print("3. Lihat Ringkasan")
    print("4. Simpan ke File & Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_data("keluar")
    elif pilihan == "2":
        tambah_data("masuk")
    elif pilihan == "3":
        sisa = hitung_sisa()
        print(colored(f"\nSisa uang Anda: Rp {sisa}", "green" if sisa > 0 else "red"))

        tampilkan_tabel(pengeluaran, "Pengeluaran")
        tampilkan_tabel(pemasukan, "Pemasukan")

        print("\nPengeluaran per kategori:")
        for k, v in data_kategori.items():
            warna = warna_kategori.get(k, "white")
            print(colored(f"- {k}: Rp {v}", warna))
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid!")

def animasi_selesai():
    for i in range(3):
        os.system('cls')
        print(colored("Menyimpan data" + "." * (i + 1), "cyan"))
        time.sleep(0.4)

animasi_selesai()

with open("laporan_keuangan.txt", "w") as f:
    f.write("=== Laporan Keuangan Bulanan Anak Kos ===\n")
    f.write(f"Uang Bulanan: Rp {uang_bulanan}\n\n")

    f.write("Pengeluaran:\n")
    for row in pengeluaran:
        f.write(f"Hari {row[0]} - Rp {row[1]} ({row[2]})\n")

    f.write("\nPemasukan:\n")
    for row in pemasukan:
        f.write(f"Hari {row[0]} - Rp {row[1]} ({row[2]})\n")

    f.write("\nPengeluaran per kategori:\n")
    for k, v in data_kategori.items():
        f.write(f"- {k}: Rp {v}\n")

    f.write("\nSisa Uang: Rp " + str(hitung_sisa()) + "\n")

print(colored("Data berhasil disimpan ke laporan_keuangan.txt", "yellow"))
os.system("code laporan_keuangan.txt")

