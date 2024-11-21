import tkinter as tk
from tkinter import messagebox

#Ventana de registro
def abrir_ventana_registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de Usuarios")
    ventana_registro.geometry("300x200")

#Campos para el registro
    label_usuario_registro = tk.Label(ventana_registro, text="Nuevo Usuario:")
    label_usuario_registro.grid(row=0, column=0, padx=10, pady=10)
    entry_usuario_registro = tk.Entry(ventana_registro)
    entry_usuario_registro.grid(row=0, column=1, padx=10, pady=10)

    label_contrasena_registro = tk.Label(ventana_registro, text="Nueva Contraseña:")
    label_contrasena_registro.grid(row=1, column=0, padx=10, pady=10)
    entry_contrasena_registro = tk.Entry(ventana_registro, show="*")
    entry_contrasena_registro.grid(row=1, column=1, padx=10, pady=10)

#Funcion para registrar usuarios
    def registrar_usuario():
        usuario = entry_usuario_registro.get()
        contrasena = entry_contrasena_registro.get()

        if usuario == "" or contrasena == "":
            messagebox.showerror("Error", "Por favor complete los campos.")
        else:
            messagebox.showinfo("Bienvenido al grupo", f"Usuario {usuario} registrado exitosamente.")

#Boton para registrar
    boton_registrar = tk.Button(ventana_registro, text="Registrar Usuario", bg="green", fg="white", command=registrar_usuario)
    boton_registrar.grid(row=2, column=0, columnspan=2, pady=10)

