matriz = [[1, 4, 2],
          [5, 7, 1],
          [8, 9, 5]]
resultado = 0
for i in range(len(matriz)):
    resultado += matriz[i][i]
print("- El resultado de la sumatoria de la diagonal principal de la matriz es:", resultado)