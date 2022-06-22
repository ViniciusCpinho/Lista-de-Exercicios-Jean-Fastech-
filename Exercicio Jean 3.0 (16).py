def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto/100) * custo

taxa = float(input('Digite o imposto a ser aplicado no produto: '))
custo = float(input('Digite o valor do custo do produto: '))

print(f'O valor do produto com o imposto é de : {somaImposto(taxa, custo)}')
