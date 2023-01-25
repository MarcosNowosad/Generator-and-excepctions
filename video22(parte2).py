#COMO CAPTURAR EXEPCIONES DE FORMA CONSECUTIVA
# una buena idea en ves de colocar varios except , ponemos lo siguiente
# except:

    #print("Ha ocurrido un error")

#lo que hace esto es capturar todos los errores del bloque, pero la desventaja es que no le avisa al usuario
# en que falló.
def divide():
    while True:
            try:

                    op1=float(input("Introduce un primer numero: "))
                    op2 = float(input("Introduce un segundo numero: "))

                    print("El resultado es " + str(op1/op2) )
                    break
            except ValueError:

                print("El valor introducido es erroneo")

            except ZeroDivisionError:

                print("No se puede dividir entre 0")
            finally:
                print("El programa sigue en curso apesar de los errores")
    print("calculo finalizado")

divide()

#Otra funcion acompañada de un try: es el finally:
# lo que hace esta funcios es que no importa si  el programa atrapa o no atrapa  exepciones,
# el finally se va a ejecutar igual.(mas adelante lo vamos a usar)