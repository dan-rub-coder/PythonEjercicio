"""
def generarPares(limite):
    num =1
    miLista = []

    while num<limite:
        miLista.append(num*2)
        num += 1

    return miLista

print(generarPares(10))
"""


#------Con un generador sería----------
"""
def generarPares(limite):
    num = 1
    while num<limite:
        yield num*2
        num += 1

    
devuelvePares = generarPares(10)
#for i in devuelvePares:
#    print(i)
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
print(next(devuelvePares))
"""

#-----------------------------------------------------------
