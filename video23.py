#Excepciones III

#Como lanzar excepciones,
#Creacion de excepciones propias(mas adelante en el curso cuando veamos la POO)

#Creamos programa para evaluar nuestra edad con la funcion raise

def evaluaEdad(edad):
    if edad<0:
        raise TypeError("la edad introducida es incorrecta")
    elif edad<18:
        return "Eres muy joven para pasar"
    elif edad<40:
        return "Puedes pasar"
    elif edad<65:
        return "Tienes una edad justa, pasa"
    elif edad<100:
        return  "No puedes pasar, eres muy viejo"

#print(evaluaEdad(-10))

#Importar una clase para hacer la raiz de un numero

import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un numero: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorNegativeNum:
    print(ErrorNegativeNum)

print("el programa ha terminado")

#Darle un nombre al error( esto sirve para cuando mas adelante hagamos una base de datos,
#muchas veces la base se borra y ocurre una excepcion  con esto podemos solucionar algunos problemas)

# def calculaRaiz(num1):
#     if num1<0:
#         raise ValueError("El numero no puede ser negativo")
#     else:
#         return math.sqrt(num1)

# try:
#     print(calculaRaiz(op1))
# except ValueError as ErrorNegativeNum:
#     print(ErrorNegativeNum)
