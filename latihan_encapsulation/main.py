# Latihan Encapsulation

from ipaddress import NetmaskValueError


class Hero:

  # Private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandart = health
        self.__attPowerStandart = attPower
        self.__armorStandart = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandart * self.__level
        self.__attPower = self.__attPowerStandart * self.__level
        self.__armor = self.__armorStandart * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} :level : {} \n\thealth = {}/{} \n\tattack : {} \n\tarmor : {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower,  self.__armor)

    # Method Getter
    @property
    def gainExp(self):
        pass

    # Mthod Setter
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'Level Up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandart * self.__level
            self.__attPower = self.__attPowerStandart * self.__level
            self.__armor = self.__armorStandart * self.__level

    def attack(self, musuh):
        self.gainExp = 50


slardar = Hero('sladar', 100, 5, 10)
axe = Hero('axe', 100, 10, 20)
print(slardar.info)
print("\n\t")
slardar.attack(axe)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)
