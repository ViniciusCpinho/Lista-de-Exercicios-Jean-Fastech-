nome = str(input("digite o nome do usuario: "))
nome = nome.upper()
n = ""
for i in range(len(nome)):
    n = n + nome[i]
    print(n)