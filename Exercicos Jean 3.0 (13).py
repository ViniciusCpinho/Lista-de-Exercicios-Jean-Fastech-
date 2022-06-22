def escada(num):
    for i in range(num):
        i += 1
        print(str(i) * i)

num = int(input('Digite um numero inteiro qualquer: '))
escada(num)