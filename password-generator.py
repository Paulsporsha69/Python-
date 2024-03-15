import random

character =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []

symbol=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
print("Welcome to Password Generator!\n")
letters = int(input("How many letters would you like in password?\n"))
symbols_p = int(input("How many symbols would you like in password?\n"))
number_p = int(input("How many numbers would you like in password?\n"))
for char in range(1,letters+1):
    password +=  random.choice(character)
for char in range(1,symbols_p+1):
    password +=  random.choice(symbol)
for char in range(1,number_p+1) :
    password +=  random.choice(numbers)


print(password)

random.shuffle(password)
print("Password after shuffle")
print(password)