# # First line of code !
# print("Hello World")
#
# # Making shapes
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
#
# # Variables Introduction
# character_name = "Jeff"
# ch_age = "64"
# print("There was a man named " + character_name + ",")
# print("He was " + ch_age + ".")
# print("He liked the name "  + character_name + ",")
# print("But he didn't like being "  + ch_age + ".")
#
# character_name = "Jordan"
# ch_age = "62"
# is_male = False
# print("There was a man named " + character_name + ",")
# print("He was " + ch_age + ".")
# character_name = "Pippen"
# ch_age = "59.6"
# print("He liked the name "  + character_name + ",")
# print("But he didn't like being "  + ch_age + ".")
#
# #Plain text= string, Numerical values don't require quotation marks, True/False= Boolean.
#
# # Working with strings
#
# print("Stanford\nUniversity")
# print("Stanford\"University")
#
# phrase = "Stanford University"
# print(phrase)
# print(phrase + " is cool")
# #Functions with string
# print(phrase.upper())
# print(phrase.lower())
# print(phrase.isupper())
# #The first function converts everything to uppercase, and the second converts to lowercase.
# #The third on is a true or false: if all characters are uppercase, it'll display 'true' and vice versa
#
# print(phrase.upper().isupper())
# #This function works linearly. Turns the phrase into capital letters, then it checks if all characters are capitalized.
#
# print(len(phrase))
# #This function counts all characters in 'phrase' including spaces.
#
# print(phrase[0])
# #This function basically tells you what the first character in the string is.
# #Numbering for strings starts at 0 not 1.
# print(phrase.index("t"))
# #This function shows the numerical position of a character.
# print(phrase.replace("University", "Team"))
# #Replaces 'Uni' with 'Team'. Works with letters too.
#
# # Working with numbers.
#
# print(-2.3334)
# print(56/0.5)
# print(3*9+3)
# print(5*(3+5))
# #Python can do math. Works with order of operations. Can print all numerical values.
#
# #Modulus operator.
# print(13%7)
# #Basically divides no.1 with no.2 and gives out the remainder.
#
# my_num = 5
# print(my_num)
# print(str(my_num))
# print( "Lakers in " + str(my_num))
#
# print(abs(my_num))
# print(pow(6, 7))
# print(max(2, 3))
# print(min(2, 3))
# print(round(3.4))
# #The first func gives the absolute value of-5, which is 5.
# #Second one, the second value is the index of the first (6^7).
# #Third and fourth one, it gives the max/min number between the 2 values.
# #The last one rounds the value off to the nearest whole number.
#
# from math import *
#
# #This imports more math functions. Called a module.
#
# print(floor(3.7))
# print(ceil(3.7))
# #The first one gives the first number (3), second one rounds the number up (4).
#
# print(sqrt(60))
# #This one finds the square root.
#
# # Getting input from users.
#
# name = input("Enter your name: ")
# age = (input("Enter your age: "))
# print("Hello " + name + "! You are " + age)
#
# # 'int' function is a variable number, no decimal. 'float' is a variable with decimals. MiniCalc in other file.
#
# # Lists
#
# players = ["De Bruyne", "Hazard", "Dybala", "Coutinho", "Pogba"]
# print(players)
# print(players[0])
# print(players[-1])
# print(players[2:])
# print(players[2:4])
# #Func 1 prints all variables in 'players', func 2 specifies the first value (0), func 3 prints the first value from the back.
# #Func 4 prints all the values after variable 2, including 2. Func 5 prints all variables starting from 2 up to but not including 4.
#
# players[3] = "Dembele"
# print(players[3])
# print(players)
# #Switches variable 3 to Dembele then prints variable 3. It also re-prints 'players' in this new format.
#
# # List Functions.
#
# lucky_numbers = [71, 19, 12, 25, 7, 69]
# people = ["John", "Tim", "Luke", "Harold"]
# cities = ["Madeira", "Manchester", "Madrid", "Turin", "Riyadh"]
#
# cities.extend(people)
# print(cities)
# #Adds all the values in 'people' to the list 'cities'.
#
# cities.append("Nairobi")
# print(cities)
# #Adds 'Nairobi' to the end of the list, including the added values.
#
# cities.insert(3, "Capetown")
# print(cities)
# #Adds the new element at the third index, and pushes the former elements after index 3 one index up.
#
# cities.remove("Nairobi")
# print(cities)
# #Removes 'Nairobi' from the list.
#
# cities.pop()
# print(cities)
# #Removes the last element in the list.
#
# #cities.clear()
# #print(cities)
# #Clears the list of everything.
#
# print(cities.index("Turin"))
# #Gives the index of element 'Turin'
#
# cities.append("Nairobi")
# cities.append("Nairobi")
# print(cities.count("Nairobi"))
# #This counts how many elements are 'Nairobi'
#
# cities.sort()
# print(cities)
# #Arranges the list in alphabetical order.
#
# lucky_numbers.sort()
# print(lucky_numbers)
# #Arranges the list in ascending order.
#
# lucky_numbers.reverse()
# print(lucky_numbers)
# #Rearranges the order of this list from back to front.
#
# people2 = people.copy()
# print(people2)
# #Copies list 'people'.
#
# # Tuples
#
# coordinates = (4,5)
# print(coordinates[1])
# #Tuples are immutable. They cannot be changed/ reassigned values etc.
# #A difference between tuples and lists is tuples have parentheses while lists use square brackets.
#
# # Functions
#
# def say_hi(name, age):
#     print("Hello " + name + "!" + ", you're " + str(age))
#
# say_hi("Steph", 37)
# say_hi("Martin", 55)
#
# # Return Statement.
#
# def cube(num):
#     return num * num * num
#
# result = cube(5)
# print(result)
# #Or we can simply do print(cube(5))

# If statements

is_male = True

if is_male:
    print("\nYou are male.")
else:
    print("\nYou are female.")

is_tall = True

if is_tall or is_male:
    print("\nYou are tall, or male or both")
else:
    print("\nYou are not tall or male.")

if is_male and is_tall:
    print("\nYou are both male and tall.")
else:
    print("\nYou are either female or not tall or both.")




















