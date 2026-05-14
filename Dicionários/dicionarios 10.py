produtos = {"Leite": 5, "Pão": 7, "Mel": 12}
remover = input("Qual item deseja remover?")
produtos.pop(remover)
adicionar = input("Qual item deseja adiconar?")
valor = input("Qual o valor do item?")
produtos.update({adicionar:valor})
print(produtos)


