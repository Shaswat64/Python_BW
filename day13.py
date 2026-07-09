class Test():
    a = 10
    __b = 1
    c = __b + 1

    def display(self):
        return self.__b
    def __data(self):
        return self.a
    
obj = Test()
print(obj.a)
# print(obj.__b)  #doesnt give data
print(obj.display())
# print(obj.__data()) #doesnt give data


class A():
    name = "Shaswat"
    __nip = 123
class B(A):
    def display(self):
        return self.name
class C(A):
    def display2(self):
        return self.__nip + 56
    
c = C()
print(c.display2())
c = B
print(c.display())
