#class
class Test():
    a = 10
    b = 11

obj = Test()
obj1 = Test()
print(obj)
print(obj == obj1)  #false aauxa beacuse different memory addresses
print(obj.a)
print(obj1.a)

obj.a = "Harry Kane"        #the changes are made in obj but not obj1
obj.c = "Morgan Rogers"

print(obj.a)    
print(obj.c)

print(obj1.a)       #the changes made are only limited to obj but not obj1
# print(obj1.c)

print("--------"*10)

class Test2:
    a = 10
    b = 20

    def add(self,d):
        self.c = 100
        self.d = d
        return d + self.b
    
    def sub(self):
        print(self.d)
        return self.a - self.b
    
    def result(self):
        return self.add(10) + self.sub()


   
obj = Test2()
print(obj.add(20))
print(obj.sub())
obj.a = 20
print(obj.sub())
print(obj.c)
print(obj.result())

print("---------"*15)


class Test3():
    print("Testing")
    def __init__(self):
        print(("Testing"))

obj = Test3

print("---------"*15)




class Test4():
    a = 10
    message = "Testing-Message"

    def __str__(self):
        return  self.message

obj = Test4()
print(obj)


class Test5():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(a,b)

    def add(self):
        return self.a + self.b

obj = Test5(50,1)
print(obj.add())