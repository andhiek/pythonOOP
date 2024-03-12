# GetterAnd Setter


class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = "name {}: \n\thealth: {}".format(
        #     self.name, self.__health)

    @property  # Berperilaku dynamic
    def info(self):
        return "name {}: \n\thealth: {}".format(
            self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None

    def gethealth(self):
        return self.__health


sniper = Hero('sniper', 100, 50)
print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk  __armor')
print(sniper.armor)
sniper.armor = 20
print(sniper.armor)
print('delete armor')
del sniper.armor
print(sniper.armor)
