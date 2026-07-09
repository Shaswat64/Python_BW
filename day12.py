# class A():
#     a = 1

# class B(A):
#     b = 67

# class C(B):
#     c = 80

# print(C.__mro__)        #shows how the class is ordered ( From C to B, B to A)


class A():
    a = -1
    def __init__(self):
        pass
class B():
    a=-4
    def __init__(self):
        pass
class C(B,A):
    B.__init__() #super.__init__()  which ever is declared first in the class can be subtituted with super
    A.__init__()
    c = 10

obj = C()
print(obj.a)


    