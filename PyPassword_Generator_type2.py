#hardVersion
#Generate the password doesn't follow any pattern.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#taking input from the user
k_letters = int(input("How many letters would you like to print in your password? "))
k_symbols = int(input("How many symbols would you like? "))
k_numbers = int(input("How many numbers would you like? "))

password = ""

for char in range(1, k_letters+1):
    password += random.choice(letters)
for symb in range(1, k_symbols+1):
    password += random.choice(symbols)
for numb in range(1, k_numbers+1):
    password += random.choice(numbers)

shuffled_password = random.sample(password, len(password))
print(password)
# random.shuffle(password)
print(shuffled_password)



# new_password = random.shuffle(password)

# print(new_password)

