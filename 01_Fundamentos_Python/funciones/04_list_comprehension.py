# list_comprehension = = ['expresion' for 'elemento' in 'iterable']

def contraseña(password):
    
    if len(password) < 8:
        return False
    

    # Aqui esta la magia 
    return any(caracter.isupper() for caracter in password) and\
            any(caracter.isdigit() for caracter in password)

print(contraseña("abc1234"))
print(contraseña("abc123456"))
print(contraseña("Abc12345"))
print(contraseña("Abcdefghy"))


def contraseña(password):
    return (len(password) >= 8 and any(caracter.isupper() for caracter in password) and\
            any(caracter.isdigit() for caracter in password))

print(contraseña("abc1234"))
print(contraseña("abc123456"))
print(contraseña("Abc12345"))
print(contraseña("Abcdefghy"))