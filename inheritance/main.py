# Pendahuluan Inheritance (Pewarisan)
# Pewarisan antara class ke class
# class pertama di sebut super class dan class kedua di sebut Subclass

# Contoh
class Hero:  # Super class

    def __init__(self, name, health):
        self.name = name
        self.health = health

# cara melakukan inheritance


class Hero_intelegent(Hero):  # ini adalah subclass
    pass


class Hero_strength(Hero):  # ini adalah subclass
    pass


lina = Hero('Lina', 100)
techies = Hero_intelegent('teachies', 50)
axe = Hero_strength('Axe', 200)
print(lina.name)
print(techies.__dict__)
print(axe.__dict__)
