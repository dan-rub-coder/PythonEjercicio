
import numpy as np

#------------------------------------------------------------EJERCICIOS--------------------------------------------------
#Pedir que ingrese una palabra y que esta se repita 10 veces

palabra = input('Ingrese palabra: ' )

#palabras = (palabra for n in range(10))
#print(list(palabras))

def square_numbers_g(word):
    for i in range(10):
        yield (word)

#for x in range(10):
#    item = next(square_numbers_g(palabra))
#    print(item)
#---------------------------------------------------------------------------------------------------------------------------




#---Escribir un programa que pruebe si no hay elementos 0 en el array que pasemos

array = np.array([1,2,3,4,5])
"""
for x in array:
    if x == 0:
        print('Hay ''0'' en el array')
        break
    else:
        print(x)
"""

"""
elementos = ['Hay ''0'' en el array' if x == 0 else x for x in array]
print(elementos)
"""

"""
elementos = filter(lambda n: n != 0, array)
print (list(elementos))
"""
#----------------------------------------------------------------------------------------------------------------------------------