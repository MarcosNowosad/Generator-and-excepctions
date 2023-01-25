#Generadores I

#Estructuras que extraen valores de una funcion y se almacena en objetos iterables(
#(que se pueden reccorrer)
# Estos valores se almacenan de uno en uno

#Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta
# que  se solicita el siguiente. Esta caracteristica es conocida como "suspension de estados"

#Generadores ¿Que utilidad tienen?

#Son mas eficientes que las funciones tradicionales
#Muy utiles con listas de valores infinitos
#Bajo determinado escenarios, sera muy util que un generador devuelva los valores de uno en uno

#FUNCION TRADICIONAL
def generaPares(limite):
    num=1
    miLista= []
    while num<limite:
        miLista.append(num*2)
        num= num+1
    return miLista

print(generaPares(10))
#RESULTADO
# [2, 4, 6, 8, 10, 12, 14, 16, 18]


#GENERADOR

def generadorPares(limite):
    num=1

    while num<limite:

        yield num*2

        num= num+1

devuelvePares= generadorPares(10)

for i in devuelvePares:
    print(i)
#RESULTADO
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

#Generador que devuelve 1 en 1
def generadorPares(limite):
    num=1

    while num<limite:

        yield num*2

        num= num+1

devuelvePares= generadorPares(10)

print(next(devuelvePares))

print("Aqui seguiria el codigo")

print(next(devuelvePares))

print("Aqui seguiria el codigo")

print(next(devuelvePares))

#RESULTADO
# print("Aqui seguiria el codigo")
#
# 2
# Aqui seguiria el codigo
# 4
# Aqui seguiria el codigo
# 6
# Aqui seguiria el codigo
