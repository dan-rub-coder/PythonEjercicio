import re

nombre1='Daniel Rubiano'
nombre2='Antonio Gomez'
nombre3='Maria Lopez'
nombre4='Maniel Rojas'



#--------------------Funcion Match-----------------
#La funcion busca si hay un palabra en un determinado texto al comienzo siempre al comienzo
# ree.IGNORECASE ignora las mayusculas
#El caracter . me permite buscar las palabras que terminen con determinado argumento
#El caracter \d sirve para encontrar números

if re.match(".aniel", nombre2, re.IGNORECASE):
#if re.match("daniel", nombre1, re.IGNORECASE):
#if re.match("\d"", re.IGNORECASE):
    print('Si esta!!!!')
else:
    print('No existe...')


#------------------Funcion search---------------------
#La funcion search es muy parecida a la funcion match pero
#lo que las diferencia es que la funcion match siempre busca al principio
# mientras que la funcion search busca en cualquier punto 

if re.search("rubiano", nombre1, re.IGNORECASE):
    print('Si esta!!!!')
else:
    print('No existe...')


