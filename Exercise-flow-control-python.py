# Create the product menu with item names and prices

items = { 'soda': 1.50, 'chips': 2.00, 'candy': 1.00}

# Ask the user to insert money and convert it to a float 

funds = float(input("Insert money into the vending machine: $"))

# Display the product menu to the user

print("\nAvailable Items:")
for item, price in items.items():
    print(f"- {item.capitalize()}: ${price:2f}")

# Begin the transaction loop (this is while the user has money)

while funds > 0:
    choice = input("\nChoose an item to buy (type name exactly):").lower()

    if choice not in items:
        print("Invalid selection. Please choose an item from the menu")
        continue


