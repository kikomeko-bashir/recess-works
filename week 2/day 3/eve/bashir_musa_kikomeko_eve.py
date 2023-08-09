#exception handling

#types of exceptions 
#SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
#TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
#NameError: This exception is raised when a variable or function name is not found in the current scope.
#IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
#KeyError: This exception is raised when a key is not found in a dictionary.
#ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
#AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
#IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
#ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
#ImportError: This exception is raised when an import statement fails to find or load a module.#

#example 1

items = 50
try:
    a = items / 0
    print(a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#example 2->handling the type exception error
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


#example 4 -> Try and Except Statement – Catching Exceptions
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")


#example 4 -> Catching Specific Exception
def fun(a):
    if a < 4:
        b = a/(a-3)
 
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
 
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")



#example 5 -> with Else Clause
def kiko(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 

kiko(2.0, 3.0)
kiko(3.0, 3.0)


#example 5 -> with finall keyword
try:
    k = 5//0  
    print(k)
 

except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    
    print('This is always executed')




#file handling

#advantages of file handling
#Versatility: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
#Flexibility: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).
#User–friendly: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
#Cross-platform: Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.

#disadvantages of file handling 
#Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
#Security risks: File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
#Complexity: File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
#Performance: File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.

#Working of open() Function in Python
#f = open(filename, mode)  it ivolves modes which are:
#r: open an existing file for a read operation.
#w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
#a:  open an existing file for append operation. It won’t override existing data.
 #r+:  To read and write data into the file. The previous data in the file will be overridden.
#w+: To write and read data. It will override existing data.
#a+: To append and read data from the file. It won’t override existing data.

#Working in Read mode
#example 1
file = open('bash.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)

#example 2
with open("bash.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)


#Working in Write Mode
#example 1
file = open('kikomeko.txt','w')
file.write("my name is")
file.write("kikomeko bashir musa")
file.close()

#example 2
with open("fat.txt", "w") as f:
    f.write("Hello kiko")


#Working of Append Mode
#example 1
file = open('bashir.txt', 'a')
file.write("lets move")
file.close()

#example 2
file = open('musa.txt','a')
file.write("we move")
file.write("regardless")
file.close()










