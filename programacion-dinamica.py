def mochila_programacion_dinamica():
    print("========================================")
    print("   MOCHILA: PROGRAMACIÓN DINÁMICA      ")
    print("========================================\n")
    
    n = int(input("Ingrese la cantidad de objetos: "))
    capacidad = int(input("Ingrese la capacidad de la mochila: "))
    
    pesos = [0] * n
    valores = [0] * n

    for i in range(n):
        pesos[i] = int(input(f"Ingrese el peso del objeto {i + 1}: "))
        valores[i] = int(input(f"Ingrese el valor del objeto {i + 1}: "))

    # Crear matriz dp inicializada en 0
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    
    # Construir la tabla dp
    for i in range(1, n + 1):
        for j in range(1, capacidad + 1):
            if pesos[i - 1] <= j:
                incluir = valores[i - 1] + dp[i - 1][j - pesos[i - 1]]
                if incluir > dp[i - 1][j]:
                    dp[i][j] = incluir
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # --- NUEVA PARTE: IMPRIMIR LA MATRIZ DP ---
    print("\n========================================")
    print("      MATRIZ DE DECISIONES (DP)         ")
    print("========================================")
    
    # Imprimir encabezado de capacidades (Columnas)
    print("Capacidad: ", end="")
    for j in range(capacidad + 1):
        print(f"[{j}]".rjust(5), end="")
    print("\n" + "-" * (12 + (capacidad + 1) * 5))
    
    # Imprimir filas de la matriz
    for i in range(n + 1):
        if i == 0:
            print("Obj Base:  ", end="")
        else:
            print(f"Objeto {i}:  ", end="")
            
        for j in range(capacidad + 1):
            print(str(dp[i][j]).rjust(5), end="")
        print()
    # ------------------------------------------

    # Mostrar resultados finales
    print("\n================================")
    print("RESULTADO FINAL")
    print("================================")
    print(f"Valor máximo obtenido: {dp[n][capacidad]}")

# Ejecutar función
if __name__ == "__main__":
    mochila_programacion_dinamica()