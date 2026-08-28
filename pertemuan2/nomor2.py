"""
======================================= NOMOR 2 =======================================

    Sebuah robot vacuum cleaner harus membersihkan lantai yang memiliki denah berbentuk
matriks 3x5 sebagai berikut:

0 0 1 0 0
0 1 0 0 0
0 0 1 0 0

    Angka 1 menunjukkan terdapat kotoran yang harus dibersihkan oleh robot. Buatlah
program yang dapat membantu robot membersihkan lantai. Berikut beberapa
kondisi yang perlu diperhatikan:

- Posisi awal robot berada di [0,0] (pojok kiri atas). Posisi akhir robot berada di
[3,5] (pojok kiri bawah). "Hey, maybe something's wrong here!"
- Robot akan berjalan dari kiri ke kanan, namun jika mentok tembok, robot akan
turun ke baris selanjutnya dan berbalik arah.
- Jika bertemu kotoran, robot akan membersihkannya sehingga lantai tersebut
menjadi bersih

Output: Lokasi robot dan update matriks di setiap waktu
"""

# Wait, ini teh tinggal bikin denah tiap waktu dari ubin 3x5?
# Whatever, saya bikin variabel aja nanti di main
#
# Oiya, buat yang pertemuan 2 wajib pakai class nggak sih?
# Jujur nggak ada perintahnya soalnya...

def print_denah(denah, position, step):
    print("t =", step)
    for i in range(len(denah)):
        for j in range(len(denah[i])):
            if (i, j) != position:
                print(denah[i][j], end=" ")
            else:
                if denah[i][j] == 1:
                    denah[i][j] = 0
                print("x", end=" ")
            step += 1
        print()
    print("***")

if __name__ == "__main__":
    # Jujur baru tau juga kalau bisa langsung bikin denah, nggak kepikiran sebelumnya
    denah = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    position = (0, 0)
    step = 1
    for i in range(len(denah)):
        if i % 2 == 0:
            for j in range(len(denah[i])):
                position = (i, j)
                print_denah(denah, position, step)
                step += 1
        else:
            for j in range(len(denah[i]) - 1, -1, -1):
                position = (i, j)
                print_denah(denah, position, step)
                step += 1

    # print("t = 1")
    # print("x 0 1 0 0\n0 1 0 0 0\n0 0 1 0 0")
