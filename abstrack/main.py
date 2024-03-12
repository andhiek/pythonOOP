# Abstrack

# A. class biasa instancenya adalah objek / blueprint dari objek
# B .class Abstrct instancenya adalah class / blueprint dari class


# Contoh
# abc adalah (abstract base class)
from abc import ABC, abstractmethod

# untuk membuat class abstract sebuah class harus di inherit dari method ABC


class Button(ABC):

    @abstractmethod  # -> decorator class abstract
    def click(self):
        print('Button click')


class PushButton(Button):

    def click(self):
        print("push button click")


class RadioButton(Button):

    def click(self):
        print("Radio Button click")


tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
