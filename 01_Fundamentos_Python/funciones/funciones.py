# def sumar(a, b):
#     return a + b 

# resultado = sumar(5, 3)
# print(resultado)

########################

def hello_world():
    print("Hello world!")

hello_world()

# Una funcion con 2 parametros 
def sum(num1, num2):
    print(num1 + num2)

# se llama las veces que quieras y cambias el resultado
sum(2,3)
sum(1,7)
sum(100, 3)

################## RETURN ######################
# Return devuelve un resultado
# y permite que una funcion envie un valor (o varios)
def sum(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2
    
total = sum(2)
print(total)

# *permite recibir una cantidad ilimitada como (tuple)
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")
# **kwargs permite recibir datos con nombre como un (dict)
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(fitst="Dave", last="Sara")

############# Funciones Lambda (Anonimas) 



    