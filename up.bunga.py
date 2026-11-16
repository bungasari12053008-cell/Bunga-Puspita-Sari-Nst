jumlah = int(input("masukkan jumlah mahasiswa: "))

data_mahasiswa = []
lulus = 0
tidak_lulus = 0
for i in range(jumlah):
    print("\nmahasiswa ke-", i + 1)

    nama = input("masukkan nama: ")
    nilai = int (input("masukkan nilai: "))

    if nilai >= 85 and nilai <= 100:
        grade = "A"
        keterangan = "sangat baik"
        lulus += 1

    elif nilai >= 75:
        grade = "B"
        keterangan = "baik"
        lulus += 1

    elif nilai >= 60:
        grade = "c"
        keterangan = "cukup"
        lulus += 1

    else:
        grade = "D"
        keterangan = "tidak lulus"
        tidak_lulus += 1

    data_mahasiswa.append([nama, nilai, grade, keterangan])

    print("\n==== HASIL PENILAIAN AKADEMIK ====")

    for data in data_mahasiswa:
        print("nama       :", data[0])
        print("nilai      :", data[1])
        print("grade      :", data[2])
        print("keterangan :", data[3])

    print("-----------------------------")
    print("jumlah mahasiswa  :", jumlah)
    print("jumlah lulus      :", lulus)
    print("tidak lulus       :", tidak_lulus)

