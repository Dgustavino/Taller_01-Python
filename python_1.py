""" EJERCIO 1:
EJERCIO 2:
"""

lista_nombres = [ 
        'nombre1', # this is list
        'nombre2' ]

lista_apellidos = ('apell1', 
        'apell2')  # this is tuplet

# imprimo los ejemplos de la parte superior
print(lista_nombres) 
print(lista_apellidos)

# ejemplos de la estructurada de datos set()
set1 = {123456789}
set2 = {1645}
print(set1,set2) # puedo enviar multiples paramentros al print()

resultado_set = set1.union(set2)
print(resultado_set) 

numero = 5

"""This is DocString
The next lines are conditional block If statement
and recieves the variable numero int() and returns True / False 
"""
if numero == 5:
    print("soy un numero")
else:
    print("seguro soy un texto")

palabra = 'soyUnalineadeCaracteres'
print(type(numero), type(palabra))

num1 = 100
num2 = 5

# referencias en memoria 
print(id(num1) , id(num2))

num3 = 100 # almacena la misma referencia si apunta al mismo objeto
print(id(num3))


# example of a try except: // finally - else:
try:
    variable = numero+palabra
except:
    print("Soy un Error en el try de multiplicar: " + str(numero) + " " + palabra)

