# Method Resolution Order // Multiple Inheritance

class A:

    def show(self):
        print("ini adalah show A")


class B:

    def show(self):
        print("ini adalah show B")


class C(A, B):  # urutannya adalah mulai dari C -> A -> B
    pass


class D(B, A):  # urutannya adalah mulai dari D -> B -> A
    pass


objek1 = C()
objek2 = D()
objek1.show()
objek2.show()
# help(objek)
