def ParImpar(list):
    for i in range(len(list)):
        if list[i] % 2 != 0:
            list[i] += 1
        else:
            list[i] -= 1

arreglo = [1, 4, 6, 10, 16, 19, 5, 13]
print("El arreglo antes de pasar por la funcion ParImpar:")
for n in arreglo:
    print('-', n)

ParImpar(arreglo)

print("El arreglo despues de pasar por la funcion ParImpar:")
for m in arreglo:
    print('-', m)