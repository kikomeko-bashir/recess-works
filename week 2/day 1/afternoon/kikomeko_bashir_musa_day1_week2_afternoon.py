# Functionality involving Functions, Arguments, and Parameters
# Function 1 - Greeting
def greeting_custom():
    print("Salutations, good day!")

print("************************************************************************************************")

# Invoking the custom greeting function
greeting_custom()

# Function 2 with parameters for addition
def sum_custom(a, b):
    print(a + b)

print("************************************************************************************************")

sum_custom(2, 3)

# Function 3 with default parameters for addition
def sum_default(a, b=10):
    print(a + b)

print("************************************************************************************************")

sum_default(2, 3)

# Function 4 with return value for addition
def add_and_return(a, b=10):
    return a + b

print(add_and_return(2, 3))

# Function 5 with multiple return values for addition and subtraction
def add_subtract_custom(a, b=10):
    return a + b, a - b

print(add_subtract_custom(2, 3))

# Function that accepts variable number of arguments and returns their sum
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_values(1, 2, 3, 4))

# Module Utilization in Python
# This script is intended to be utilized in product.py
def address(name):
    print("Greetings,", name)

def compute_square(x):
    return x ** 2

# Importing the mathematics module with a different name
import math as m_lib

print("************************************************************************************************")

print(m_lib.sqrt(16))
print(m_lib.factorial(5))

print("************************************************************************************************")

# Input and Output Handling in Python
user_given_name = input("Please input your appellation: ")
print("Greetings, " + user_given_name)

print("Your provided name is:", input("Kindly input your designation: "))

print("Greetings,", input("Please enter your cognomen: "))

print("************************************************************************************************")

# Receiving multiple inputs in Python
provided_data = input("Kindly provide your denomination and epoch: ")
nomenclature, duration = provided_data.split()

print("Nomenclature:", nomenclature)
print("Duration:", duration)

print("************************************************************************************************")

# Capturing input data into a tuple
data_tuple = (1, 2, 3, 4)
print(type(data_tuple))
print(data_tuple)
list_version = list(data_tuple)
list_version.append(int(input("Provide any whole digit of your preference: ")))
new_tuple_version = tuple(list_version)
print(new_tuple_version)

print("************************************************************************************************")

# Capturing input data into a set
data_set = {"identification", "appellation"}
print(type(data_set))
print(data_set)
list_version_2 = list(data_set)
list_version_2.append(input("Please input an alternate title: "))
new_set_version = set(list_version_2)
print(new_set_version)



 


