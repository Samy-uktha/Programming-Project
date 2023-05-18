import tkinter as tk

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item["price"]
        return total_price

def add_item_to_cart(item):
    cart.add_item(item)
    print(f"{item['name']} added to the cart.")
    update_total_price()

def update_total_price():
    total_price = cart.calculate_total_price()
    price_label.configure(text=f"Total Price: ${total_price:.2f}")

def main():
    global cart
    cart = ShoppingCart()

    root = tk.Tk()
    root.title("Shopping Cart")
    root.geometry("1600x750")

    def on_button_click(item):
        add_item_to_cart(item)

    # Create buttons for adding items to the cart
    items = [
        {"name": "1kg apples", "price": 10.99},
        {"name": "1kg bananas", "price": 5.99},
        {"name": "1kg grapes", "price": 7.99}
    ]
    for item in items:
        button = tk.Button(root, text=f"{item['name']} (${item['price']:.2f})", command=lambda item=item: on_button_click(item))
        button.pack()

    global price_label
    price_label = tk.Label(root, text="Total Price: $0.00")
    price_label.pack(side="bottom", pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()
