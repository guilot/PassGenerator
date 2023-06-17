# PassGenerator
I was bored, so I created a simple password generator that creates random passwords from 8 to 20 characters, including all security minimum requirements and special characters that you could find on any website or service that requires a strong password.

As especial character you may find: "-", "_", ".", ",", "@","%","!","(",")","?","[","]","*","+","=","#","&","$"

Don't forget to save the password somewhere else; once you close the program, you cannot get it back.

To use it just go to dist/gen_pass.exe and execute it.

It's recommended anyway to actually download it completed and create the .exe by using the pyinstaller: 

pyinstaller --onefile -w gen_pass.py. 

Otherwise (as normal), Windows defense could detect it as a dangerous program.
