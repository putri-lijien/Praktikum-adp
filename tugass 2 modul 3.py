# Pemain 1 memilih rentang angka dan angka bom
n = int(input("Pemain 1, pilih angka positif sampai berapa: "))
k = int(input("Pemain 1, pilih angka bom: "))

# Cetak deretan angka dengan penggantian angka bom menjadi "BOM"
print("\nDeretan angka:")
for i in range(1, n + 1):
    if i % k == 0:
        print("BOM", end=" ")
    else:
        print(i, end=" ")
print("\n")

# Pemain 2 menebak angka
while True:
    tebakan = int(input(f"Pemain 2, tebak angka dari 1 - {n}: "))
    if 1 <= tebakan <= n:
        break
    else:
        print(f"Tebakan tidak valid. Masukkan angka antara 1 dan {n}.")

# Cek apakah angka yang ditebak adalah bom
if tebakan % k == 0:
    print(f"Angka {tebakan} adalah bom, Anda kalah!!")
else:
    print(f"Angka {tebakan} bukan bom, Anda menang!!")