#It looks like there's a missing closing parenthesis and a missing closing quotation mark in the `create_widgets()` method. Here's the corrected code:


import tkinter as tk

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Receipt")
        
        # Item prices in a dictionary
        self.item_prices = {
            "Item 1": 10,
            "Item 2": 15,
            "Item 3": 20,
            "Item 4": 25,
            "Item 5": 30
        }
        
        # Variables to store customer details and purchased items
        self.customer_name_var = tk.StringVar()
        self.purchased_items_var = tk.StringVar()
        self.total_amount_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Receipt Title
        title_label = tk.Label(self.root, text="Shop Receipt", font=("Arial", 16, "bold"))
        title_label.pack()

