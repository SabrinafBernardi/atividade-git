def permutacoes(lista):
    # caso base
    if len(lista) == 0:
        return [[]]

    resultado = []

    for i in range(len(lista)):
        atual = lista[i]
        resto = lista[:i] + lista[i+1:]

        for p in permutacoes(resto):
            resultado.append([atual] + p)

    return resultado
numeros = [1, 2, 3]

print(permutacoes(numeros))