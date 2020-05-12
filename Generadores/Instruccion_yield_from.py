#--------------------YIELD FROM---------------
#EL YIELD FROM SE USA PARA USAR EL FOR ANIDADO

#Cuando colocamos un * delante de la variable le estamos 
#indicando al programa que va recibir un numero indeterminado
#de elementos y ademas los va a recibir en form de tupla

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

#Para eviar el for anidado se usa el yield from--------------------

def devuelve_Ciudades(*ciudades):
    for elemento in ciudades:
            yield from elemento



ciudades_devueltas = devuelve_Ciudades("Madrid",'Barcelona','Bogotá','Medellín')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))