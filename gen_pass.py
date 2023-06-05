import string
import random
import tkinter as tk
import tkinter.messagebox as message

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PassGenerator")
ventana.geometry("500x250")
ventana.resizable(0,0)

# Crear el campo de entrada
nombre = tk.Label(ventana, text = 'Number of chars for password: ')
nombre.pack()
entrada = tk.Entry(ventana)
entrada.pack()


def generate_random_string():
    x = entrada.get()
    if x.isdigit():
      x = int(entrada.get())
      acc = ""
      special_chars = ["-", "_", ".", ",", "@","%","!","(",")","?","[","]","*","+","=","#","&","$"]
      mischars =  special_chars + list(string.ascii_letters) + list(string.digits)
      
      if (x < 8 or x > 20):
            if (x < 8):
              message.showinfo("Warinig","Min size of 8 chars")
              ventana.mainloop()
            if (x > 20):
              message.showinfo("Warinig","Max size of 20 chars")
              ventana.mainloop()
      else:
          for i in range(x):
              rand = random.choice(mischars)
              acc += rand
          
      if any(char in acc for char in special_chars) and any(char in acc for char in list(string.ascii_uppercase)) and any(char in acc for char in list(string.digits)):
          LB = tk.Entry(ventana,bd=0)
          LB.insert(0, acc)
          LB.config(state="readonly")
          LB.pack()

      else:
          generate_random_string()
    else:
      message.showinfo("Warinig","Enter a digit please.")
      ventana.mainloop()
        
        
# Crear un botón
boton = tk.Button(ventana, text="Generate new password", command=generate_random_string)
boton.pack()

ventana.mainloop()
