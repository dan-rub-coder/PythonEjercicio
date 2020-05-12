import re

"""
lista_nombres = ['Daniel Rubiano', 'Victor Rubiano', 'Valentina Rubiano', 'Cristina Rojas', 'Daniel Rojas']

#El caracter ^ hace que busque la palabra que queremos al inicio
#El caracter $ busca el texto se encuentre en la ultima pisicion
for elemento in lista_nombres:
    #if re.findall('Daniel$', elemento):
    if re.findall('^Daniel', elemento):
        print(elemento)
"""



#[] Es un buscador de caracteres además se puede 
#usar en ejemplos como el siguiente ponemos dentro
# las opciones con las que puede salir esta palabra a buscar
"""
lista_nombres = ['hombres',
                  'mujeres',
                  'niños',
                  'niñas']

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)
"""

#Para buscar caracteres con tilde se usa este mismo caracter
lista_nombres = ['hombres',
                  'mujeres',
                  'camion',
                  'camión']

for elemento in lista_nombres:
    if re.findall('cami[oó]', elemento):
        print(elemento)

        