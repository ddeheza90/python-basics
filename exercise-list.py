# play with for loops

# crete a list 

# use a for loop to iterate through the list 


# Create a list of soccer items 

soccer_gear = ["Soccer cleats", "Soccer shirt", "Soccer shorts", "soccer socks"]

# print the full list 
print("Your soccer gear checklist:")
print(soccer_gear)


# using a loop to print each item 

print("\nItems you need to pack:")
for item in soccer_gear:
    print("-", item)


# Using pop, removing items

soccer_gear = ["Soccer cleats", "Soccer shirt", "Soccer shorts", "soccer socks"]

print("Your soccer gear checklist:")
for item in soccer_gear:
    print("-", item)

# Removing first item

packed_item1 = soccer_gear.pop(0)

# Removing second item 

packed_item2 = soccer_gear.pop(1)

print("\npacked items:")
print("-", packed_item1)
print("-", packed_item2)

# Now show remaining items 

print("\nitems still to pack:")
for item in soccer_gear:
    print("-", item)

