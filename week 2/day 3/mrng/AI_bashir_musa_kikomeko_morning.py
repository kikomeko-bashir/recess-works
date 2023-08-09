
from tkinter import *

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")
        self.prices = {
            "Sugar": 5000,   
            "Salt": 500,
            "Posho": 2000,
            "Tea Leaves": 1000,
            "Rice": 3000
        }
        self.entries = {}
        self.total = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        for i, (item, price) in enumerate(self.prices.items()):
            Label(self.root, text=item).grid(row=i, column=0)
            self.entries[item] = Entry(self.root)
            self.entries[item].grid(row=i, column=1)
        
        Label(self.root, text="Customer Name:").grid(row=len(self.prices), column=0)
        self.name_entry = Entry(self.root)
        self.name_entry.grid(row=len(self.prices), column=1)
        
        Button(self.root, text="Calculate Total", command=self.calculate_total).grid(row=len(self.prices)+1, column=0)
        
        self.total_label = Label(self.root, text="Total: UGX 0.00")
        self.total_label.grid(row=len(self.prices)+1, column=1)
        
        Button(self.root, text="Print Receipt", command=self.print_receipt).grid(row=len(self.prices)+2, column=0, columnspan=2)
    
    def calculate_total(self):
        self.total = 0
        for item, price in self.prices.items():
            quantity = int(self.entries[item].get())
            self.total += price * quantity
        self.total_label.config(text="Total: UGX {:.2f}".format(self.total))
    
    def print_receipt(self):
        customer_name = self.name_entry.get()
        quantities = {item: int(entry.get()) for item, entry in self.entries.items()}
        
        print("--------------- RECEIPT ---------------")
        print("Customer Name: {}".format(customer_name))
        print("Purchased Items:")
        for item, quantity in quantities.items():
            print("{}: {} x UGX {:.2f} = UGX {:.2f}".format(item, quantity, self.prices[item], self.prices[item] * quantity))
        print("--------------------------------------")
        print("Total: UGX {:.2f}".format(self.total))

# Create the Tkinter application
root = Tk()

# Create the ReceiptApp instance
app = ReceiptApp(root)

# Start the Tkinter event loop
root.mainloop()


