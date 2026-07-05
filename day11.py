class Parent():
    a = 10
    d = 30
    def add(self):
        return self.a + self.c
    def __init__(self):
        print("From parent")

class Child(Parent):
    a = 20
    c = 100
    b = "King Harry"
    def __init__(self):
        print("From child")
        super().__init__()


obj = Child()
print(obj.a)
print(obj.b)
print(obj.d)


print(obj.add())





