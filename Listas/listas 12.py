numeros = [1, 2, 3, 4, 5]
maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    elif  num < menor:
        menor = num

print("O maior número é", maior)
print("O menor número é", menor)