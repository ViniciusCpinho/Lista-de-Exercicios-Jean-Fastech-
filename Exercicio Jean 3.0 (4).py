import math

vetor = [1, 2, 2, 3, 5, 6, 7, 8, 9, 10]
soma = 0

for i in range(0, len(vetor), +1):
    soma = soma + math.pow(vetor[i], 2)
print(soma)
