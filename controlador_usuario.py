def autenticar(login, senha):
    usuario = [
    {
        "username": "teste",
        "password": "admin"
    },
    {
        "username": "teste2",
        "password": "admin2"
    },
    {
        "username": "teste3",
        "password": "admin3"
    },
    {
        "username": "teste4",
        "password": "admin4"
    },
    ]
    for usuario in usuario:
        if usuario["username"] == login and usuario["password"] == senha:
            print('AUTENTICADO')
            return
        print('USUARIO OU SENHA INCORRETO')