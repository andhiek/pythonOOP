# Magic Method -> adalah method yang sudah ada di python yang bisa kita gunakan kembali


class Mangga:

    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):  # Digunakan pada saat Debuging
        return "Debug : Mangga : {} dengan jumlah : {}". format(self.nama, self.jumlah)

    def __str__(self):  # Digunakan pada saat Program sudah selesai atau produksi
        return "Mangga : {} dengan jumlah : {}". format(self.nama, self.jumlah)

    # Magic method aritmatika
    def __add__(self, objek):
        return "Total Belanja = {} Buah".format(self.jumlah + objek.jumlah)

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan Jumlah "


belanja1 = Mangga("Gadung", 10)
belanja2 = Mangga("Mana lagi", 5)

print(repr(belanja1))
print(belanja2)

print(belanja1 + belanja2)

print(belanja1.__dict__)
