#crear usuario unico

list_of_usernames = []


def createUsername(first, last, list_of_usernames):
    first = input('Ingresa tu nombre')
    last = input('Ingresa tu apellido')
    username = first+last
    if username in list_of_usernames:
        return "Ese nombre ya esta en uso"
    else:
        return "Ahora ingresa tu email " + createUsername

createUsername('Jhon', 'Doe', list_of_usernames)


def register(createUsername):
    email = input('email@example.com')
    email_confirmation = input('email@example.com')
    while True:
        if email == email_confirmation:
            return 'Ahora escribe tu clave'
            break
        else:
         return 'Los emails no coinciden'

        password.hash = input('Ingresa tu clave')
        password_confirmation.hash = input('Ingresa de nuevo tu clave')
    while True:
        if password == password_confirmation:
            return "Bienvenido "+ createUsername
            break
        else:
            return 'Las claves no coinciden'


