import json
import tkinter as tk
from tkinter import filedialog

# Función para abrir y convertir el archivo .txt a .json
def convertir_txt_a_json():
    # Abrir diálogo para seleccionar el archivo .txt
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

    if not file_path:
        print("No se seleccionó ningún archivo.")
        return

    # Leer el contenido del archivo .txt
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Procesar cada línea y formatear como se requiere
    palabras = []
    for line in lines:
        palabra = line.strip()  # Eliminar espacios en blanco al inicio y final
        palabras.append(palabra)

    # Generar el formato JSON
    json_data = json.dumps(palabras, indent=4, ensure_ascii=False)

    # Guardar el resultado en un archivo .json
    with open('resultado.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print("Archivo JSON generado correctamente.")

# Ejecutar la función para convertir el archivo
convertir_txt_a_json()
