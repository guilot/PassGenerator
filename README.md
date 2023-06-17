# PASSGENERATOR
I was bored, so I created a simple password generator that creates random passwords from 8 to 20 characters, including all security minimum requirements and special characters that you could find on any website or service that requires a strong password.

As especial character you may find: ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/','\\', ']', '^', '_', '`', '{', '|', '}', '~', '['

Don't forget to save the password somewhere else; once you close the program, you cannot get it back.

To use it just go to dist/gen_pass.exe and execute it.

It's recommended anyway to actually download it completed and create the .exe by using the pyinstaller: 

pyinstaller --onefile -w gen_pass.py. 

Otherwise (as normal), Windows defense could detect it as a dangerous program.

# New Functionality: 

I have added a way to encrypt and decrypt the passwords you generate. It didn't seem very safe to me to just write the password in a note.

So, now you generate a password as before, then create a Fernet key to encrypt and decrypt, and with this, you create the encrypted password that will reveal the wanted one by using it with the key you generated before.

I recommend that you just generate a Fernet key and use it with all your passwords. Then, save in one document the key and the encrypted ones, and hope that no one finds and uses the program to reveal them.

'It's not much, but it's honest work.'
