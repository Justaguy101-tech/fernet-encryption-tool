from cryptography.fernet import Fernet
from datetime import datetime
import pyperclip

def log_action(action):
    with open("decrypted_file.txt", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:&M:%S")
        log.write(f"[{timestamp}] {action}\n")

with open("key.key", "rb") as file:
    key = file.read()

f = Fernet(key)

print("Do you want to decrypt your information from a\n[1] File\n[2] Your encrpyted string")

choice = input("You: ")

if choice == "1":
    print("Whats the file name? ")
    file_name = input("You: ")

    with open(file_name, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)
    encoded = decrypted.decode()
    print("Your data has been decrypted")
    with open("decrypted_file.txt", "a") as dec_file:
        log_action("New data added")
        dec_file.write(encoded)
    print("Decrypted data: ", encoded)
    print("-" * 50)
    print("Please check you directory/folder for clarification.")
    print("-" * 50)

elif choice == "2":
    print("Please insert you text or type (p) to automatically paste your recent copied text.")
    data = input("You: ").lower()

    if data == "p":
        text = pyperclip.paste()
        decrypted = f.decrypt(text)
        encoded = decrypted.decode()
        print(encoded)