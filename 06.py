palavra = input('Digite uma palavra: ')

def contar_vogais(palavra):
    vogais = 'aeiou'
    resultado = 0
    for i in palavra:
        if i in vogais:
            resultado += 1
    return resultado
        
print(contar_vogais(palavra))