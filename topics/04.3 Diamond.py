class A:
    def do_something(self):
        print("Doing something in A")

class B(A):
    def do_something(self):
        print("Doing something in B")

class C(A):
    def do_something(self):
        print("Doing something in C")

class D(B, C):
    pass

d = D()
d.do_something()  # This will print: "Doing something in B"