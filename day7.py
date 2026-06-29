# #functions
# def hello():
#     print(f'Hello World!')

# hello()                 #fucntion call
# print(hello())          #function vitra paile print xa, print huncha tara none pani aaucha

# def math():
#     return 1,2,3,[1,2,3]
# print(math())            #tuples ma dinxa multiple variables, but tupule matra pathayo or list matra pathayo vanye single variable suppose garxa


# def math(num1,num2):
#     sum = num1+num2
#     return sum
# math(40,50)
# print(f'The sum of 20 and 30 is {math(20,30)}')

# def name(fname, lname):
#     print(f'My name is {fname} {lname}')
# name("Rijan","Dahal")

# def fun(fname, lname):
#     return f'My name is {fname} {lname}'
# print(fun("Rijan","Dahal"))


# def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
#     print("code here")


# calculate_fine("python",10,5,10) # 50
# calculate_fine("html",1.9,5,10) # error number should in int
# calculate_fine("html",1,"5",0) # error number should in int

def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
    if not (isinstance(borrowed_days,int) and isinstance(allowed_days,int) ):
        print("Error input should be ")
    elif(allowed_days<borrowed_days):
        above_deadline = borrowed_days - allowed_days
        print(f'You have surpassed your deadline, you have to pay {fine_per_day * above_deadline}')
    else:
        print(f'The book you returned {book_name} for {borrowed_days} days was in allowed number of days: {allowed_days}, no fine')

calculate_fine("Muna_Madan",5,7,10)