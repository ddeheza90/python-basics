#1

to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed
print(changed_values)

#2 

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics
print(lyrics_split)

#3

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
changed_values = lyrics
print(changed_values)

#4

long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print("Length of village name:", string_length)

#5

my_path = '   /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download'
my_folders = my_path.strip().split("/")
print(my_folders)

#6

composers = "Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"

# Seperate all composers using semicolon
composers_split = composers.split(';')

# Get the third composer 
third_composer = composers_split[2]

# Split that name by the comma
last_name, first_name = third_composer.split(',')

# Reformat it as "first last"
third_composer_name = f"{first_name} {last_name}"

# print it
print(third_composer_name)



left_padded = '            Operators are stading by'
right_padded = 'Call now'

#Strip spaces from both 
clean_left = left_padded.lstrip()
clean_right = right_padded.rstrip()

# Combine them with the exclamation mark

combined = clean_right + '!' + clean_left
print(combined)




student_name = "Owen"
grade = 94.75
assigment_number = 12
print("Student name: %s, Assigment ID: %04d, Grade: %.2f%%" % (student_name, assigment_number, grade))



# Pad employee ID of 5 numbers

employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print("Padded employee ID:", employee_id_padded)

# Print the raw string

print(r"\n represents a new line,") 
# So the r before the string prevents \n from making a new line








