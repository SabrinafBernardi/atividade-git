preco = {"Leite": 5, "Pão":10, "Mel": 12}
produto = str(input("Qual produto deseja alterar o preço?"))

if produto in preco:
    novo_valor = float(input("Qual o novo valor do produto?"))
    preco[produto] = novo_valor
    print("Preço atualizado")
else:
    print("Produto não encontrado")

print(preco)
