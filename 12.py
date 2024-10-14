x = float(input('Digite um valor em celsius: '))
y = float(input('Digite um valor em Fahrenheit: '))

def converter(x,y):
    celsius = float(x * 1.8) + 32
    print(f'{celsius:.2f} fahrenheit')
    fahrenheit = float(y - 32) / 1.8
    print(f'{fahrenheit:.2f} celsius')

converter(x, y)
