# Overide Method

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{}\n\thealth : {} ".format(self.name, self.health))


class Hero_intelligence(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # Overide

    def showInfo(self):
        print("showInfo di subclass intelligent")
        print("{}\n\tTipe : intelligent \n\thealth : {}".format(
            self.name,
            self.health
        )
        )


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_intelligence('lina')
axe = Hero_strength('axe')

lina.showInfo()
axe.showInfo()
