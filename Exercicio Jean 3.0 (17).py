def Quarteto_Magico(linha, coluna):
    if linha > 20:
        linha  = 20
    elif linha < 1:
        linha = 1

    if coluna > 20:
        coluna = 20
    elif coluna < 1:
        coluna = 1

    return ''

linha = int(input('Digite um valor inteiro para a linha da matriz: '))
coluna = int(input('Digite um valor inteiro para a coluna da matriz: '))

for x in range(linha):
    if x == 0 or x == linha - 1:
        print ('+' + ('-' * (coluna - 2)) + '+')
    else:
        print ('|' + ('-' * (coluna - 2)) + '|')

print(Quarteto_Magico(linha, coluna))

