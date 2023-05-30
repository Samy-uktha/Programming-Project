import tkinter as tk
from tkinter import ttk
#import tabulate
#from tabulate import tabulate

class ShoppingList:
    def __init__(self, master):
        self.master = master
        master.title("Shopping List")

        # Create variables to store item names and prices
        #self.items = []
        self.prices = []


        # Create buttons for the items
        apple = tk.Button(master, text="Apple", height=10, width=20,bg="red",command=lambda: self.add_item("Apple", 20)).grid(row=0, column=0, padx=10)
        banana = tk.Button(master, text="Banana", height=10, width=20,bg="yellow" ,command=lambda: self.add_item("Banana", 30)).grid(row=0, column=1)
        orange = tk.Button(master, text="Orange",height=10, width=20,bg="orange", command=lambda: self.add_item("Orange", 40)).grid(row=0, column=2, padx=10)
        mango = tk.Button(master, text="Mango",height=10, width=20,bg="yellow", command=lambda: self.add_item("Mango", 40)).grid(row=0, column=3)
        watermelon = tk.Button(master, text="Watermelon",height=10, width=20,bg="pink", command=lambda: self.add_item("Watermelon", 40)).grid(row=1, column=0)
        pineapple = tk.Button(master, text="Pineapple",height=10, width=20,bg="orange", command=lambda: self.add_item("Pineapple", 40)).grid(row=1, column=1)
        papaya = tk.Button(master, text="Papaya",height=10, width=20,bg="salmon", command=lambda: self.add_item("Papaya", 40)).grid(row=1, column=2)
        jackfruit = tk.Button(master, text="Jackfruit",height=10, width=20,bg="green", command=lambda: self.add_item("Jackfruit", 40)).grid(row=0, column=3)
        dragonfruit=tk.Button(master,text="Dragonfruit",height=10,width=20,bg="orchid",command=lambda:self.add_item("Dragonfruit",50)).grid(row=2,column=3)
        custardapple=tk.Button(master,text="custardapple",height=10,width=20,bg="gold",command=lambda:self.add_item("custardapple",30)).grid(row=2,column=0)
        kiwi=tk.Button(master,text="kiwi",height=10,width=20,bg="aquamarine",command=lambda:self.add_item("kiwi",50)).grid(row=2,column=1)
        peache=tk.Button(master,text="peach",height=10,width=20,bg="crimson",command=lambda:self.add_item("peach,90)).grid(row=2,column=3)
        plum=tk.Button(master,text="plum",height=10,width=20,bg="silver",command=lambda:self.add_item("plum",70)).grid(row=3,column=0)
                                                                                                          

        self.item_prices = {
            apple: 10,
            banana: 10,
            orange: 20,
            mango: 30,
            watermelon: 30,
            pineapple: 40,
            papaya: 30,
            jackfruit: 50,
            Dragonfruit:50,
            custardapple:30,
            peach:90,
            plum:70
        }
        self.shopping_cart = {}


        # Create labels for item name, price and total price
        #tk.Label(master, text="Item:").grid(row=0, column=1)
        #tk.Label(master, text="Price:").grid(row=0, column=2)
        tk.Label(master, text="Total Price:").grid(row=3, column=0)

        # Create a label to display the total price
        self.total_price_label = tk.Label(master, text="0")
        self.total_price_label.grid(row=3, column=1)

        # Create a button to display the bill
        tk.Button(master,text="Generate Bill", command=self.generate_bill).grid(row=4, column=0, columnspan=3)

    def add_to_cart(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1



    def generate_bill(self):
        # Create a new window for the bill
        bill_window = tk.Toplevel(self.master)
        bill_window.title("Bill")
        bill_window.geometry("1000x500")

        bill_table = ttk.Treeview(bill_window, columns=("item", "quantity", "price"), show="headings")
        bill_table.heading("item", text="Item")
        bill_table.heading("quantity", text="Quantity")
        bill_table.heading("price", text="Price")
        bill_table.pack()

        total_cost = 0

        for i in range(len(self.items)):
            price = self.prices[i]
            item_row = (self.items[i], quantity, f"${price * quantity}")
            bill_table.insert("", "end", values=item_row)
            total_cost += price * quantity

        total_row = ("Total Cost:", "", f"${total_cost}")

# Create the main window and run the program
root = tk.Tk()
root.geometry("1700x750")
shopping_list = ShoppingList(root)
root.mainloop()
