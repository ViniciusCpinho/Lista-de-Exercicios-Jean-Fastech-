A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
MatrizC = [[0, 0], [0, 0]]

#for para colocar dados na primeira matriz

for l in range(0, 2):
    for c in range(0, 2):
        A[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-=" * 30)

#for para colocar dados na segunda matriz

for l in range(0, 2):
    for c in range(0, 2):
        B[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-=" * 30)

#2 for para mostrar as matrizes A e B, *uma matriz em cada!!

print('Matriz [A]')
print()

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{A[l][c]:^5}]', end='')
    print()

print()
print('Matriz [B]')
print()

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{B[l][c]:^5}]', end='')
    print()
print("-=" * 30)

#for para a soma das matrizes A e B

print('Matriz [C]')
for l in range(0, 2):
    for c in range(0, 2):
        MatrizC[l][c] = A[l][c] + B[l][c]
        print(f'[{MatrizC[l][c]:^5}]', end='')
    print()
print('-=' * 30)