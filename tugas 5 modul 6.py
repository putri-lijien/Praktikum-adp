#INPUT MATRIKS A
print("Masukkan ukuran matriks A:")
baris_a = int(input("Jumlah baris A: "))
kolom_a = int(input("Jumlah kolom A: "))
print("Masukkan elemen-elemen matriks A:")
A = []
for i in range(baris_a):
    baris = []
    for j in range(kolom_a):
        elemen = float(input(f"A[{i+1}][{j+1}]: "))
        baris.append(elemen)
    A.append(baris)

# Input matriks B
print("\nMasukkan ukuran matriks B:")
baris_b = int(input("Jumlah baris B: "))
kolom_b = int(input("Jumlah kolom B: "))

print("Masukkan elemen-elemen matriks B:")
B = []
for i in range(baris_b):
    baris = []
    for j in range(kolom_b):
        elemen = float(input(f"B[{i+1}][{j+1}]: "))    
        baris.append(elemen)
    B.append(baris)

# Loop operasi kalkulator
while True:
    print("\nMenu Kalkulator Matriks:")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinan Matriks")
    print("5. Invers Matriks")
    print("6. Transpose Matriks")
    print("7. Ganti matriks")
    print("8. Keluar")

    pilihan = input("Masukkan pilihan (1-8): ")

    if pilihan == "1":
        if baris_a == baris_b and kolom_a == kolom_b:
            hasil = []
            for i in range(baris_a):
                baris = []
                for j in range(kolom_a):
                    baris.append(A[i][j] + B[i][j])
                hasil.append(baris)
            print("Hasil A + B:")
            for row in hasil:
                print(row)
        else:
            print("Ukuran matriks tidak sama.")

    elif pilihan == "2":
        if baris_a == baris_b and kolom_a == kolom_b:
            hasil = []
            for i in range(baris_a):
                baris = []
                for j in range(kolom_a):
                    baris.append(A[i][j] - B[i][j])
                hasil.append(baris)
            print("Hasil A - B:")
            for row in hasil:
                print(row)
        else:
            print("Ukuran matriks tidak sama.")

    elif pilihan == "3":
        if kolom_a == baris_b:
            hasil = []
            for i in range(baris_a):
                baris = []
                for j in range(kolom_b):
                    total = 0
                    for k in range(kolom_a):
                        total += A[i][k] * B[k][j]
                    baris.append(total)
                hasil.append(baris)
            print("Hasil A x B:")
            for row in hasil:
                print(row)
        else:
            print("Jumlah kolom A harus sama dengan jumlah baris B.")

    elif pilihan == "4":
        if baris_a == kolom_a:
            if baris_a == 2:
                detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                print("Determinan matriks A:", detA)
            elif baris_a == 3:
                detA = (
                    A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
                    - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
                    + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
                )
                print("Determinan matriks A:", detA)
            else:
                print("Determinan hanya dihitung untuk 2x2 atau 3x3 matriks.")
        else:
            print("Matriks A bukan matriks persegi.")

        if baris_b == kolom_b:
            if baris_b == 2:
                detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                print("Determinan matriks B:", detB)
            elif baris_b == 3:
                detB = (
                    B[0][0]*(B[1][1]*B[2][2] - B[1][2]*B[2][1])
                    - B[0][1]*(B[1][0]*B[2][2] - B[1][2]*B[2][0])
                    + B[0][2]*(B[1][0]*B[2][1] - B[1][1]*B[2][0])
                )
                print("Determinan matriks B:", detB)
            else:
                print("Determinan hanya dihitung untuk 2x2 atau 3x3 matriks.")
        else:
            print("Matriks B bukan matriks persegi.")

    elif pilihan == "5":
        if baris_a == kolom_a:
            if baris_a == 2:
                det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                if det != 0:
                    inv = [
                        [ A[1][1]/det, -A[0][1]/det],
                        [-A[1][0]/det,  A[0][0]/det]
                    ]
                    print("Invers matriks A:")
                    for row in inv:
                        print(row)
                else:
                    print("Matriks A tidak memiliki invers.")
            elif baris_a == 3:
                det = (
                    A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
                    A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
                    A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
                )
                if det != 0:
                    cofaktor = [
                        [
                            (A[1][1]*A[2][2] - A[1][2]*A[2][1]),
                            -(A[1][0]*A[2][2] - A[1][2]*A[2][0]),
                            (A[1][0]*A[2][1] - A[1][1]*A[2][0])
                        ],
                        [
                            -(A[0][1]*A[2][2] - A[0][2]*A[2][1]),
                            (A[0][0]*A[2][2] - A[0][2]*A[2][0]),
                            -(A[0][0]*A[2][1] - A[0][1]*A[2][0])
                        ],
                        [
                            (A[0][1]*A[1][2] - A[0][2]*A[1][1]),
                            -(A[0][0]*A[1][2] - A[0][2]*A[1][0]),
                            (A[0][0]*A[1][1] - A[0][1]*A[1][0])
                        ]
                    ]
                    # Transpose kofaktor dan bagi dengan determinan
                    invers = []
                    for i in range(3):
                        baris = []
                        for j in range(3):
                            baris.append(cofaktor[j][i] / det)
                        invers.append(baris)
                    print("Invers matriks A:")
                    for row in invers:
                        print(row)
                else:
                    print("Matriks A tidak memiliki invers.")
            else:
                print("Invers hanya dihitung untuk matriks 2x2 atau 3x3.")
        else:
            print("Matriks A bukan matriks persegi.")

        # Invers matriks B
        if baris_b == kolom_b:
            if baris_b == 2:
                det = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                if det != 0:
                    inv = [
                        [ B[1][1]/det, -B[0][1]/det],
                        [-B[1][0]/det,  B[0][0]/det]
                    ]
                    print("Invers matriks B:")
                    for row in inv:
                        print(row)
                else:
                    print("Matriks B tidak memiliki invers.")
            elif baris_b == 3:
                det = (
                    B[0][0]*(B[1][1]*B[2][2] - B[1][2]*B[2][1]) -
                    B[0][1]*(B[1][0]*B[2][2] - B[1][2]*B[2][0]) +
                    B[0][2]*(B[1][0]*B[2][1] - B[1][1]*B[2][0])
                )
                if det != 0:
                    cofaktor = [
                        [
                            (B[1][1]*B[2][2] - B[1][2]*B[2][1]),
                            -(B[1][0]*B[2][2] - B[1][2]*B[2][0]),
                            (B[1][0]*B[2][1] - B[1][1]*B[2][0])
                        ],
                        [
                            -(B[0][1]*B[2][2] - B[0][2]*B[2][1]),
                            (B[0][0]*B[2][2] - B[0][2]*B[2][0]),
                            -(B[0][0]*B[2][1] - B[0][1]*B[2][0])
                        ],
                        [
                            (B[0][1]*B[1][2] - B[0][2]*B[1][1]),
                            -(B[0][0]*B[1][2] - B[0][2]*B[1][0]),
                            (B[0][0]*B[1][1] - B[0][1]*B[1][0])
                        ]
                    ]
                    invers = []
                    for i in range(3):
                        baris = []
                        for j in range(3):
                            baris.append(cofaktor[j][i] / det)
                        invers.append(baris)
                    print("Invers matriks B:")
                    for row in invers:
                        print(row)
                else:
                    print("Matriks B tidak memiliki invers.")
            else:
                print("Invers hanya dihitung untuk matriks 2x2 atau 3x3.")
        else:
            print("Matriks B bukan matriks persegi.")

    elif pilihan == "6":
        print("Transpose matriks A:")
        for i in range(kolom_a):
            baris = []
            for j in range(baris_a):
                baris.append(A[j][i])
            print(baris)

        print("Transpose matriks B:")
        for i in range(kolom_b):
            baris = []
            for j in range(baris_b):
                baris.append(B[j][i])
            print(baris)

    elif pilihan == "7":
        # Ganti matriks A
        print("\nMasukkan ukuran matriks A:")
        baris_a = int(input("Jumlah baris A: "))
        kolom_a = int(input("Jumlah kolom A: "))
        A = []
        print("Masukkan elemen-elemen matriks A:")
        for i in range(baris_a):
            baris = []
            for j in range(kolom_a):
                elemen = float(input(f"A[{i+1}][{j+1}]: "))
                baris.append(elemen)
            A.append(baris)

        # Ganti matriks B
        print("\nMasukkan ukuran matriks B:")
        baris_b = int(input("Jumlah baris B: "))
        kolom_b = int(input("Jumlah kolom B: "))
        B = []
        print("Masukkan elemen-elemen matriks B:")
        for i in range(baris_b):
            baris = []
            for j in range(kolom_b):
                elemen = float(input(f"B[{i+1}][{j+1}]: "))
                baris.append(elemen)
            B.append(baris)

    elif pilihan == "8":
        print("Terima kasih telah menggunakan kalkulator matriks.")
        break

    else:
        print("Pilihan tidak valid.")