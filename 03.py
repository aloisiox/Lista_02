print('-----CALCULADORA-----')
escolha = int(input('Selecione sua operação: \n 1-Soma \n 2-Subtração \n 3-Divisão \n 4-Multiplicação \n'))
numero = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))


def soma(numero, numero2):
    if escolha == 1:
        print(numero + numero2)

soma(numero,numero2)


def sub(numero, numero2):
    if escolha == 2:
        print(numero - numero2)

sub(numero, numero2)

def div(numero, numero2):
    if escolha == 3:
        print(numero / numero2)

div(numero, numero2)

def mult(numero, numero2):
    if escolha == 4:
        print(numero * numero2)

mult(numero, numero2)


