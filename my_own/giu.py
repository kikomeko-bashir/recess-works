import tkinter as tk
root = tk.Tk()

root.geometry("500x500")
root.title("kiko's")

#adding a text field
label = tk.Label(root, text="Kiko   ")
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3)
textbox.pack(padx=10)

#adding a button
"""button = tk.Button(root, text="Click Me" )
button.pack(padx=20, pady=20)
"""

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0, column=0,sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0, column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=0, column=2,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=1, column=0,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=1, column=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6")
btn6.grid(row=1, column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()



