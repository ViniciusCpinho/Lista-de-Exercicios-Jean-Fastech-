matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

#O for abaixo é para realizar a entrada de dados dentro da matriz

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-=" * 30)

#O for abaixo é um print da matriz com o valores digitados acima

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-=" * 30)

# k é o numero que irá multiplicar a linha principal da matriz

k =int(input('Digite um valor para multiplicar a diagonal principal da matriz: '))
print('-=' * 30)

# For para trocar os valores antigos para os novos valores

for i in range(0,3):
    matriz[i][i] = matriz[i][i] * k

# for para dar print de como está a nova matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
