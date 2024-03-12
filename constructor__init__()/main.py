# class Hero:  # Template
#     pass


# hero1 = Hero()  # Object / instance (instanciate)
# hero2 = Hero()
# hero3 = Hero()

# hero1.name = "sniper"
# hero1.health = 100

# hero2.name = "sven"
# hero2.health = 200

# hero3.name = "ucup"
# hero3.health = 1000


# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)


# Constructor __init__()


class Hero:  # Template

    # Class variabel / Statik Variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("mirana", 100, 15, 1)
hero3 = Hero("ucup", 1000, 100, 0)


print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
