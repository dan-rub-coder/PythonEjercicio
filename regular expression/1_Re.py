import re

#cadena = 'Vamos a aprender extresiones regulares'


#----METODO SEARCH-------
#La primera vaariable que recibe es la palabra que
#queremos buscar y la segunda es el texto donde lo quremos buscar
#print(re.search("aprender", cadena))

"""
textoBuscar="aprender"
if re.search(textoBuscar, cadena) is not None:
    print('He encontrado el texto')
else:
    print('No he encontrado el texto')
"""


#-------METODO START, END y SPAN-----------
#Mostrará la posicion en la que inicia el texto y en que termina
#El metodo span hace star y end y lo introduce en una tupla
"""
textoBuscar = 'aprender'
textoEncontrado = re.search(textoBuscar, cadena)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
"""


#-------------METODO FINDALL----------------------
#Findall encuentra todas las coincidencias de la palabra en el texto
cadena ="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar = 'Python'

print(len(re.findall(textoBuscar, cadena)))

#findall devuelve una lista con la cantidad de palabras que hacen match en el texo
#si imprimo la longitud (len) de esa lista me retornara la cantidad de palabras que en el texto 
