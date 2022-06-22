from random import randint
def print_matriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i])
def criar_matriz(matriz, nome):
    coluna = int(input(f'Quantas colunas terá a matriz {nome}: '))
    linha = int(input(f'Quantas linhas terá a matriz {nome}: '))

    for i in range(linha):
        lista = []
        for e in range(coluna):
            lista.append(randint(1,9))
        matriz.append(lista)

a = b = []
criar_matriz(a, "A")
criar_matriz(b, "B")
print('Matriz A: ')
print_matriz(a)
print('Matriz B: ')
print_matriz(b)

c = []
if len(a) == len(b) and len(a[1]) == len(b[1]):
    for i in range(len(a[1])):
        multi = []
        for e in range(len(a)):
            multi.append(a[i][e] * b[i][e])
        c.append(multi)
    print('Matriz C')
    print_matriz(c)
