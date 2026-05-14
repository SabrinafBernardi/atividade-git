def kadane(lista):
    soma_atual = lista[0]
    soma_maxima = lista[0]

    for num in lista[1:]:
        soma_atual = max(num, soma_atual + num)
        soma_maxima = max(soma_maxima, soma_atual)

    return soma_maxima

numeros = [1, -5, 3, -7, 8, -90, 4]
print(kadane(numeros))