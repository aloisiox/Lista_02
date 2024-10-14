palavra = input('Contagem de palavras: ')

def contar_palavras(palavra):
    contar = palavra.split()
    return len (contar)

print(contar_palavras(palavra))