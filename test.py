
# This is the list of items that the costomer can choose from and it tells teh cost of each item 
items = [
    ["apple", 0.80],
    ["bread", 2.50],
    ["milk", 1.90],
    ["eggs", 3.20],
    ["cheese", 4.00],
    ["banana", 0.50],
    ["rice", 2.00],
    ["pasta", 1.80],
    ["juice", 2.20],
    ["chicken", 6.70],
]

# This resets the cart to nothing and the cost of the cart to 0
cart = {}
total_cost = 0




        while True:
            print("\nThe items in the store and their cost.")
            for item in items:
                print(item[0], '-',item[1])
            break