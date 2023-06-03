import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

#Creating class and initializing variables
class ShoppingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Program")
        self.login_page()

#defining function for login page with username and password labels and entry boxes
    def login_page(self):

        self.bg_image = tk.PhotoImage(file="supermarket.png")
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        self.username_label = tk.Label(self.master, text="Username:", font="Arial 20", background="salmon")
        self.username_label.place(x=600,y=100)

        self.username_entry = tk.Entry(self.master, font="Arial 20", background="pink")
        self.username_entry.place(x=530,y=150)

        self.password_label = tk.Label(self.master, text="Password:",font="Arial 20", background="salmon")
        self.password_label.place(x=600,y=250)

        self.password_entry = tk.Entry(self.master, show="*",font="Arial 20",background="pink")
        self.password_entry.place(x=530,y=300)

        self.login_button = tk.Button(self.master, text="Login",font="Arial 20",background="light green" ,activebackground="green", command=self.login)
        self.login_button.place(x=640,y=400)

# defining a function login to check if the given username and password matches with a predefined value
    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.open_section_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


# creating a toplevel window containing sections
    def open_section_window(self):

        section_window = tk.Toplevel(self.master)
        section_window.title("Shopping Program")
        section_window.geometry("1920x1080")

        self.bg_image = tk.PhotoImage(file="supermarket.png")
        self.bg_label = tk.Label(section_window, image=self.bg_image)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)


# creating multiple nested dictionaries inside a list self.sections
# first level of dictionaries represents sections, the second level represents subsections, and third level represents items

        self.sections = [
            {"name": "Groceries", "subsections": [

                {"name": "Fruits", "items": [
                    {"name": "Orange", "price": 30},
                    {"name": "Lemon", "price": 30},
                    {"name": "Pineapple", "price": 40},
                    {"name": "Watermelon", "price": 50},
                    {"name": "Pomegranate", "price": 30},
                    {"name": "Kiwi", "price": 40},
                    {"name": "Guava", "price": 40},
                    {"name": "Pear", "price": 30},
                    {"name": "Apple", "price": 20}
                ]},

                {"name": "Vegetables", "items": [
                    {"name": "Spinach", "price": 30},
                    {"name": "Lettuce", "price": 30},
                    {"name": "Onion", "price": 20},
                    {"name": "Chilli", "price": 20},
                    {"name": "Tomato", "price": 30},
                    {"name": "Potato", "price": 30},
                    {"name": "Pumpkin", "price": 40},
                    {"name": "Cauliflower", "price": 40},
                    {"name": "Corn", "price": 40}
                ]},

                {"name": "Dairy", "items": [
                    {"name": "Egg", "price": 20},
                    {"name": "Milk", "price": 30},
                    {"name": "Cheese", "price": 30},
                    {"name": "Gelato", "price": 40},
                    {"name": "Curd", "price": 30},
                    {"name": "Cream", "price": 40}
                ]},

                {"name": "Bakery", "items": [
                    {"name": "Bread", "price": 30},
                    {"name": "Garlic Bread", "price": 40},
                    {"name": "Pudding", "price": 50},
                    {"name": "Cookie", "price": 40},
                    {"name": "Biscuit", "price": 30},
                    {"name": "Cupcake", "price": 50},
                    {"name": "Baguette", "price": 30},
                    {"name": "Muffin", "price": 40},
                    {"name": "Donut", "price": 40},
                    {"name": "Swissroll", "price": 60},
                    {"name": "Pie", "price": 60}
                ]}
            ]},
            {"name": "Other", "subsections": [

                {"name": "Meat", "items": [
                    {"name": "Sausage", "price": 30},
                    {"name": "Chicken", "price": 30},
                    {"name": "Pork", "price": 40},
                    {"name": "Beef", "price": 40},
                    {"name": "Turkey", "price": 40},
                    {"name": "Mutton", "price": 50},
                    {"name": "Venison", "price": 50},
                    {"name": "Meatloaf", "price": 50},
                    {"name": "Salami", "price": 60},
                    {"name": "Ham", "price": 40}
                ]},
                {"name": "Seafood", "items": [
                    {"name": "Prawns", "price": 50},
                    {"name": "Salmon", "price": 40},
                    {"name": "Crab", "price": 60},
                    {"name": "Lobster", "price": 70},
                    {"name": "Shrimp", "price": 70},
                    {"name": "Crawfish", "price": 70},
                    {"name": "Sushi", "price": 60},
                    {"name": "Mussels", "price": 50},
                    {"name": "Oyster", "price": 70},
                    {"name": "Pomfret", "price": 40}
                ]},
                {"name": "Frozen", "items": [
                    {"name": "Ice Cream", "price": 30},
                    {"name": "Popsicle", "price": 30},
                    {"name": "Kulfi", "price": 20},
                    {"name": "Gelato", "price": 40},
                    {"name": "Glace", "price": 40},
                    {"name": "Mochi", "price": 50},
                    {"name": "Ice Cream Sandwich", "price": 40},
                    {"name": "Sundae", "price": 60},
                    {"name": "Ice Cream Bar", "price": 30}
                ]}
            ]},
            {"name": "Snacks", "subsections": [
                {"name": "Chips", "items": [
                    {"name": "Yellow Lays", "price": 20},
                    {"name": "Blue Bingo", "price": 20},
                    {"name": "Kurkure", "price": 20},
                    {"name": "Maxx", "price": 30},
                    {"name": "Red Bingo", "price": 20},
                    {"name": "Pringles", "price": 40},
                    {"name": "Blue Lays", "price": 20},
                    {"name": "Red Lays", "price": 20},
                    {"name": "Red Kurkure", "price": 20},
                    {"name": "Red Maxx", "price": 30}
                ]},
                {"name": "Drinks", "items": [
                    {"name": "Chocolate Milkshake", "price": 30},
                    {"name": "Strawberry Milkshake", "price": 30},
                    {"name": "Banana Milkshake", "price": 30},
                    {"name": "Slice", "price": 20},
                    {"name": "Maaza", "price": 20},
                    {"name": "Fanta", "price": 20},
                    {"name": "Pepsi", "price": 30},
                    {"name": "Coca Cola", "price": 30},
                    {"name": "Sprite", "price": 20},
                    {"name": "Frooti", "price": 20}
                ]},
                {"name": "Chocolate", "items": [
                    {"name": "Dairy Milk", "price": 40},
                    {"name": "Nestle", "price": 30},
                    {"name": "Perk", "price": 20},
                    {"name": "5 Star", "price": 20},
                    {"name": "Kit Kat", "price": 20},
                    {"name": "Milky Bar", "price": 30},
                    {"name": "Munch", "price": 20},
                    {"name": "Hersheys", "price": 40},
                    {"name": "Mars", "price": 30},
                    {"name": "Snickers", "price": 30}
                ]}
            ]}
        ]

        self.shopping_cart = []

        for section in self.sections:
            section_button = tk.Button(section_window,background="pink",text=section["name"],font="Arial 20", command=lambda section = section: [section_window.destroy(),self.open_subsection_window(section)])
            section_button.pack(pady=40)

        logout_button = tk.Button(section_window, width=20,text="Logout",font="Arial 20",background="light blue" ,activebackground="blue",command= lambda:[section_window.destroy(), self.login_page()])
        logout_button.pack(side="bottom", pady=40)

#function to open the subsection window for the selected section
    def open_subsection_window(self, section):

        subsection_window = tk.Toplevel(self.master)
        subsection_window.title(section["name"])
        subsection_window.geometry("1920x1080")

        self.bg_image = tk.PhotoImage(file="aisle.png")
        self.bg_label = tk.Label(subsection_window, image=self.bg_image)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        subsection_label = tk.Label(subsection_window, width=20, background="pink",text=section["name"], font="Arial 30")
        subsection_label.pack(pady=40)

        for subsection in section["subsections"]:
            subsection_button = tk.Button(subsection_window, background="salmon", text=subsection["name"],font="Arial 20", command=lambda subsection=subsection: [subsection_window.destroy(), self.open_item_window(subsection)])
            subsection_button.pack(pady=30)

        back_button = tk.Button(subsection_window, width=20,text="Back",font="Arial 15",background="light blue" ,activebackground="blue", command=lambda:[subsection_window.destroy(), self.open_section_window()])
        back_button.pack(side="bottom", pady = 30)

#function to open the item window for the selected subsection
    def open_item_window(self, subsection):

        item_window = tk.Toplevel(self.master)
        item_window.title(subsection["name"])
        item_window.geometry("1920x1080")

        self.bg_image = tk.PhotoImage(file="items.png")
        self.bg_label = tk.Label(item_window, image=self.bg_image)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        item_label = tk.Label(item_window,width=20,background="pink", text=subsection["name"], font=("Arial", 30))
        item_label.pack(pady=5)

        for item in subsection["items"]:

            item_frame = tk.Frame(item_window,width=100, height=15 ,background="pink")
            item_frame.pack(pady=5)

            item_button = tk.Button(item_frame, background="coral3", width=20, text=item["name"],font="Arial 15", command=lambda item=item: self.add_to_cart(item))
            item_button.grid(column=1, row=1)

            quantity_label = tk.Label(item_frame, text= "Quantity: 0", background="salmon", font="Arial 15")
            quantity_label.grid(column=3,row=1, padx=30)#side=tk.LEFT, padx=30)
            item["quantity_label"] = quantity_label

            price_label = tk.Label(item_frame, text= f"${item['price']}", font="Arial 15")
            price_label.grid(column=2,row=1,padx=30)

            remove_button = tk.Button(item_frame, text="Remove",font="Arial 15", background="crimson", command=lambda item=item: self.remove_from_cart(item))
            remove_button.grid(column=4,row=1, padx=30)#side=tk.LEFT, padx=30)


        generate_bill_button = tk.Button(item_window, text="Generate Bill",font="Arial 20",background="light green" ,activebackground="green", command=lambda: [item_window.destroy(),self.open_bill_window()])
        generate_bill_button.pack(pady=10)

        back_button = tk.Button(item_window, width=20,text="Back",font="Arial 15",background="light blue" ,activebackground="blue", command= lambda :[item_window.destroy(),self.open_section_window()])
        back_button.pack(side="bottom", pady = 30)


#function to add item to the cart
    def add_to_cart(self, item):
        name = item["name"]
        price = item["price"]

        for row in self.shopping_cart:
            if row["name"] == name:
                row["quantity"] += 1
                break
        else:
            self.shopping_cart.append({"name": name, "quantity": 1, "price": price})

        for row in self.shopping_cart:
            item["quantity_label"].config(text=f"Quantity: {row['quantity']}")

#function to remove item from cart
    def remove_from_cart(self, item):

        for row in self.shopping_cart:
            if row["quantity"] >= 0:
                row["quantity"] -= 1
                item["quantity_label"].config(text=f"Quantity: {row['quantity']}")

                if row["quantity"] == 0:
                    self.shopping_cart.remove(row)
            else:
                messagebox.showinfo("Error", 'Item is not in cart')


# function to open a bill window with a table showing items in the cart, quantity, and total price
    def open_bill_window(self):
        bill_window = tk.Toplevel(self.master)
        bill_window.title("Bill")
        bill_window.geometry("1920x1080")

        self.bg_image = tk.PhotoImage(file="bill.png")
        self.bg_label = tk.Label(bill_window, image=self.bg_image)
        self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        bill_label = tk.Label(bill_window, width=30,text="Bill", font="Arial 30", background="pink")
        bill_label.pack(pady=30)

        bill_table = ttk.Treeview(bill_window, columns=("name", "price" , "quantity", "total price"), show="headings")
        bill_table.heading("name", text="Item")
        bill_table.heading("quantity", text="Quantity")
        bill_table.heading("price", text="Price")
        bill_table.heading("total price", text="Total Price")
        bill_table.pack()

        for item in self.shopping_cart:
            total_price = item["quantity"] * item["price"]
            row = (item["name"], f"${item['price']}", item["quantity"], f"${total_price}")
            bill_table.insert("", "end", values=row)

        total_cost = sum(item["price"] * item["quantity"] for item in self.shopping_cart)
        total_label = tk.Label(bill_window, text=f"Total Cost: ${total_cost}", font="Arial 20")
        total_label.pack(pady=10)


        self.payment_frame = tk.Frame(bill_window)
        self.payment_frame.pack(pady=10)

        tk.Label(self.payment_frame,width=30, text="Payment Details", font="Arial 20", background="pink").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.payment_frame, width=30,text="Card Number:",font="Arial 15").grid(row=1, column=0, sticky=tk.E)
        self.card_entry = tk.Entry(self.payment_frame,font="Arial 15")
        self.card_entry.grid(row=1, column=1, padx=20,pady=10)

        tk.Label(self.payment_frame,width=30, text="Name on Card:",font="Arial 15").grid(row=2, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(self.payment_frame,font="Arial 15")
        self.name_entry.grid(row=2, column=1, padx=20, pady=10)

        tk.Label(self.payment_frame,width=30, text="CVV:",font="Arial 15").grid(row=3, column=0, sticky=tk.E)
        self.cvv_entry = tk.Entry(self.payment_frame,font="Arial 15")
        self.cvv_entry.grid(row=3, column=1, padx=20, pady=10)

        self.checkout_button = tk.Button(bill_window, text="Checkout",font="Arial 20", background="light green", activebackground="dark green", command= lambda:self.checkout())
        self.checkout_button.pack()

        back_button = tk.Button(bill_window, width = 20, text="Back",font="Arial 15",background="light blue" ,activebackground="blue", command= lambda:[bill_window.destroy(), self.open_section_window()])
        back_button.pack(side="bottom", pady=30)


#function to add users payment details
    def checkout(self):
        card_number = self.card_entry.get()
        name_on_card = self.name_entry.get()
        cvv = self.cvv_entry.get()

        if card_number and name_on_card and cvv:
            if len(str(card_number)) != 16:
                messagebox.showinfo("Invalid Card Number", "Please enter a valid 16 digit card number")
            elif type(name_on_card) is not str:
                messagebox.showinfo("Invalid Name", "Please enter a valid name")
            elif len(str(cvv)) != 3:
                messagebox.showinfo("Invalid CVV", "Please enter a valid 3 digit CVV")
            else:
                messagebox.showinfo("Checkout", f"Payment Successful!")
                self.shopping_cart.clear()

                self.clear_payment_fields()

        else:
            messagebox.showerror("Error", "Please fill in all payment details.")
            self.open_bill_window()

# function to clear all inputs given after payment is successful
    def clear_payment_fields(self):
        self.card_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.cvv_entry.delete(0, tk.END)

        self.shopping_cart.clear()


root = tk.Tk()
root.geometry("1920x1080")
app = ShoppingGUI(root)
root.mainloop()
