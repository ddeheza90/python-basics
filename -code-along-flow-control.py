'''
our_number = 42

is_guessed = False

while is_guessed == False:

# get input from the user 

guess = int(input("Enter your guess: "))

# conditional statements to check the guess

if guess == our_number: 
    print('Hooray!')
elif guess > our_number:
    print("Too high!")
else:
    print("Too low!")

# stop light 

color = "Red"

if color == 'Red':
    print("Stop")
else:
    print('Go!')

# game over 

health = 0

if health <= 0: 
    print('Game Over!')
'''

'''
counter = 1

while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0: 
        print(f'{counter}: Fizzbuzz')
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print (f'{counter}: Buzz')

        counter = counter + 1 

else: 
    print("Done with while loop")
'''
"""
# continue command 

counter = 1

while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0: 
        print(f'{counter}: Fizzbuzz')
        counter += 1
        continue
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print (f'{counter}: Buzz')
              
        
    counter = counter + 1 

else:
    print('Done with while loop!')
"""
"""
# break command 

counter = 1

while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0: 
        print(f'{counter}: Fizzbuzz')
        counter += 1
        break
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print (f'{counter}: Buzz')
              
        
    counter = counter + 1 

else:
    print('Done with while loop!')
"""

# for loop example 

loop_range = range(1, 11)

for i in loop_range:
    print(f'Iteration {i}')

print(max(loop_range))

# for loop with a list 

fruits = ['apple', 'banana', 'cherry', 3, 4.5]

for i in fruits:
    print(f'Fruit: {i}')

