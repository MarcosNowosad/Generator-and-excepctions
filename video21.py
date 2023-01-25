#Exceptiones I
# ¿QUE ES? son errores  que ocurren durante la ejecucion del programa.
#La sintaxis del codigo  es correcta pero durante la ejecucion ha ocurrido "Algo inesperado"

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2

    except ZeroDivisionError:
        print("No se puede dividir entre 0 ")
        return "Operacion Erronea"

op1 = (int(input("Introduce el primer número: ")))

op2 = (int(input("Introduce el segundo número: ")))

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")

#RESULTADO
#   File "C:\Users\marco\Desktop\Curse-python\video21.py", line 18, in divide
#     return num1 / num2
#            ~~~~~^~~~~~
# ZeroDivisionError: division by zero

#Para que omita este error y siga con el codigo hay que fijarse como
# se llama, en este caso es ZeroDivisionError
#hay que meterla dentro de un bloque try:

# try:
#     return num1 / num2
# except ZeroDivisionError:
#     print("No se puede dividir entre 0: ")
#     return "Operacion Erronea"
#

#RESULTADO
#
# No se puede dividir entre 0
# Operacion Erronea
# Operación ejecutada. Continuación de ejecúción del programa
#
