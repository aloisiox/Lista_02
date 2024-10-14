def fatorial(numero):
    n = 1
    for i in range(numero, 0, -1):
        n = n * i
    return n

numero = int(input('Digite um numero inteiro nao-negativo: '))
if numero > 0:
    print(f'O fatorial de {numero} é {fatorial(numero)}')
else:
    print('ERRO, O NUMERO DEVE SER POSITIVO!!')

        
