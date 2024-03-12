# Latihan sederhana

class Hero:

    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, Hero):
        print(self.name + ' menyerang ' + Hero.name)
        Hero.diserang(self, self.attackPower)

    def diserang(self, Hero, attackPower_lawan):
        print(self.name + ' diserang ' + Hero.name)
        attack_diterima = attackPower_lawan / self.armorNumber
        print("serangan serasa : " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " tersisa " + str(self.health))


sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)
