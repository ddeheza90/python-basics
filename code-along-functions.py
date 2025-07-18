# functions are reusable pieaces of code 

print("Hello!")
print("My name is python")

def greet(name):
    name = name.lower()
    name = name.capitalize()
    print(f":Hello, {name}! Welcome to the party!")

def user_input(prompt):
    input_value = input(prompt)



def main_menu():
    print("welcome to the main menu!")
    print("1. Start")
    print("2. Exit")

    choice = input("Please choose an option: ")
    print(f'You chose option {choice}')
    return choice
    
# let user insert more money

print("Hello!")
print("My name is python")
greet("mike")
greet("bob")
main_menu()

main_menu_choice = main_menu()

if main_menu_choice == 1:
        print("Starting the program...")
else:
        print("Existing the program. Goodbye!")
