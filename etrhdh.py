# Supermarket Till Program

# Item list (easy to edit later)
items = {
    "apple": 0.80,
    "bread": 2.50,
    "milk": 1.90,
    "eggs": 3.20,
    "cheese": 4.00,
    "banana": 0.50,
    "chicken": 7.50,
    "rice": 2.00,
    "pasta": 1.80,
    "juice": 2.20
}

cart = {}
total_cost = 0

print("Welcome to the Supermarket Till!")
start = input("Are you ready to start shopping? (yes/no): ").lower()

if start != "yes":
    print("Goodbye!")
else:
    while True:
        print("\nAvailable items:")
        for item, price in items.items():
            print(f"{item.title()} - ${price:.2f}")

        choice = input("\nEnter the item you want to buy: ").lower()

        if choice not in items:
            print("Invalid item. Please choose from the list.")
            continue

        try:
            quantity = int(input("How many would you like? "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        cost = items[choice] * quantity
        total_cost += cost

        # Add to cart
        if choice in cart:
            cart[choice]["quantity"] += quantity
            cart[choice]["cost"] += cost
        else:
            cart[choice] = {"quantity": quantity, "cost": cost}

        print(f"{quantity} x {choice} = ${cost:.2f}")
        print(f"Running total: ${total_cost:.2f}")

        more = input("Do you want to buy more items? (yes/no): ").lower()
        if more != "yes":
            break

    # Print receipt
    print("\n--- Receipt ---")
    for item, details in cart.items():
        print(f"{item.title()} x {details['quantity']} = ${details['cost']:.2f}")

    print(f"\nTotal to pay: ${total_cost:.2f}")
    print("Thank you for shopping!")







items = {
    "apple": 0.80,
    "bread": 2.50,
    "milk": 1.90,
    "eggs": 3.20,
    "cheese": 4.00,
    "banana": 0.50,
    "rice": 2.00,
    "pasta": 1.80,
    "juice": 2.20,
    "chicken": 6.70,
}

cart = {}
total_cost = 0

print (items)