# Simple E-Commerce System
# Task 2: Internship Project

# Product list (ID, Name, Price in USD)
products = [
    [1, "Laptop", 500],       
    [2, "Smartphone", 350],    
    [3, "Headphones", 80],
    [4, "Keyboard", 40],
    [5, "Mouse", 25]
]

# Empty cart
cart = []

# Show all products
def show_products():
    print("\nAvailable Products:")
    for p in products:
        print(f"{p[0]}. {p[1]} - ${p[2]}")
    print()

# Add product to cart
def add_to_cart():
    try:
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        # Find product by ID
        found = False
        for p in products:
            if p[0] == product_id:
                cart.append([p[1], p[2], quantity])
                print(f"{quantity} x {p[1]} added to your cart.\n")
                found = True
                break
        if not found:
            print("Invalid Product ID!\n")

    except ValueError:
        print("Please enter valid numbers!\n")

# View items in cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.\n")
    else:
        print("\nItems in your cart:")
        total = 0
        for item in cart:
            name = item[0]
            price = item[1]
            qty = item[2]
            subtotal = price * qty
            total += subtotal
            print(f"- {name} x{qty} = ${subtotal}")
        print(f"Total = ${total}\n")

# Checkout
def checkout():
    if not cart:
        print("Your cart is empty. Please Add some items first.\n")
    else:
        view_cart()
        print("Thank you for shopping with us!\n")
        cart.clear()

# Main menu
while True:
    print("---------- Welcome to Our E-Commerce Store ----------")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    print("---------------")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_products()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.\n")
