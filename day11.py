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





# class A():
#     a = 1

# class B(A):
#     b = 67

# class C(B):
#     c = 80

# print(C.__mro__)        #shows how the class is ordered ( From C to B, B to A)