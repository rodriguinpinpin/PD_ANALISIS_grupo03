def mochila_programacion_dinamica():
    # Ingrese la cantidad de objetos y capacidad
    n = int(input("Ingrese la cantidad de objetos: "))
    capacidad = int(input("Ingrese la capacidad de la mochila: "))
    
    pesos = [0] * n
    valores = [0] * n