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

    # Procesar cada línea y extraer solo las contraseñas y los tags de nombres
    passwords = []
    tags = []
    for line in lines:
        if ':' in line:  # Verificar que la línea contenga ':'
            email, password = line.strip().split(':', 1)
            tagname = email.split('@')[0]
            passwords.append(password.strip())
            tags.append(tagname.strip())

    # Generar el formato JSON para las contraseñas
    json_passwords = json.dumps(passwords, indent=4, ensure_ascii=False)
    # Guardar las contraseñas en un archivo .json
    with open('passwords.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_passwords)

    # Generar el formato JSON para los tags de nombres
    json_tags = json.dumps(tags, indent=4, ensure_ascii=False)
    # Guardar los tags de nombres en un archivo .json
    with open('usernames.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_tags)

    print("Archivos JSON generados correctamente.")

# Ejecutar la función para convertir el archivo
convertir_txt_a_json()
