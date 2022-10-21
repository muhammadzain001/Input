# input function which will allow you to make your programs get
# and use input from a user.

name = input("Please enter your name:")

print("Your name is " + name + ".")

print(type(name))

# no matter what the input function is given as an input.
# It always gives back a string.

fav_num = input("What is your favorite number?")

print("Your favorite number is " + fav_num + "." + " " + "And your name is " + name + ".")

# Exercise

name1 = input("What is your name?")
quest = input("Whats ur quest?")
color = input("What is your favorite color?")

print("So your name is " + name1 +",your quest is " + quest + ",and your favorite color is " + color)

# int() and float()

user_int = int(input("Please enter an integer"))
print(user_int)
print(type(user_int))

user_int1 = float(input("Please enter a float"))
print(user_int1)
print(type(user_int1))