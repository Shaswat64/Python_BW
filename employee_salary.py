# Create a base class Employee with attributes:

# employee_id
# name
# basic_salary

# Create a derived class PermanentEmployee that:

# adds bonus and tax_percentage
# calculates gross salary
# calculates tax amount
# calculates net salary
# displays all employee details.


class Employee:
    employee_id = 3456723
    name = "Madueke"
    basic_salary = 1200


class PermanentEmployee(Employee):
    bonus = 20
    tax_percentage = 40

    def gross_salary(self):
        self.bonus_salary = self.bonus + super().basic_salary
        return self.bonus_salary

    def tax_amount(self):
        self.taxed_amount = self.bonus_salary * (self.tax_percentage / 100)
        return self.taxed_amount

    def net_salary(self):
        self.total_salary = self.bonus_salary - self.taxed_amount
        return self.total_salary

    def employee_detail(self):
        self.gross_salary()
        self.tax_amount()
        self.net_salary()
        return f"""
            Employee ID: {super().employee_id}    
            Name: {super().name}  
            Basic Salary: {self.basic_salary}  
            Bonus earned: {self.bonus}     
            Tax percentage: {self.tax_percentage}       
            Tax amount: {self.taxed_amount}  
            Net salary: {self.total_salary}
            """


obj = PermanentEmployee()
print(obj.employee_detail())
