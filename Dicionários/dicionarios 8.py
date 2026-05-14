alunos =  {"Ana": 10, "Beatriz": 8, "Carlos": 6}
nome = input("Qual o nome do aluno?")
aluno = alunos.get(nome, "Aluno não cadastrado")
print(aluno)