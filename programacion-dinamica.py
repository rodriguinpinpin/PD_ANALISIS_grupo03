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
# Crear matriz dp inicializada en 0
dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
# Construir la tabla dp
for i in range(1, n + 1):
    for j in range(1, capacidad + 1):
        # El objeto actual en las listas indexadas en 0 es pesos[i-1]
        if pesos[i - 1] <= j:
            incluir = valores[i - 1] + dp[i - 1][j - pesos[i - 1]]
            if incluir > dp[i - 1][j]:
                dp[i][j] = incluir
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
            