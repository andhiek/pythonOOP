# Abstrack dan decorator


# abc adalah (abstract base class)
from abc import ABC, abstractmethod


# untuk membuat class abstract sebuah class harus di inherit dari method ABC


class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod  # -> decorator class abstract
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        print("Go to : {}".format(self.link))

    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link


tombol1 = PushButton("www.kelasTerbuka.id")

tombol1.click()
