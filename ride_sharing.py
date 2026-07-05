class Person:
    name = "Lebron James"
    age = 45
    phone = "9865321457"
    address = "Kalegaun, Dumbai"
class Vehicle:
    vehicle_number = 145325458625
    vehicle_model = "Tiger_800  1940"
    vehicle_type = "Tank"
    liscense_plate = 600
class Driver(Person,Vehicle):
    driver_id = 9874585541
    rides_completed = 365
    earnings_per_rider = 655

    def calculate_earning(self):
        total_earning = self.rides_completed * self.earnings_per_rider
        return total_earning
    def display_info(self):
        self.calculate_earning()
        return f'''
                Driver ID :  {self.driver_id}
                Personal information
                Vehicle information
                Number of rides completed
                Earning per ride
                Total earnings
            '''