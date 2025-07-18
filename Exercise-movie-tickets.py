# Ticket prices and tax rate 

adult_price = 11.25
child_price = 7.25
tax_rate = 0.075

# Storing available movies in a dictionary 

movies = {
    1: "The Boondock Saints",
    2: "Venom",
    3: "The Hangover"
}

# This function to calculate the price including tax

def calculate_total(adults, children):
    subtotal = (adults * adult_price) + (children * child_price)
    total = subtotal + (subtotal * tax_rate)
    return round(total, 2)

puchase_summary = {}
choice = "y"

# Starting the main ticket purchase loop

while choice.lower() == "y":
    print("\nWelcome to Regal Cinema!")
    print("Now Showing:")

    # show the list of movies and also ask for the movie selection
     
    for key, title in movies.items():
        print(f"{key}. {title}")

movie_num = int(input("What is the movie you want to see (1, 2, 3)?"))
selected_movie = movies.get(movie_num, None)








