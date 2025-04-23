import random, string, time, pyperclip, json

code = " " + string.punctuation + string.digits + string.ascii_letters
code = list(code)

user_message = ""
cipher_text = ""

history = {}

key = code.copy()
random.seed(42)
random.shuffle(key)

# SAVING---------------------------------------------------------------
def saving_encryptions(user_message, encrypted):
    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = {}

    history[user_message] = encrypted

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)
    print("saved.")

# ENCRYPT--------------------------------------------------------------
def encrypt(user_message):
    user_message = input("what would you like to encrypt: ")
    print(" ")
    cipher_text = ""

    with open("history.json", "r") as file:
        content = file.read()

    if user_message == content:
        print("--- this entry is already in the database ---")
    else:
        for letter in user_message:
            index = code.index(letter)
            cipher_text = cipher_text + key[index]

        time.sleep(1)
        print(f"encrypted text: {cipher_text}")
        print(" ")

        time.sleep(1)
        pyperclip.copy(cipher_text)
        print("text copied to clipboard.")

        saving_encryptions(user_message, cipher_text)

time.sleep(1)

# DECRYPT--------------------------------------------------------------
def decrypt(cipher_text):
    cipher_text = input("what would you like to decrypt: ")
    user_message = ""

    with open("history.json", "r") as file:
        content = file.read()

    if f"{cipher_text}" in content:
        for letter in cipher_text:
            index = key.index(letter)
            user_message += code[index]

        time.sleep(1)
        print(f"original text: {user_message}")

        time.sleep(1)
        pyperclip.copy(user_message)
        print("text copied to clipboard.")
    else:
        time.sleep(1)
        print("--- this entry does not exist in the database ---")



print("-------------------------------------------------")
print("")
print("       welcome to my encryption program          ")
print("")
print("-------------------------------------------------")
time.sleep(1)

answer = input("would you like to encrypt or decrypt? (e/d) ")
print(" ")

if answer == "e":
    encrypt(user_message)
elif answer == "d":
    decrypt(cipher_text)
else:
    print("invalid response")

print("-------------------------------------------------")
