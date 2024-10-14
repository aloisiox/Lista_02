print('-----CALCULADORA-----')
numero = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
operacao = input("Digite a operação (+, -, *, /): ")

def calcular(numero, numero2, operacao):
       if operacao == '+':
              return numero + numero2
       elif operacao == '-':
              return numero - numero2
       elif operacao == '*':
              return numero * numero2
       elif operacao == '/':
              return numero / numero2
    
print(calcular(numero, numero2, operacao))







