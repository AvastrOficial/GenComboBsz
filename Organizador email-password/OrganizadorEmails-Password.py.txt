import tkinter as tk
from tkinter import filedialog

# Función para verificar si una línea es válida (tiene ambos, email y password)
def is_valid_line(line):
    parts = line.split(":")
    return len(parts) == 2 and all(parts)

# Función para procesar el archivo seleccionado
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    valid_lines = set()
    invalid_lines = set()

    for line in lines:
        line = line.strip()
        if is_valid_line(line):
            email, password = line.split(":")
            if email.count('@') == 1 and email.split('@')[0] != '':
                valid_lines.add(line)
            else:
                invalid_lines.add(line)
        else:
            invalid_lines.add(line)

    with open("correos_completos.txt", "w") as complete_file:
        for line in valid_lines:
            complete_file.write(line + "\n")

    with open("correos_incompletos.txt", "w") as incomplete_file:
        for line in invalid_lines:
            incomplete_file.write(line + "\n")

    print("Correos completos guardados en 'correos_completos.txt'")
    print("Correos incompletos guardados en 'correos_incompletos.txt'")

# Función para abrir el diálogo de selección de archivos
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        process_file(file_path)

# Ejecutar la función de selección de archivos
open_file_dialog()
