income = int(input("Enter your income "))
cs = int(input("Enter your credit score "))
gr = input("Enter Y/y if you have gurantor ").lower()
if(income>=3000):
    if(cs>=700):
        print("Loan is approved")
    else:
        print("Loan is rejected")
elif(income<3000):
    if(cs>=750):
        if(gr=="y"):
            print("The loan is approved")
        else:
            print("Loan is rejected")
    else:
        print("Loan is rejected")


    
