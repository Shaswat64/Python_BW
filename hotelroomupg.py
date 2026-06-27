num_of_nights = int(input("The number of nights room was booked for: "))
loyalty_member = input("Enter y/Y if you are loyalty member: ").lower()
previous_customer = int(input("How many times has the customer booked rooms? "))

if num_of_nights >= 5:
    if loyalty_member == "y":
        if previous_customer >= 10:
            print("Luxry Upgrade")
        else:
            print("Standard Upgrade")
    else:
        print("No upgrade")
else:
    net_expenditure = int(input("Total expenditure this year: "))
    if loyalty_member == "y":
        if net_expenditure > 2000:
            print("Standard Upgrade")
        else:
            print("No upgrade")
    else:
        print("No upgrade")
