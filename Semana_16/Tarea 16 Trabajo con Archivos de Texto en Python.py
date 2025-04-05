# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Esta es mi primera nota.\n")
    file.write("Aquí va la segunda línea de notas.\n")
    file.write("Finalmente, la tercera línea de mis notas.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea extras

# El uso de 'with open' maneja automáticamente el cierre de archivos
