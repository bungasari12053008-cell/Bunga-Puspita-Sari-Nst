#program evaluasi mahasiswa

#input nilai mahasiswa
tugas = float(input("masukan nilai tugas:"))
uts = float(input("masukan nilai uts:"))
uas = float(input("masukan nilai uas:"))
kehadiran =(input("masukan nilai kehadiran:"))

#menghitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) +(0.50* uas)

#menampilkan nilai akhir
print("nilai akhir:", nilai_akhir)

#menentukan status kelulusan
if nilai_akhir >= 75 and kehadiran >=80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 ==0:
        print("status : LULUS DENGAN PRADIKAT")
    else:
        print("status :LULUS")
else:
        print("status: BELUM LULUS")