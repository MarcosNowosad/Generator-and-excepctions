#Generadores II

#yield from
# utilidad:  Simplificar el codigo de los generadores en el caso de utilizar bucles anidados

#generador que devuelva una ciudades
#cuando colocamos un * adelante del argumento quiere decir que no sabemos cuantos parametros va a recibir
# no sabemos si son 2 , 3 o 7, y los va a recibir en forma de tupla

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
           # yield subElemento
        yield from elemento
#lo que hace yield from, es devolvernos los primeros subElementos del primer Elemento
#EJ con yield from
#M
#a

#sin yiel from

#Madrid
#Bs As

ciudades_devueltas= devuelveCiudades("Madrid", "Bs As", "Barcelona", "Bilbao", "Valencia")

#Si queremos que nos devuelva uno en uno, usamos el next

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
#con yield from accedemos a todos los sub elementos que queramos, en este caso lo llamamos 2 veces con next

