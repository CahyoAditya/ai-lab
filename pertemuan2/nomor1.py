"""
=================================== NOMOR 1 =========================================

    Seorang dosen di Universitas Negeri Bogor (UNB) akan melakukan input nilai akhir
untuk mata kuliah Logika Komputasi. Mahasiswa yang mengambil mata kuliah tersebut
terbagi menjadi dua status, yaitu mahasiswa reguler dan mahasiswa alih jenis. Setiap
status memiliki karakteristik yang berbeda. Mahasiswa reguler hanya akan memiliki nilai
UTS, nilai UAS, Nilai Praktikum, dan Nilai Keaktifan yang tergantung pada seberapa
sering mahasiswa tersebut menjawab pertanyaan dari dosen. Sedangkan mahasiswa alih
jenis memiliki memiliki nilai yang sama seperti mahasiswa reguler, hanya saja terdapat
satu nilai tambahan, yaitu Ujian Matrikulasi. Perlu diperhatikan bahwa setiap mahasiswa
minimal memiliki satu nilai keaktifan. Output yang diharapkan adalah nilai terbobot,
dengan bobot tiap nilai adalah sebagai berikut :

i. Mahasiswa Reguler
- Nilai UTS : 30%
- Nilai UAS : 35%
- Nilai Praktikum : 30%
- Nilai Keaktifan : 5%

ii. Mahasiswa Alih Jenis
- Nilai UTS : 25%
- Nilai UAS : 25%
- Nilai Praktikum : 20%
- Nilai Keaktifan : 5%
- Nilai Ujian Matrikulasi : 25%

NB : Jika terdapat mahasiswa yang memiliki Nilai Keaktifan lebih dari satu, maka
nilai-nilai keaktifan tersebut dirata-ratakan tanpa bobot sebelum dimasukan kedalam
bobot nilai akhir.

Hint : Buatlah dua fungsi berbeda, untuk mahasiswa reguler dan mahasiswa alih jenis!
"""

# Intinya sih,
# -> identifikasi tipe mahasiswa (kalau alih jenis ada matrikulasinya)
# -> hitung rata rata keaktifan
# -> proses berdasarkan tipe mahasiswa
#
# Pertanyaan:
# 1. Bagaimana cara mendapatkan input?

def mahasiswa_reguler(data) -> float:
    data = data.split(", ")
    data = [float(x) for x in data]     # Ubah ke float
    # print("Reguler: ", data)            # Reguler:  [86.0, 78.0, 82.0, 80.0, 81.0, 81.0]

    sum_keaktifan = 0
    for i in range(3, len(data)):
        sum_keaktifan += int(data[i])
    avg_keaktifan = sum_keaktifan / (len(data) - 3)
    # print(sum_keaktifan, avg_keaktifan)

    return (data[0] * 0.3) + (data[1] * 0.35) + (data[2] * 0.3) + (avg_keaktifan * 0.05)

def mahasiswa_alih_jenis(data):
    data = data.split(", ")
    data[len(data) - 1] = data[len(data) - 1].split(" = ")[1]    # Ambil hanya nilai matrikulasi
    data = [float(x) for x in data]     # Ubah ke float
    # print("Alih Jenis: ", data)     # Alih Jenis:  [85.0, 80.0, 86.0, 75.0, 79.0]

    sum_keaktifan = 0
    for i in range(3, len(data) - 1):
        sum_keaktifan += int(data[i])
    avg_keaktifan = sum_keaktifan / (len(data) - 4)
    # print(sum_keaktifan, avg_keaktifan)

    return (data[0] * 0.25) + (data[1] * 0.25) + (data[2] * 0.2) + (avg_keaktifan * 0.05) + (data[len(data) - 1] * 0.25)



# Tadi pas nyari nyari terkait Python, banyak yang pakai ginian
# Ternyata intinya ini mirip mirip sama int main() {} di C
# Mungkin buat selanjutnya bakalan pake ginian terus
if __name__ == "__main__":
    data = input()
    # print(data)

    if "matrikulasi" in data.lower():
        print(mahasiswa_alih_jenis(data))
    else:
        print(mahasiswa_reguler(data))
