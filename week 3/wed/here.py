"""class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage example:
with FileHandler('kiko.txt', 'r') as file:
    content = file.read()
    print(content)
"""



import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

# Usage example:
with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    for row in rows:
        print(row)




"""import threading
import multiprocessing
import time

def my_function(seconds):
    print(f"Starting function for {seconds} seconds.")
    time.sleep(seconds)
    print(f"Function completed after {seconds} seconds.")

# Multithreading example:
threads = []
for i in range(1, 6):
    t = threading.Thread(target=my_function, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

# Multiprocessing example:
processes = []
for i in range(1, 6):
    p = multiprocessing.Process(target=my_function, args=(i,))
    processes.append(p)
    p.start()

for process in processes:
    process.join()
"""