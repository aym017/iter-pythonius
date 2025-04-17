#First line of code !
print("Hello World")

#Making shapes
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#Variables Introduction
character_name = "Jeff"
ch_age = "64"
print("There was a man named " + character_name + ",")
print("He was " + ch_age + ".")
print("He liked the name "  + character_name + ",")
print("But he didn't like being "  + ch_age + ".")

character_name = "Jordan"
ch_age = "62"
is_male = False
print("There was a man named " + character_name + ",")
print("He was " + ch_age + ".")
character_name = "Pippen"
ch_age = "59.6"
print("He liked the name "  + character_name + ",")
print("But he didn't like being "  + ch_age + ".")

# Plain text= string, Numerical values don't require quotation marks, True/False= Boolean.

# Working with strings

print("Stanford\nUniversity")
print("Stanford\"University")

phrase = "Stanford University"
print(phrase)
print(phrase + " is cool")
#Functions
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
#The first function converts everything to uppercase, and the second converts to lowercase.
#The third on is a true or false: if all characters are uppercase, it'll display 'true' and vice versa

print(phrase.upper().isupper())
#This function works linearly. It first turns the phrase into capital letters, then it checks if all characters are capitalized.