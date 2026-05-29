# Hard Level
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = list(alphabet) + list(alphabet.upper())
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password = []

for i in range(nr_letters):
    letter = random.choice(letters)
    password.append(letter)

for i in range(nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

for i in range(nr_numbers):
    number = random.choice(numbers)
    password.append(number)

random.shuffle(password)
print(f"Your password is: {''.join(password)}")
