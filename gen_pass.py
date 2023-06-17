import string
import random
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
from cryptography.fernet import Fernet
import base64

# Create the main window
window = tk.Tk()
window.title("PassGenerator")
window.geometry("500x400")
window.resizable(0, 0)

# Create the input field for password length
name = tk.Label(window, text='Number of chars for password:')
name.pack()
entrada_1 = tk.Entry(window)
entrada_1.pack()

# Generate random password
def generate_random_string():
    x = entrada_1.get()
    if x.isdigit():
        x = int(x)
        acc = ""

        char_list = [chr(i) for i in range(32, 127)]
        special_chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                         '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        if x < 8 or x > 20:
            if x < 8:
                messagebox.showinfo("Warning", "Min size of 8 chars")
            if x > 20:
                messagebox.showinfo("Warning", "Max size of 20 chars")
        else:
            while True:
                acc = ""
                while len(acc) < x:
                    rand = random.choice(char_list)
                    acc += rand

                if any(char in acc for char in special_chars) and \
                        any(char in acc for char in string.ascii_uppercase) and \
                        any(char in acc for char in string.digits):
                    break

            # Show password in a dialog
            password_dialog = simpledialog.askstring("Generated Password", "Password:", parent=window,
                                                     initialvalue=acc)
            if password_dialog:
                window.clipboard_clear()
                window.clipboard_append(password_dialog)
                window.update()

    else:
        messagebox.showinfo("Warning", "Enter a digit please.")

# Generate Fernet key
def generate_fernet_key():
    charset = [chr(i) for i in range(32, 128)]
    key = ''.join(random.choice(charset) for _ in range(32))  # Fernet key length is 32
    key_dialog = simpledialog.askstring("Generated Fernet Key", "Fernet Key:", parent=window,
                                        initialvalue=base64.urlsafe_b64encode(key.encode()).decode())
    if key_dialog:
        window.clipboard_clear()
        window.clipboard_append(key_dialog)
        window.update()

# Encrypt password
def encrypt_password():
    key = entrada_2.get()
    password = entrada_3.get()
    if not key:
        messagebox.showinfo("Error", "Please enter a key to encrypt.")
        return
    if not password:
        messagebox.showinfo("Error", "Please enter a password to encrypt.")
        return
    try:
        fernet = Fernet(key.encode())
        encrypted_password = fernet.encrypt(password.encode())
        encrypted_password_dialog = simpledialog.askstring("Encrypted Password", "Encrypted Password:",
                                                           parent=window,
                                                           initialvalue=base64.urlsafe_b64encode(
                                                               encrypted_password).decode())
        if encrypted_password_dialog:
            window.clipboard_clear()
            window.clipboard_append(encrypted_password_dialog)
            window.update()
    except ValueError:
        messagebox.showinfo("Error", "Invalid key or password.")

# Decrypt password
def decrypt_password():
    key = entrada_4.get()
    encrypted_password = entrada_5.get()
    if not key:
        messagebox.showinfo("Error", "Please enter a key to decrypt.")
        return
    if not encrypted_password:
        messagebox.showinfo("Error", "Please enter an encrypted password to decrypt.")
        return
    try:
        fernet = Fernet(key.encode())
        decrypted_password = fernet.decrypt(base64.urlsafe_b64decode(encrypted_password)).decode()
        decrypted_password_dialog = simpledialog.askstring("Decrypted Password", "Decrypted Password:",
                                                           parent=window,
                                                           initialvalue=decrypted_password)
        if decrypted_password_dialog:
            window.clipboard_clear()
            window.clipboard_append(decrypted_password_dialog)
            window.update()
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt password. Invalid key or encrypted password.")

# Generate random password button
btn_generate_password = tk.Button(window, text="Generate New Password", command=generate_random_string)
btn_generate_password.pack()

# Generate Fernet key button
btn_generate_key = tk.Button(window, text="Generate Fernet Key", command=generate_fernet_key)
btn_generate_key.pack()

# Create the input field for key to encrypt
name = tk.Label(window, text='Add Key to Encrypt:')
name.pack()
entrada_2 = tk.Entry(window)
entrada_2.pack()

# Create the input field for password to encrypt
name = tk.Label(window, text='Add Password to Encrypt:')
name.pack()
entrada_3 = tk.Entry(window)
entrada_3.pack()

# Encrypt password button
btn_encrypt_password = tk.Button(window, text="Encrypt Password", command=encrypt_password)
btn_encrypt_password.pack()

# Create the input field for key to decrypt
name = tk.Label(window, text='Add Key to Decrypt:')
name.pack()
entrada_4 = tk.Entry(window)
entrada_4.pack()

# Create the input field for password to decrypt
name = tk.Label(window, text='Add Password to Decrypt:')
name.pack()
entrada_5 = tk.Entry(window)
entrada_5.pack()

# Decrypt password button
btn_decrypt_password = tk.Button(window, text="Decrypt Password", command=decrypt_password)
btn_decrypt_password.pack()

window.mainloop()
