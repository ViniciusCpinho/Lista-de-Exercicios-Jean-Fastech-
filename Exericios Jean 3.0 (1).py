# variaveis com os numeros de alunos e provas realizadas caso tenha alguma alteração no numero
num_aluno = 2
num_notas = 2

# vetor para armazenar as notas de cada aluno
notas = []

# variaveis de média
media = 0
melhor7 = 0

#inicio do código

for i in range(1, num_aluno + 1):
    for j in range(num_notas):
        notas.append(float(input("digite a nota do aluno " + str(i) + ': ')))
        media = media + notas[j]

for i in range(1, num_aluno + 1):
    if notas[i] >= 7:
        melhor7 += 1
        print("O números de alunos acima da media foi de {0}".format(melhor7))

#fim do código