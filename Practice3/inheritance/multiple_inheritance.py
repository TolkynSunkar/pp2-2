class A:
    def hello(self):
        print("Hello from A")

class B:
    def bye(self):
        print("Goodbye from B")

class C(A, B):
    pass

c = C()
c.hello()
c.bye()