import os
import tkinter as tk
from tkinter import messagebox
import re


def Limpiar_Campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)


def esEnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


def esDecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def esNumerode10digitos(valor):
    return valor.isdigit() and len(valor) == 10


def esTextoValido(valor):
    return bool(re.match(r"^[a-zA-Z\s]+$", valor))


def guardar_Valores():
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    elif var_genero.get() == 3:
        genero = "Otro"

    if (esEnteroValido(edad)
        and esDecimalValido(estatura)
        and esNumerode10digitos(telefono)
        and esTextoValido(nombre)
        and esTextoValido(apellidos)):

        datos = (
            f"Nombre: {nombre}\n"
            f"Apellidos: {apellidos}\n"
            f"Edad: {edad}\n"
            f"Estatura: {estatura}\n"
            f"Teléfono: {telefono}\n"
            f"Género: {genero}\n"
        )

        carpeta = r"C:\Users\monto\Desktop\Practica04"
        os.makedirs(carpeta, exist_ok=True)

        ruta = os.path.join(carpeta, "FormularioPython.txt")

        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n")

        messagebox.showinfo(
            "Información",
            "Datos guardados con éxito:\n\n" + datos
        )

        Limpiar_Campos()

    else:
        messagebox.showerror(
            "Error",
            "Por favor, ingrese datos válidos en los campos."
        )


ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr. 01")
ventana.configure(bg="lightblue")

var_genero = tk.IntVar()


lbNombre = tk.Label(ventana, text="Nombre (s):", font=("Comic Sans MS", 13))
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:", font=("Comic Sans MS", 13))
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono:", font=("Comic Sans MS", 13))
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:", font=("Comic Sans MS", 13))
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:", font=("Comic Sans MS", 13))
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Género:", font=("Comic Sans MS", 13))
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

rbOtro = tk.Radiobutton(ventana, text="Otro", variable=var_genero, value=3)
rbOtro.pack()


btnBorrar = tk.Button(ventana, text="Borrar", command=Limpiar_Campos)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_Valores)
btnGuardar.pack()


ventana.mainloop()