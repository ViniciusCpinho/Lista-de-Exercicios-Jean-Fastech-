# vetor que recebe os numeros
vetnum = []

# variaveis responsaveis auxiliar nas operações.
soma = 0
multi = 1

for i in range(5):
    numeros = int(input("digite um numero "))
    vetnum.append(numeros)
    soma = vetnum[i] + soma
    multi = vetnum[i] * multi

print("Os números escolhidos foram ")

for i in range(5):
    print(vetnum[i])

print("A soma deles é de "
      + str(soma) + ","
      + " a multiplicação entre eles resulta "
      + str(multi))
