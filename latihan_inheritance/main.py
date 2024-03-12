# Latihan Inheritance
from Hero import Hero_intelligent, Hero_strength


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')


lina.showInfo()
axe.showInfo()
print("\n")
lina.gainExp = 200
axe.gainExp = 250
print("\n")
lina.showInfo()
axe.showInfo()
