nome = input("Digite o nome do aluno:\n")

with open("dados/nomes.txt", "a") as f:
    f.write(f"{nome}\n")