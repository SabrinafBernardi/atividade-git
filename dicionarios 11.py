usuarios = {"Ana": 22, "Pedro": 30, "Maria": 31}

while True:
    print("\n=================MENU INICIAL=================")
    print("0 - Sair")
    print("1 - Ver nomes dos usuários")
    print("2 - Ver idades dos usuários")
    print("3 - Ver todos os usuários")
    print("4 - Buscar usuário")
    print("5 - Cadastrar novo usuário")
    print("6 - Remover usuário")
    print("7 - Remover último usuário")
    print("8 - Copiar e alterar dicionário")
    print("9 - Adicionar usuários por nomes")
    print("10 - Limpar todos os dados")
    print("11 - Cadastrar usuários via tuplas")
    print("=========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o programa. Até logo!")
        break

    elif opcao == "1":
        chaves = usuarios.keys()
        print("Nomes:", chaves)

    elif opcao == "2":
        valores = usuarios.values()
        print("Idades:", valores)

    elif opcao == "3":
        print("Usuários:", usuarios)

    elif opcao == "4":
        op4 = input("Qual usuário está buscando? ")
        buscar = usuarios.get(op4, "Usuário não cadastrado")
        print(buscar)

    elif opcao == "5":
        nome = input("Digite o nome a ser cadastrado: ")
        idade = int(input("Digite a idade do usuário: "))
        usuarios[nome] = idade
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    elif opcao == "6":
        nome = input("Qual usuário deseja remover? ")
        resultado = usuarios.pop(nome, "Usuário não encontrado")
        print(resultado if resultado == "Usuário não encontrado" else f"'{nome}' removido com sucesso!")

    elif opcao == "7":
        if usuarios:
            removido = usuarios.popitem()
            print(f"Usuário removido: {removido}")
        else:
            print("Dicionário vazio, nenhum usuário para remover.")

    elif opcao == "8":
        copia = usuarios.copy()
        nome = input("Digite o nome a ser alterado na cópia: ")
        idade = int(input("Digite a nova idade: "))
        copia[nome] = idade
        print("Cópia:", copia)
        print("Original:", usuarios)

    elif opcao == "9":
        op9 = input("Digite os nomes separados por vírgulas: ")
        usuarios2 = dict.fromkeys(op9.split(","), "18")
        usuarios.update(usuarios2)
        print("Dicionário atualizado:", usuarios)

    elif opcao == "10":
        confirmacao = input("Tem certeza? Isso apagará todos os dados! (S/N): ")
        if confirmacao == "S":
            usuarios.clear()
            print("Dicionário limpo:", usuarios)

    elif opcao == "11":
        quantidade = int(input("Quantas tuplas deseja informar? "))
        lista_tuplas = []
        for i in range(quantidade):
            nome = input(f"Digite o nome {i + 1}: ")
            idade = int(input(f"Digite a idade {i + 1}: "))
            lista_tuplas.append((nome, idade))
        usuarios2 = dict(lista_tuplas)
        print("Novo dicionário:", usuarios2)
        usuarios.update(usuarios2)
        print("Dicionário atualizado:", usuarios)

    else:
        print("Opção inválida! Tente novamente.")