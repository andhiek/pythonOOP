# Encapsulasi

class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attpower = attackPower

    # method getter / ambil variable private
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getPower(self):
        return self.__attpower

    # Setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaibaru):
        self.__attpower += nilaibaru


# Awal dari game
megatron = Hero("megatron", 100, 50)
print(megatron.__dict__)


# game berjalan
print(megatron.getName())
print(megatron.getPower())
print(megatron.getHealth())
megatron.diserang(10)
print(megatron.getHealth())
megatron.setAttPower(25)
print(megatron.getPower())
