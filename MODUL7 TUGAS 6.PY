def input_data_mahasiswa():
    data = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        print(f"\nData mahasiswa ke-{i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        data.append([nama, nim, uts, uas, tugas])
    return data

def hitung_rata_rata(data, kolom):
    total = 0
    for mhs in data:
        total += mhs[kolom]
    return total / len(data)

def hitung_nilai_akhir(data):
    nilai_akhir = []
    for mhs in data:
        akhir = (0.35 * mhs[3]) + (0.35 * mhs[2]) + (0.30 * mhs[4])
        nilai_akhir.append(akhir)
    return nilai_akhir

def urutkan_mahasiswa(data, nilai_akhir):
    for i in range(len(data)):
        data[i].append(nilai_akhir[i])
    
    
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][5] < data[j+1][5]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def buat_garis():
    print("+" + "-"*12 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*12 + "+" + "-"*12 + "+" + "-"*10 + "+")

def tampilkan_hasil(data, rata_uts, rata_uas, rata_tugas, rata_akhir):
    buat_garis()
    print("| {:<10} | {:<8} | {:<8} | {:<8} | {:<10} | {:<10} | {:<8} |".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    buat_garis()
    
    for i in range(len(data)):
        print("| {:<10} | {:<8} | {:<8.2f} | {:<8.2f} | {:<10.2f} | {:<10.2f} | {:<8} |".format(
            data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], i+1))
    
    buat_garis()
    print("| {:<10} | {:<8} | {:<8.2f} | {:<8.2f} | {:<10.2f} | {:<10.2f} | {:<8} |".format(
        "Rata-rata", "", rata_uts, rata_uas, rata_tugas, rata_akhir, ""))
    buat_garis()

def main():
    data_mahasiswa = input_data_mahasiswa()
    
    # Hitung rata-rata
    rata_uts = hitung_rata_rata(data_mahasiswa, 2)
    rata_uas = hitung_rata_rata(data_mahasiswa, 3)
    rata_tugas = hitung_rata_rata(data_mahasiswa, 4)
    
    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(data_mahasiswa)
    
    # Hitung rata-rata nilai akhir
    total_akhir = 0
    for nilai in nilai_akhir:
        total_akhir += nilai
    rata_akhir = total_akhir / len(nilai_akhir)
    
    # Urutkan data
    data_terurut = urutkan_mahasiswa(data_mahasiswa, nilai_akhir)
    
    # Tampilkan hasil
    tampilkan_hasil(data_terurut, rata_uts, rata_uas, rata_tugas, rata_akhir)

main()