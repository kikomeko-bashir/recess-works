# Regular expressions
# match first word, group word, all numbers

import re
txt = 'hey Bashir I am a software developer with 3 years of experience'

# match first word
match = re.search(r"\b\w+\b", txt)
if match:
    print(match.group())

# match all numbers
matches = re.findall(r"\d+", txt)
print(matches)

# Email validation


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\w+$'
    if re.match(pattern, email):
        return True

    else:
        return False


email1 = "kikomekobashir29@gmail.com"
email2 = "kikomekobashir.29gmail"

print(validate_email(email1))
print(validate_email(email2))


# generators and iterators
"""
    __iter__
    __next__
    yield - keyword for generator
"""


def factorial(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * factorial(m-1)


def factorial_generator(m, n):
    for i in range(m, n):
        yield factorial(i)


# displaying the factorial values
for f_value in factorial_generator(1, 15):
    print(f_value)


# another sample generator concept
def factorial(n):
    if n == 0:
        yield 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        yield fact


for i in range(1, 6):
    print(*factorial(i))


# Decorators - @my_decorator
# They are used to modify the behaviour of a class/function without
# directly changing their source code.
def my_decorator(func):
    def inner():
        print("I am inner")
        func()
    return inner


@my_decorator
def outer():
    print("I am outer")


outer()
