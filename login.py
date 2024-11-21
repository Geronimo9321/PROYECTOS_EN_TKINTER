import tkinter as tk
from tkinter import messagebox
from ventana_registro import abrir_ventana_registro

#Verifico las credenciales
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    #Credencial de ejempo
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Bienvenido", "Inicio de sesíon exitoso")
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

#Ventana principal
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("300x250")

#Mensaje de Bienvenida
label_bienvenida = tk.Label(ventana, text="Bienvenidos a mi App", font=("Arial", 14))
label_bienvenida.grid(row=0, column=0, columnspan=2, pady=20)

#Elementos de la interfaz
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=1, column=1, padx=10, pady=5)

label_contrasena = tk.Label(ventana, text="Contraseña:")
label_contrasena.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.grid(row=2, column=1, padx=10, pady=5)

#Boton de iniciar sesión + registro
boton_iniciar_sesion = tk.Button(ventana, text="Inicar sesión", command=verificar_credenciales, bg="green", fg="white")
boton_iniciar_sesion.grid(row=3, column=0, padx=10, pady=10, sticky="w")

boton_registrarse = tk.Button(ventana, text="Registrarse", bg="blue", fg="white", command=abrir_ventana_registro)
boton_registrarse.grid(row=3, column=1, padx=10, pady=10, sticky="e")

ventana.mainloop()