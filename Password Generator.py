import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("*******Welcome to Password Generator******\n")
num_letters = int(input("How many letters in your password: "))
num_numbers = int(input("How many numbers in your password: "))
num_symbols = int(input("How many symbols in your password: "))

password_list = []

for i in range(1,num_letters+1):
    password_list.append(random.choice(letters))
for i in range(1,num_numbers+1):
    password_list += random.choice(numbers)
for i in range(1,num_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(f"Your password is {password} .")

