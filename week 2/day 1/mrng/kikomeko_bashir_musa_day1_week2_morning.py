class BankAccount:
    def __init__(self, account_number, balance, amount):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount

    def display(self):
        print(self.account_number, self.balance, self.amount)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.balance)

account1 = BankAccount("123272gs", 70000000, 9900000)
account1.display()
account1.deposit(2000000)
account1.withdraw(2000)
account1.display_balance()

print("=====================================================================================================================")

class CustomRectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(self.length * self.width)

    def calculate_parameter(self):
        print(2 * (self.length + self.width))

rectangle = CustomRectangle(23, 12)
rectangle.calculate_area()
rectangle.calculate_parameter()

print("###############################################################################################")

class SoftwareEngineeringStudent:
    def __init__(self, name, student_no, age):
        self.name = name
        self.student_no = student_no
        self.age = age

    def display(self):
        print("I am a software engineering student known as", self.name, "with student number", self.student_no, "and", self.age, "years old.")

student = SoftwareEngineeringStudent("Kikomeko Bashir Musa", "2100705034", 23)
student.display()

print("###############################################################################################")

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(3.14 * self.radius ** 2)

    def calculate_circumference(self):
        print(2 * 3.14 * self.radius)

circle = CircleCalculator(5)
circle.calculate_area()
circle.calculate_circumference()

print("###############################################################################################")

class BonusCalculator:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, "has a salary of", self.salary)

    def calculate_bonus(self):
        if self.salary > 5000:
            print(self.salary * 0.15)
        else:
            print(self.salary)

employee1 = BonusCalculator("Kikomeko", 23000)
employee1.display()
employee1.calculate_bonus()
employee2 = BonusCalculator("Musa", 25700)
employee2.display()
employee2.calculate_bonus()

class CustomCar:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    def drive(self, distance):
        self._mileage += distance

my_car = CustomCar("Toyota", "Subaru", 2022)
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())
print("Mileage:", my_car.get_mileage())
my_car.drive(100)
print("Mileage after driving:", my_car.get_mileage())

print("###############################################################################################")

class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp_converter = TemperatureConverter(37)
celsius_temp = temp_converter.get_celsius()
print("Celsius Temperature:", celsius_temp)
fahrenheit_temp = temp_converter.get_fahrenheit()
print("Fahrenheit Temperature:", fahrenheit_temp)

print("###############################################################################################")

class PayIncreaseEmployee:
    def __init__(self, name, employee_id, salary):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increase_salary(self, increment_amount):
        self._salary += increment_amount

employee = PayIncreaseEmployee("Kikomeko Bashir Musa", "IP132", 1000000)
name = employee.get_name()
employee_id = employee.get_employee_id()
salary = employee.get_salary()
print("Name:", name)
print("Employee ID:", employee_id)
print("Salary:", salary)
increment_amount = 150000
employee.increase_salary(increment_amount)
new_salary = employee.get_salary()
print("Updated Salary:", new_salary)





