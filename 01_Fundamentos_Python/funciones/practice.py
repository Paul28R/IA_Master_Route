# funciones

# 

def operacion(num1,num2, tipo="suma"):
    if tipo == "suma":
        return num1 + num2
    elif tipo == "resta":
        return num1 - num2
    elif tipo == "div":
        return num1 / num2
    elif tipo == "mult":
        return num1 * num2
    
print(operacion(2, 7, "resta"))



def operacion(num1,num2, tipo="suma"):
    operaciones = {"resta": num1 - num2, "div": num1 / num2, 
                   "mult": num1 * num2 if num2 != 0 else
                     "Error: Division por cero"}
    return operaciones.get(tipo, "Operacion no valida")

print(operacion(2, 7, "div"))

####################################



def El_contador_de_text(**kmargs):
    

 


