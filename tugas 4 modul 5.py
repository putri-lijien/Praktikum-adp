# input jumlah mahasiswa
jumlah_mahasiswa =int(input("masukkan jumlah mahasiswa praktikum ADP :"))
data_mahasiswa =[]
#input data mahasiswa
for i in range(jumlah_mahasiswa):
    print("Mahasiswa ke-",i+1)
    nama= input("nama mahasiswa:")
    pretest= float(input("nilai pretest:"))
    posttest= float(input("nilai posttest:"))
    makalah= float(input("nilai makalah:"))

    nilai_akhir= round((0.4*pretest)+(0.4*posttest)+(0.2*makalah),2)
    data_mahasiswa.append([nama,nilai_akhir])

# Menampilkan tabel nama dan nilai akhir
print("\nTabel Nilai Mahasiswa:")
print("|  Nama Mahasiswa  |  Nilai Akhir  |")
print("-" * 36)
for mahasiswa in data_mahasiswa:
    print("| ",  mahasiswa[0]  ,  "   |   ",mahasiswa[1], "      |")

# Menghitung rata-rata nilai akhir
total_nilai = 0
for mahasiswa in data_mahasiswa:
    total_nilai += mahasiswa[1]
rata_rata = total_nilai / jumlah_mahasiswa
print("\nRata-rata nilai akhir kelas:", rata_rata)

# Menentukan nilai tertinggi dan terendah
nilai_tertinggi = data_mahasiswa[0][1]
nilai_terendah = data_mahasiswa[0][1]
mahasiswa_tertinggi = data_mahasiswa[0][0]
mahasiswa_terendah = data_mahasiswa[0][0]

for mahasiswa in data_mahasiswa:
    if mahasiswa[1] > nilai_tertinggi:
        nilai_tertinggi = mahasiswa[1]
        mahasiswa_tertinggi = mahasiswa[0]
    if mahasiswa[1] < nilai_terendah:
        nilai_terendah = mahasiswa[1]
        mahasiswa_terendah = mahasiswa[0]

print("\nNilai tertinggi:", nilai_tertinggi, "oleh", mahasiswa_tertinggi)
print("Nilai terendah:", nilai_terendah, "oleh", mahasiswa_terendah)

# Menampilkan mahasiswa dengan nilai di atas rata-rata
print("\nMahasiswa dengan nilai di atas rata-rata:")
for mahasiswa in data_mahasiswa:
    if mahasiswa[1] > rata_rata:
        print(mahasiswa[0], "-", mahasiswa[1])