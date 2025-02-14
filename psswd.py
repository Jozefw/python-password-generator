#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

psswd = ''
for letter in range(1,nr_letters+1):
    rando_char = random.choice(letters)
    psswd += rando_char
    print(psswd)

for number in range(1,nr_numbers+1):
    rando_num = random.choice(numbers)
    psswd += rando_num
    print(psswd)

for sym in range(1,nr_symbols+1):
    rando_sym = random.choice(symbols)
    psswd += rando_sym
    print(psswd)
#print(psswd)  