import os
import shutil

def organizar_archivos():
    ruta = entry_path.get()

    if not ruta:
        return

    for archivo in os.listdir(ruta):
        archivo_ruta = os.path.join(ruta, archivo)

        if os.path.isfile(archivo_ruta):
            extension = archivo.split(".")[-1]

            carpeta_destino = os.path.join(ruta, extension)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            shutil.move(archivo_ruta, os.path.join(carpeta_destino, archivo))

import tkinter as tk
from tkinter import filedialog, messagebox
from task_automator.core import organize_folder

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, carpeta)

def ejecutar():
    path = entry_path.get()
    if not path:
        messagebox.showerror("Error", "Selecciona una carpeta")
        return

    dry_run = var_dry.get()

    resultado = organize_folder(path, dry_run=dry_run)
    messagebox.showinfo("Resultado", str(resultado))

# Ventana principal
root = tk.Tk()
root.title("Organizador de Archivos")
root.geometry("500x400")   # tamaño ventana
root.resizable(False, False)  # no se puede cambiar tamaño

# centrar ventana
ancho = 500
alto = 400
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()

x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)

root.geometry(f"{ancho}x{alto}+{x}+{y}")

root.title("Organizador de Archivos")
root.configure(bg="#2c2f33")


# Campo de ruta
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=10)

# Botón seleccionar
btn_select = tk.Button(
    root,
    text="Seleccionar carpeta",
    command=seleccionar_carpeta,
    width=25,
    height=2,
    bg="#4CAF50",
    fg="white"
)

btn_select.pack(pady=10)

btn_organizar = tk.Button(
    root,
    text="Organizar archivos",
    command=organizar_archivos,
    width=25,
    height=2,
    bg="#7289da",
    fg="white"
)

btn_organizar.pack(pady=10)

# Checkbox dry run
var_dry = tk.BooleanVar()
chk = tk.Checkbutton(root, text="Simular (no mover archivos)", variable=var_dry)
chk.pack()

# Botón ejecutar
btn_run = tk.Button(root, text="Organizar", command=ejecutar)
btn_run.pack(pady=10)

root.mainloop()
root = tk.Tk()
root.title("Organizador de Archivos")

root.iconbitmap("243423.ico")

