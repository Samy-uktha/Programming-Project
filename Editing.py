import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *


class ShoppingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Program")

        #self.bg_image = tk.PhotoImage(file="supermarket.png")
        #self.bg_label = tk.Label(self.master, image=self.bg_image)
        #self.bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        self.login_page()

    def login_page(self):
        self.username_label = tk.Label(self.master, text="Username:", font="Algerian 20", background="#98EECC")
        self.username_label.place(x=700,y=100)

        self.username_entry = tk.Entry(self.master, font="Arial 20", background="pink")
        self.username_entry.place(x=630,y=150)

        self.password_label = tk.Label(self.master, text="Password:",font="Arial 20", background="98EECC")
        self.password_label.place(x=700,y=250)

        self.password_entry = tk.Entry(self.master, show="*",font="Arial 20",background="pink")
        self.password_entry.place(x=630,y=300)

        self.login_button = tk.Button(self.master, text="Login",font="Algerian 20",background="light green" ,activebackground="green", command=self.login)
        self.login_button.place(x=720,y=400)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate the username and password
        if username == "Admin" and password == "project":
            self.show_sections()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_sections(self):

        self.username_label.destroy()
        self.username_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()

        self.sections = [
            {"name": "Groceries", "subsections": [

                {"name": "Fruits", "items": [
                    {"name": "Orange", "price": 1.50},
                    {"name": "Lemon", "price": 1.00},
                    {"name": "Grapefruit", "price": 2.00}
                ]},

                {"name": "Vegetables", "items": [
                    {"name": "Mango", "price": 2.50},
                    {"name": "Pineapple", "price": 2.00},
                    {"name": "Banana", "price": 0.50}
                ]},

                {"name": "Dairy", "items": [
                    {"name": "butter", "price": 2.50},
                    {"name": "Milk", "price": 2.00},
                    {"name": "Cheese", "price": 0.50},
                    {"name": "gelato", "price": 2.00},
                    {"name": "Curd", "price": 0.50},
                    {"name": "sourcream", "price": 2.00}
                    
                ]},

                {"name": "Bakery", "items": [
                    {"name": "Bread", "price": 2.50},
                    {"name": "garlicbread", "price": 2.00},
                    {"name": "pudding", "price": 0.50},
                    {"name": "custard", "price": 2.50}
                ]}
            ]},
            {"name": "Beverages", "subsections": [

                {"name": "Natural", "items": [
                    {"name": "Spinach", "price": 1.50},
                    {"name": "Lettuce", "price": 1.00},
                    {"name": "Kale", "price": 2.00},
                    {"name": "Papaya", "price": 2.00},
                    {"name": "Apple", "price": 2.00},
                    {"name": "orange", "price": 2.00},
                    {"name": "Banana", "price": 2.00}
                ]},
                {"name": "Artificial", "items": [
                    {"name": "7up", "price": 5.00},
                    {"name": "coke", "price": 4.75},
                    {"name": "Thumbsup", "price": 3.50},
                    {"name": "chocoshake", "price": 2.00},
                    {"name": "milka", "price": 2.00},
                    {"name": "pepsi", "price": 2.00},
                    {"name": "bovonto", "price": 2.00},
                    {"name": "sprite", "price": 2.00},
                    {"name": "pulpy_orange", "price": 2.00}
                    
                ]}
            ]}
        ]

        self.shopping_cart = []

        self.create_sections()

    def create_sections(self):
        for section in self.sections:
            section_button = tk.Button(self.master, text=section["name"],command=lambda section = section: self.open_subsection_window(section))
            section_button.pack(pady=10)
        logout_button = tk.Button(self.master, text="Logout",command= lambda:self.login_page)
        logout_button.pack(side="bottom", pady=20)

    def open_subsection_window(self, section):
        subsection_window = tk.Toplevel(self.master)
        subsection_window.title(section["name"])
        subsection_window.geometry("1920x1080")

        subsection_label = tk.Label(subsection_window, text=section["name"], font=("Helvetica", 16))
        subsection_label.pack(pady=10)

        for subsection in section["subsections"]:
            subsection_button = tk.Button(subsection_window, text=subsection["name"], command=lambda subsection=subsection: self.open_item_window(subsection))
            subsection_button.pack(pady=5)

        back_button = tk.Button(subsection_window, text="Back", command=lambda:[subsection_window.destroy()])
        back_button.pack(side="bottom", pady = 20)


    def open_item_window(self, subsection):
        item_window = tk.Toplevel(self.master)
        item_window.title(subsection["name"])
        item_window.geometry("1920x1080")

        item_label = tk.Label(item_window, text=subsection["name"], font=("Helvetica", 16))
        item_label.pack(pady=10)

        for item in subsection["items"]:

            item_frame = tk.Frame(item_window)
            item_frame.pack(pady=2)

            item_button = tk.Button(item_frame, text=item["name"], command=lambda item=item: self.add_to_cart(item))
            item_button.pack(pady=5)

            quantity_label = tk.Label(item_frame, text= "Quantity: 0")
            quantity_label.pack(side=tk.LEFT, padx=10)
            item["quantity_label"] = quantity_label


            remove_button = tk.Button(item_frame, text="Remove", command=lambda item=item: self.remove_from_cart(item))
            remove_button.pack(side=tk.LEFT)


        generate_bill_button = tk.Button(item_window, text="Generate Bill", command=lambda: self.open_bill_window())
        generate_bill_button.pack(pady=10)

        back_button = tk.Button(item_window, text="Back", command= lambda: [item_window.destroy(),self.open_subsection_window])
        back_button.pack(side="bottom", pady = 20)

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


    def remove_from_cart(self, item):

        for row in self.shopping_cart:
            if row["quantity"] >= 0:
                row["quantity"] -= 1
                item["quantity_label"].config(text=f"Quantity: {row['quantity']}")

                if row["quantity"] == 0:
                    self.shopping_cart.remove(row)

            else:
                messagebox.showinfo("Error", 'Item is not in cart')

        '''if item in self.shopping_cart:
            item["quantity"] -= 1
            item["quantity_label"].config(text=f"Quantity: {item['quantity']}")
            if item["quantity"] == 0:
                self.shopping_cart.remove(item)'''




    def open_bill_window(self):
        bill_window = tk.Toplevel(self.master)
        bill_window.title("Bill")
        bill_window.geometry("1920x1080")

        bill_label = tk.Label(bill_window, text="Bill", font=("Helvetica", 16))
        bill_label.pack(pady=10)

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
        total_label = tk.Label(bill_window, text=f"Total Cost: ${total_cost}", font=("Helvetica", 14))
        total_label.pack(pady=10)

        self.payment_frame = tk.Frame(bill_window)
        self.payment_frame.pack(pady=10)

        tk.Label(self.payment_frame, text="Payment Details").grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(self.payment_frame, text="Card Number:").grid(row=1, column=0, sticky=tk.E)
        self.card_entry = tk.Entry(self.payment_frame)
        self.card_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.payment_frame, text="Name on Card:").grid(row=2, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(self.payment_frame)
        self.name_entry.grid(row=2, column=1, padx=5)

        tk.Label(self.payment_frame, text="CVV:").grid(row=3, column=0, sticky=tk.E)
        self.cvv_entry = tk.Entry(self.payment_frame)
        self.cvv_entry.grid(row=3, column=1, padx=5)

        self.checkout_button = tk.Button(bill_window, text="Checkout", command= lambda:self.checkout())
        self.checkout_button.pack()

        back_button = tk.Button(bill_window, text="Back", command= lambda:[bill_window.destroy(), self.open_item_window])
        back_button.pack(side="bottom", pady=20)



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
                #for button in self.item_buttons:
                 #   button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Please fill in all payment details.")



    def clear_payment_fields(self):
        self.card_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.cvv_entry.delete(0, tk.END)

        self.shopping_cart.clear()




root = tk.Tk()
root.geometry("1920x1080")
app = ShoppingGUI(root)
root.mainloop()

