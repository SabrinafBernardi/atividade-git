nomes = input("Digite os nomes separados por vírgulas:")
dnomes = dict.fromkeys(nomes.split(","), "0")
print(dnomes)
