#Exceptiones II
#ARREGLANDO MAS ERRORES CON try:
#en este caso capturamos 2 excepciones , ZeroDivisionError, y ValueError
#
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
#lo que hace este while True: es lo siguiente
#en caso de que introduzcamos un valor incorrector como un string, el while nos va a mostrar un error, y nos
#pedira que ingresemos devuelta un numero., en caso de que este bien, hace un break, y sigue con las demas lineas.

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo: ")


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

