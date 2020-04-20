import random
import string

size = int(input("Please enter the length for the password: "))
password_chars = string.ascii_letters + string.digits + string.punctuation
generated_pass = ""
for i in range(size):
    generated_pass += random.choice(password_chars)
print("Random password : " + generated_pass)
