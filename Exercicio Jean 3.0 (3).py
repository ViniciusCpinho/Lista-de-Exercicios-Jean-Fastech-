
idade = []
altura = []

for i in range(2):
    ide = int(input('digite a idade da pessoa '))
    alt = float(input('digite a altura da pessoa '))
    idade.append(ide)
    altura.append(alt)

idade.reverse()
altura.reverse()
print(altura)
print(idade)

