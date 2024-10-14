email = input('Digite seu email: ')

def func(email):
    return '@' in email
    
func(email)

if func(email):
    print('VALIDO')
else:
    print('INVALIDO')