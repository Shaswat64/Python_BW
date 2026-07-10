# 1. Banking System

# A bank wants to manage different types of accounts.

# Parent Class: Account

# Public Attributes

# account_holder
# account_number

# Private Attributes

# balance
# pin

# Methods

# Deposit money
# Verify PIN
# Display account information
# Child Class: SavingsAccount

# Public Attributes

# interest_rate

# Methods

# Withdraw money after PIN verification
# Calculate yearly interest
# Display complete account summary



class Account():
    def __init__(self, accountHolder,accountNo,balance,pin):
        self.account_holder = accountHolder
        self.account_number = accountNo
        self.__balance = balance
        self.__PIN = pin
    

    def deposited(self,deposit):
        self.deposit = deposit
        self.__new_balance = self.__balance + self.deposit
        print(f'The new balance is = {self.__new_balance}')
        return self.__new_balance
    

    def pinVerify(self,newPIN):
        self.verfiedPIN = newPIN
        if not self.verfiedPIN == self.__PIN :
            return f'The PIN is incorrect'
        else:
            return f'Correct PIN'
    

    def displayinfo(self,pinNum):
        self.deposited()
        self.pin = pinNum
        if(self.pin == self.__PIN):
            return f'''
                Account Holder: {self.account_holder}
                Account Number: {self.account_number}
                '''



class SavingAccount(Account):
    def __init__(self, accountHolder, accountNo, balance, pin, intrestRate):
        self.intrest_rate = intrestRate
        super().__init__(accountHolder, accountNo, balance, pin)
        


