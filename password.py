import random

print("Welcome to the Pypassword Generator")
num=['1','2','3','4','5','6','7','8','9','0']
alph=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
symb=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','?','/','>','<',']']

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

password = ''
for _ in range(letters):
    password += random.choice(alph)
for _ in range(numbers):
    password += random.choice(num)
for _ in range(symbols):
    password += random.choice(symb)

# Shuffle the password characters to make it more random
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Generated Password:", password)
