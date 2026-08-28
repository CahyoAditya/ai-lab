"""
============================= NOMOR 2 ====================================

Universitas Negeri Bogor memberikan pilihan golongan biaya UKT kepada
mahasiswanya. Penentuan golongan biaya UKT tersebut ditentukan berdasarkan
beberapa pertimbangan sebagai berikut :

a) Jika BIDIKMISI, mahasiswa akan mendapatkan golongan UKT 1.
b) Jika TIDAK BIDIKMISI, maka ketentuannya adalah :

● Jika total gaji orang tua/wali > Rp 10.000.000, mahasiswa akan
mendapatkan golongan UKT 5.
● Jika total gaji orang tua/wali > Rp 7.000.000 dan <= Rp 10.000.000,
mahasiswa akan mendapatkan golongan UKT 4.
● Jika total gaji orang tua/wali > Rp 4.000.000 dan <= Rp 7.000.000,
mahasiswa akan mendapatkan golongan UKT 3.
● Jika total gaji orang tua/wali <= Rp 4.000.000, mahasiswa akan
mendapatkan golongan UKT 2.
"""

if (input().lower() == "bidikmisi"):
    print("Anda mendapatkan golongan UKT 1")
else:
    gaji = float(input())

    if gaji > 10000000:
        print("Anda mendapatkan golongan UKT 5")
    elif gaji > 7000000:
        print("Anda mendapatkan golongan UKT 4")
    elif gaji > 4000000:
        print("Anda mendapatkan golongan UKT 3")
    else:
        print("Anda mendapatkan golongan UKT 2")
