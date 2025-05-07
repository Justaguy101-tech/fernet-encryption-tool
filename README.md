# Simple Fernet Encryption/Decryption Tool

This is a beginner-friendly encryption and decryption program built in Python using the `cryptography.fernet` module. It’s designed to help users securely encrypt their sensitive data and easily decrypt it later, using a consistent key.

---

## Features

- **Fernet-based encryption** for secure data handling.
- **Key generation and saving** to `key.key`.
- **Encrypt text input** and save it to a file.
- **Decrypt using two modes:**
  - **Option 1:** Decrypt from a saved encrypted file.
  - **Option 2:** Decrypt a copied/pasted encrypted string.
- **Auto-copy decrypted text** to clipboard using `pyperclip`.
- **Clean CLI interface** with clear prompts.

---

## How It Works

### Encrypter
1. Prompts the user to enter the message they want to encrypt.
2. Generates a `key.key` file if it doesn’t exist.
3. Encrypts the message using the key.
4. Saves the encrypted result to a `.txt` file.

### Decrypter
1. Loads the same `key.key` file.
2. Asks the user:
   - [1] Decrypt from a file.
   - [2] Paste an encrypted string to decrypt.
3. Decrypts the content and copies it to the clipboard.
4. Displays the decrypted message in the terminal.

---

## Requirements

Install the necessary modules using pip:
```bash
pip install cryptography pyperclip
```

---

### File structure

├── encrypter.py      # Encrypts user input
├── decrypter.py      # Decrypts from file or pasted string
├── key.key           # Key used for both encryption & decryption
├── encrypted.txt     # (Optional) Example output file
├── decrypted.txt     # (Optional) Example output file

---

## Upcoming updates

- GUI version using tkinter(planned).
- Timestamped logs stored.
- Decrypt and auto-copy from any supported filetype.
- Add error handling/logging improvments
- passoword-protected key loading

---

## Notes

- You must keep your key.key file safe - losing it means you cannot decrypt your data.
- This tool was built for learning purposes ut can be used practically with proper care.
- Inspired by rea-world cryptography concept while keeping it simple for beginners.

---

## Author

Made by a 15-year-old aspiring ethical hacker who's currently learning Python, Cryptography, and cybersecurity - one project at a time.
