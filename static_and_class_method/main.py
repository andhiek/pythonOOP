# Static method anf Class method


class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Getter
    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object tapi berlaku untuk Class
    def getjumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke object dan class

    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(Hero.getjumlah1())
rikimaru = Hero("rikimaru")
print(sniper.getJumlah())
ranger = Hero("ranger")
print(ranger.getJumlah3())
