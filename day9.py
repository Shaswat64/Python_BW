#default argument

def area(r,pie=3.14):
    return pie*r*r

print(area(1))
print(area(1,5))



#lambda function

n = lambda a,b: a+b
print(n(1,2))

a = [1,2,3,4,5]
# result = []
# for i in a:
#     result.append(i*i)
# print(result)

a = [i**2 for i in a]
print(a)

square = lambda *args: [i**2 for i in args]

print(square(1,2,3,4,3,2,2,3,3,3))

