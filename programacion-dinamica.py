def mochila_programacion_dinamica():
    # Ingrese la cantidad de objetos y capacidad
    n = int(input("Ingrese la cantidad de objetos: "))
    capacidad = int(input("Ingrese la capacidad de la mochila: "))
    
    pesos = [0] * n
    valores = [0] * n
# Ingrese pesos y valores
    for i in range(n):
        pesos[i] = int(input(f"Ingrese el peso del objeto {i + 1}: "))
        valores[i] = int(input(f"Ingrese el valor del objeto {i + 1}: "))