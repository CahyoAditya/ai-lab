"""
================================= NOMOR 3 ============================================

    Anda terlibat dalam sebuah proyek untuk membuat agen mobil otonom yang bisa
berkendara tanpa kendali dari manusia sebagai pengemudi. Mobil otonom ini masih
sangat baru dikembangkan oleh perusahaan pemilik proyek sehingga hal yang bisa
dilakukan oleh agen ini sangat terbatas. Agen hanya bisa melakukan 3 hal, seperti pada
tabel di bawah ini :

    +---------+------------+-------------+-----------------+
    | Percept | See people | See nothing | See blind alley |
    +---------+------------+-------------+-----------------+
    | Action  | Brake      | Accelerate  | Reverse         |
    +---------+------------+-------------+-----------------+

NB :
Brake => location += 0, Accelerate => location += 1, Reverse => location -= 1
"""

# Intinya cuman if percept -> Action, gampang lah ya

if __name__ == "__main__":
    location = 0
    while True:
        percept = input("Percept: ")
        if percept.lower() == "see people":
            location += 0
        elif percept.lower() == "see nothing":
            location += 1
        elif percept.lower() == "see blind alley":
            location -= 1
        else:
            print("Invalid percept, Try: see people, see nothing, see blind alley")
        print("Location:", location)
