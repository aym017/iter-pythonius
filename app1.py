# First line of code !
print("Hello World")

# Making shapes
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables Introduction
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

#Plain text= string, Numerical values don't require quotation marks, True/False= Boolean.

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
#This function works linearly. Turns the phrase into capital letters, then it checks if all characters are capitalized.

print(len(phrase))
#This function counts all characters in 'phrase' including spaces.

print(phrase[0])
#This function basically tells you what the first character in the string is.
#Numbering for strings starts at 0 not 1.
print(phrase.index("t"))
#This function shows the numerical position of a character.
print(phrase.replace("University", "Team"))
#Replaces 'Uni' with 'Team'. Works with letters too.

# Working with numbers.

print(-2.3334)
print(56/0.5)
print(3*9+3)
print(5*(3+5))
#Python can do math. Works with order of operations. Can print all numerical values.

#Modulus operator.
print(13%7)
#Basically divides no.1 with no.2 and gives out the remainder.

my_num = 5
print(my_num)
print(str(my_num))
print( "Lakers in " + str(my_num))

print(abs(my_num))
print(pow(6, 7))
print(max(2, 3))
print(min(2, 3))
print(round(3.4))
#The first func gives the absolute value of-5, which is 5.
#Second one, the second value is the index of the first (6^7).
#Third and fourth one, it gives the max/min number between the 2 values.
#The last one rounds the value off to the nearest whole number.

from math import *

#This imports more math functions. Called a module.

print(floor(3.7))
print(ceil(3.7))
#The first one gives the first number (3), second one rounds the number up (4).

print(sqrt(60))
#This one finds the square root.

# Getting input from users.

name = input("Enter your name: ")
age = (input("Enter your age: "))
print("Hello " + name + "! You are " + age)

# 'int' function is a variable number, no decimal. 'float' is a variable with decimals. MiniCalc in other file.

