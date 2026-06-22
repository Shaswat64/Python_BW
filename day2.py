#Type Check
a = 10 #int
a = 1.2 #float
a = True #boolean
a = "s" #string
a = None #Nonetype 
print(type(a))
a = "" #String
a = None  #Nonetype




#Type Casting 
a="10"
print("Before type casting", type(a))
a = 10
print("After type casting", type(a))




#Type Validation
print(isinstance(a, int)) #Gives boolean value true or false



# ** used for power
# // used for divison result in integer
# / used for divison result in float

a = 10
b = 3 
print(

    a+b,
    a**b,
    a*b,
    a/b, a//b, 
    a-b
)





#string can only use two arthimetic operation + and * 
# + joins two string together (concationation)
# * multiplies string with integer for eg "Hello" * 3 gives Hello Hello Hello

a = "broadway "
b = 3

print(a*b, a+a)



#Comparison operators give result in boolean form
# ==	Equal to	5 == 5	True
# !=	Not equal to	5 != 3	True
# >	Greater than	7 > 3	True
# <	Less than	2 < 5	True
# >=	Greater than or equal to	6 >= 6	True
# <=	Less than or equal to	4 <= 6	True





#Logical operataors

is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)  # True



# Logical operators in Python are used to combine conditions and return a boolean result (True or False).

# ➤ List of Logical Operators
# Operator	Meaning	Example	Result
# and	True only if both conditions are true	5 > 3 and 10 > 5	True
# or	True if at least one condition is true	5 > 10 or 3 < 8	True
# not	Reverses (negates) the result	not (5 > 3)	False
# ➤ Examples
#  Using and
# age = 20
# citizen = True
# print(age >= 18 and citizen)  # True
#  Using or
# is_weekend = False
# is_holiday = True
# print(is_weekend or is_holiday)  # True
#  Using not
# logged_in = False
# print(not logged_in)  # True





#if condition
if (1 == 2):
    print("1 is equal ")
else:
    print("1 is not equal")