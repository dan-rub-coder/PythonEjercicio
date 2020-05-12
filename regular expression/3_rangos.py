import re

lista_nombres = ['Ana',
                  'Camilo',
                  'Victor',
                  'Valentina',
                  'Cristina']


#Con el caracter ^ negamos lo que estamos pidiendo dentro de los parantesis cuadrados
#pedimos lo que no esta en ese rango se ubica al inicio

for elemento in lista_nombres:
    if re.findall('[R-Z]', elemento):
    #if re.findall('[R-Z]%', elemento):
    #if re.findall('[^A-D]', elemento):
    #if re.findall('[R-ZA-d]', elemento): #Aca mostraría ambos rangos
    if re.findall('[.:]', elemento): #Muestra los caracteres que tienen un . o :    
        print(elemento)
