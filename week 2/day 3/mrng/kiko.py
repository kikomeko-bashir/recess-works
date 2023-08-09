import tkinter as tk

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Receipt")
        
        # Item prices in a dictionary
        self.item_prices = {
            "Salt": 2,
            "Sugar": 4,
            "Tea Leaves": 1,
            "Groundnuts (Gnuts)": 3,
            "Posho": 3.5
        }
        
        # Variables to store customer details and purchased items
        self.customer_name_var = tk.StringVar()
        self.purchased_items_var = tk.StringVar()
        self.total_amount_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Receipt Title
        title_label = tk.Label(self.root, text="Shop Receipt", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Customer Name
        name_label = tk.Label(self.root, text="Customer Name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root, textvariable=self.customer_name_var, width=30)
        self.name_entry.pack()
        
        # Purchase Items
        items_label = tk.Label(self.root, text="Purchase Items (separate with comma):")
        items_label.pack()
        self.items_entry = tk.Entry(self.root, width=30)
        self.items_entry.pack()
        
        # Calculate Button
        calculate_btn = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        calculate_btn.pack(pady=10)
        
        # Total Amount
        total_label = tk.Label(self.root, text="Total Amount:")
        total_label.pack()
        total_value = tk.Label(self.root, textvariable=self.total_amount_var, font=("Arial", 14, "bold"))
        total_value.pack()
        
        # Print Button
        print_btn = tk.Button(self.root, text="Print Receipt", command=self.print_receipt)
        print_btn.pack(pady=20)
    
    def calculate_total(self):
        # Get the customer name and purchased items
        customer_name = self.customer_name_var.get()
        purchased_items = self.items_entry.get()
        
        # Split the items into a list and calculate the total amount
        items_list = purchased_items.strip().split(",")
        total = sum(self.item_prices.get(item.strip(), 0) for item in items_list)
        
        # Update the total amount label
        self.total_amount_var.set(f"${total:.2f}")
    
    def print_receipt(self):
        # Get the customer name and purchased items
        customer_name = self.customer_name_var.get()
        purchased_items = self.items_entry.get()
        
        # Split the items into a list and calculate the total amount
        items_list = purchased_items.strip().split(",")
        total = sum(self.item_prices.get(item.strip(), 0) for item in items_list)
        
        # Print the receipt
        print("--------------- SHOP RECEIPT ---------------")
        print(f"Customer Name: {customer_name}")
        print("Purchased Items:")
        for item in items_list:
            print(f"{item.strip()}: ${self.item_prices.get(item.strip(), 0):.2f}")
        print(f"Total Amount: ${total:.2f}")
        print("-------------------------------------------")

# Create the Tkinter application
root = tk.Tk()

# Create the ReceiptApp instance
app = ReceiptApp(root)

# Start the Tkinter event loop
root.mainloop()
