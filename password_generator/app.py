'''
Copyright © 2022 AzizbekDeveloper
https://www.azizbekdeveloper.herokuapp.com/ - Website
https://www.instagram.com/azizbekdeveloper/ - Instagram
'''
import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
	length = int(input("Enter password length: "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	return "".join(password)

print(generate_random_password())