from cryptography.fernet import Fernet
import os
from datetime import datetime
import pyperclip

def log_action(action):
    with open("encrypted_file.txt", "ab") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:&M:%S")
        full_data = f"\n[{timestamp}] {action}\n"
        encoded = full_data.encode()
        encrypted = f.encrypt(encoded)
        log.write(encrypted)

def load_or_generate_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
            return key

key = load_or_generate_key()
f = Fernet(key)

print("Data encryption")
while True:
    print("Please put your data below")
    print("-" * 50)
    data = input("You: ").encode()

    encrypted = f.encrypt(data)
    decoded = encrypted.decode()

    print("Here's your encrypted data and the original data in comparison")
    print("Here is your original data: ", data.decode())
    print("Here is you encrypted data: ", decoded)
    print("-" * 50)
    print("Do you want to save this into a txt file, (C)opy or do nothing with it?\nPlease choose a number below>>")
    print("[1] Save to a file\n[2] Copy the encrypted data\n[Else] Skip and do nothing")
    choice = input("You: ")

    if choice == "1":
        with open("encrypted_file.txt", "ab") as file:
            file.write(encrypted)
            log_action("Encrypted new data")
            print("Data added to file")
            print("Please check your directory/folder for clarification.")
    elif choice == "2":
        text = pyperclip.copy(decoded)
        print("Data succesfully copied to your clipboared")
    else:
        print("Done")
        pass