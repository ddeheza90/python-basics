items = { 
    "soda": 1.50,
    "chips": 2.00, 
    "candy": 1.00, 
    "water": 1.25,
}

# Welcome User 

print("welcome to Vending Machine!")

# Prompt user for money 
"""
funds = float(input("Please input the amount of money you have:"))
print(f'${funds}')

# Display menu

for item , price in items.items():
    print(f'-{item}: ${price: 2f}')

# Create loop; as long as person has funds



    choice = input("Please pick from the menu:")
    if choice in items:
        if funds >= item:
            balance = funds -items
            print(balance)
"""

# Ask if they want to make another purchase 

again = True 

while again == True:
  input_again = input("if you dont want to make another purchase, type no: ")
if input_again == "no":
  goAgain = False


    