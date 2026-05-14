dados = {"Nome": "Sabrina", "Idade":21, "Sexo":"Feminino"}
apagar = str(input("Deseja apagar todos os dados? S/N"))
if apagar == "S":
    dados.clear()
    print(dados)
else:
    print("OK")
    print(dados)