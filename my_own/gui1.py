import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="MyGUI")
        self.label.pack(padx=10, pady=10 )

        self.textbox = tk.Text(self.root )
        self.textbox.pack(padx=10, pady=10 )

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="show message", variable=self.check_state)
        self.check.pack(padx=10, pady=10 )

        self.button = tk.Button(self.root, text="show message", command=self.show_message)
        self.button.pack(padx=10, pady=10 )

        self.root.mainloop()



    def show_message(self):
      """print (self.check_state.get())"""
      if self.check_state.get() == 1:
        print(self.textbox.get('1.0', tk.END))
      else:
       messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

MyGUI()