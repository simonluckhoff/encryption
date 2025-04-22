import random
import string
import time

code = " " + string.punctuation + string.digits + string.ascii_letters
code = list(code)

user_message = ""
cipher_text = ""  

key = code.copy()  
random.shuffle(key)

# ENCRYPT--------------------------------------------------------------
def encrypt(user_message):
    user_message = input("what would you like to encrypt: ")
    cipher_text = ""

    for letter in user_message:
        index = code.index(letter)
        # cipher_text += key[index]
        # the actual concatenating side of it. 
        cipher_text = cipher_text + key[index]

    time.sleep(1)
    # print(f"original text: {user_message}")
    print(f"encrypted text: {cipher_text}")

time.sleep(1)

# DECRYPT--------------------------------------------------------------
def decrypt(cipher_text):
    cipher_text = input("what would you like to decrypt: ")
    user_message = ""

    for letter in cipher_text:
        # refers to copied list, because that list stays the same, smart. 
        index = key.index(letter) 
        user_message += code[index]

    time.sleep(1)
    print(f"original text: {user_message}")
    # print(f"encrypted text: {cipher_text}")


print("-------------------------------------------------")
print("       welcome to my encryption program          ")
print("-------------------------------------------------")
time.sleep(1)

encrypt(user_message)

print("-------------------------------------------------")
time.sleep(1)

decrypt(cipher_text)

print("-------------------------------------------------")
