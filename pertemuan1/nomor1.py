"""
================================== NOMOR 1 =========================================

    Seorang pemilik kedai kopi di Bogor membutuhkan bantuan untuk menghitung total
harga yang harus dibayar setiap pelanggan di kedai kopinya. Jika total harga makanan
dan minuman yang dibeli oleh pelanggan lebih besar dari Rp 50.000, pelanggan
mendapatkan diskon 27%, jika total harga antara Rp 30.000 sampai dengan Rp 50.000,
maka pelanggan berhak mendapatkan 22%, jika total harga lebih kecil dari Rp 30.000,
maka pelanggan tidak mendapatkan potongan harga.

"""

nomor: float = float(input())

if nomor > 50000:
    nomor = nomor * (1 - 0.27)
elif nomor > 30000:
    nomor = nomor * (1 - 0.22)

print(f"{nomor:.0f}")
