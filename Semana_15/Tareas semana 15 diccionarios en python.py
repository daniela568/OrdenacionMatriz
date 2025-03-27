# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Daniela Camacho",
    "edad": 26,
    "ciudad": "Nueva Loja",
    "profesion": "Ingeniero"
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Lago Agrio"

# Agregar una nueva clave "telefono" con un número ficticio
informacion_personal["telefono"] = "123-456-789"

# Verificar si la clave "telefono" existe, si no, agregarla (ya agregada en el paso anterior)
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "986-885-568"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
