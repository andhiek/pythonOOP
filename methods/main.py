
class Hero:  # Template

    # Class variabel / Statik Variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel / attribute
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

  # void / method tanpa return dan argument
    def nama(self):
        print("namaku adalah " + self.name)

  # method dengan argument
    def healthUp(self, up):
        self.health += up

  # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("sniper", 100, 10, 5)
print(Hero.jumlah)
hero2 = Hero("mirana", 90, 5, 10)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)
print(Hero.jumlah)


hero1.nama()
hero1.healthUp(10)
hero2.nama()
hero3.nama()

print(f"heath hero1 =  { hero1.getHealth()}")
