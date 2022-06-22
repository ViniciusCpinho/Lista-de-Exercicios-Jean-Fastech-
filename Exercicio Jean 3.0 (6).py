linha1 = input('digite a frase a ser analizada: ')
linha2 = input('digite a segunda frase a ser analizada: ')

if len(linha1) == len(linha2) and linha1 == linha2:
    print("as duas string são de mesmo tamanho e possuem o mesmo conteudo: ")

elif len(linha1) == len(linha2) and linha1 != linha2:
    print("as string possuem mesmo tamanho e diferentes conteudos: ")

else:
    print("as strings possuem tamanho e conteudos diferentes: ")
