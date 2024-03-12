class Hero:

    # class variabel
    jumlah = 0
    __privateJumlah = 0  # class private

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # private instance variabel
        self.__armor = 'private'  # -> ataidak bisa di akses

        # variable instance protected
        self._protected = "lina"  # -> bisa di akses tapi jangan dirubah


lina = Hero('lina', 100)

print(lina.__dict__)
lina.__armor = 'armor'
print(lina._protected)
lina._protected = "apa"
print(lina.__dict__)
