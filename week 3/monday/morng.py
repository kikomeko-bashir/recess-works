"""# email varification


# generators and iterators
def factorial(n):
    # return the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

# print the factorial of a number from 1 - 10
for i in range(1, 11):
    print(i, "! =", factorial(i))


#iterators
# example 3 
#generatea function that yields the square of numbers from 1 - 10
def square():
    for i in range(1, 10):
        yield i ** 2

# create an iterator object that yields the square of numbers from 1 - 10
square_iterator = square()

# print the first 5 square of numbers from 1 - 10
for i in range(5):
    print(next(square_iterator))"""

# decorators @my_decorator
"""def my_decorator(func):
    def inner():
        print("I am inner")
        func()
    return inner
    
@my_decorator
def outer_decorator():
    print("I am outer")

outer_decorator()"""

class Squares:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the iterator
squares = Squares(7)
for square in squares:
    print(square)

        