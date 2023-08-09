"""a) Here is an example of a context manager for file handling that automatically opens and closes a file:

"""
class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


"""You can use it like this:"""


with FileHandler('file.txt', 'w') as f:
    f.write('Hello, world!')


"""b) Here is an example of a context manager for managing a database connection:"""


import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


#You can use it like this:


with DatabaseConnection('mySql.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bashir')
    results = cursor.fetchall()


#c) Here is an example of multithreading and multiprocessing that allows us to run the function for different amounts of time:


import threading
import multiprocessing
import time

def my_function(duration):
    time.sleep(duration)
    print('Function complete!')

# Multithreading
thread1 = threading.Thread(target=my_function, args=(5,))
thread2 = threading.Thread(target=my_function, args=(10,))
thread1.start()
thread2.start()

# Multiprocessing
process1 = multiprocessing.Process(target=my_function, args=(5,))
process2 = multiprocessing.Process(target=my_function, args=(10,))
process1.start()
process2.start()


#The `my_function` takes a duration argument, which is the amount of time the function should run. The `threading.Thread` and `multiprocessing.Process` classes are used to create threads and processes that run the function with different durations.