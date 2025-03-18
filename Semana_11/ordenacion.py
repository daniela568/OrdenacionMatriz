def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz


# Matriz 3x3 de ejemplo
matriz = [
    [34, 12, 25],
    [88, 45, 67],
    [91, 42, 78]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar fila a ordenar
fila_a_ordenar = int(input("Ingresa el número de la fila a ordenar (0-2): "))

# Ordenar la fila especificada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
