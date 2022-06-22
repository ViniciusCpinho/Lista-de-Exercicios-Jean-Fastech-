def teste_de_DNA_do_ratinho(num):
    if num > 0:
        return ('P')
    else:
        return ('N')

num = float(input('Digite um numero qualquer: '))
print(f'Esse numero é: {teste_de_DNA_do_ratinho(num)}')