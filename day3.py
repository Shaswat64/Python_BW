#static 
marks = 30
if (marks>=80 and marks<=100):
    print("Distinction")
elif (marks<=79 and marks>=60):
    print("first")
elif (marks<=59 and marks>=45):
    print("second")
else:
    print("Fail")

#dynamic
marks = int(input("Enter the marks "))
if (marks>=80 and marks<=100):
    if(marks==100):
        print("Full marks")
    else:
        print("Distinction")
elif (marks<=79 and marks>=60):
    print("first")
elif (marks<=59 and marks>=45):
    print("second")
else:
    print("Fail")



#single line
gender = "M"
data = "Male" if gender == "M" else "Female"
print(data)



