# decaclaração de variaveis globais

#função para verificar se a data é possivel
def validade(data):
    data = data.split('/')
    dia = data[0]
    dia = int(dia)
    mes = data[1]
    mes = int(mes)
    ano = data[2]
    ano = int(ano)

    if 0 < mes < 13:
        if mes == 2:
            if 0 < dia <= 28:
                return (f'A data escolhida foi dia {dia} de {meses[mes]} de {ano} ')
            elif dia == 29:
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    return (f'A data escolhida foi dia {dia} de {meses[mes]} de {ano} ')
                else:
                    return ('Null')
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if 0 < dia <= 31:
                return (f'A data escolhida foi dia {dia} de {meses[mes]} de {ano} ')
            else:
                return ('Null')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 0 < dia <= 30:
                return (f'A data escolhida foi dia {dia} de {meses[mes]} de {ano} ')
            else:
                return ('Null')
    else:
        return ('Null')

#meses
meses = [',', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

#entrada da data e verificação
datas = input('Digite uma data no formato DD/MM/AAAA: ')
print(validade(datas))



