from tkinter import *

# Define the prices of each item
prices = {
    "Item 1": 10.00,
    "Item 2": 20.00,
    "Item 3": 30.00,
    "Item 4": 40.00,
    "Item 5": 50.00
}

# Define the function to calculate the total cost
def calculate_total():
    total = 0.00
    quantities = {}
    for item, price in prices.items():
        quantity = int(entries[item].get())
        quantities[item] = quantity
        total += price * quantity
    total_label.config(text="Total: ${:.2f}".format(total))
    return quantities, total

# Define the function to print the receipt
def print_receipt():
    customer_name = name_entry.get()
    quantities, total = calculate_total()

    # Print the receipt
    print("--------------- RECEIPT ---------------")
    print("Customer Name: {}".format(customer_name))
    print("Purchased Items:")
    for item, quantity in quantities.items():
        print("{}: {} x ${:.2f} = ${:.2f}".format(item, quantity, prices[item], prices[item] * quantity))
    print("--------------------------------------")
    print("Total: ${:.2f}".format(total))

# Create the GUI
root = Tk()
root.title("Receipt Printing Program")

# Create the form
entries = {}
for i, (item, price) in enumerate(prices.items()):
    Label(root, text=item).grid(row=i, column=0)
    entries[item] = Entry(root)
    entries[item].grid(row=i, column=1)

# Customer Name
name_label = Label(root, text="Customer Name:")
name_label.grid(row=len(prices), column=0)
name_entry = Entry(root)
name_entry.grid(row=len(prices), column=1)

# Create the button to calculate the total cost
Button(root, text="Calculate Total", command=calculate_total).grid(row=len(prices)+1, column=0)

# Create the label to display the total cost
total_label = Label(root, text="Total: $0.00")
total_label.grid(row=len(prices)+1, column=1)

# Create the button to print the receipt
Button(root, text="Print Receipt", command=print_receipt).grid(row=len(prices)+2, column=0, columnspan=2)

# Start the GUI
root.mainloop()
