# Multiple Inheritance


class A:

    def method_A(self):
        print("ini adalah method A")


class B:
    def method_B(self):
        print("ini adalah method B")


class C(A, B):
    pass


objeK = C()

objeK.method_A()
objeK.method_B()
