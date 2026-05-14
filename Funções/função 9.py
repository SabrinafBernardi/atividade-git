def mostrar_dados(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")

mostrar_dados(nome= "Sabrina", idade= 21, cidade="Curitiba")