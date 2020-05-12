
#-----------------------------------------------Clase 1-------------------------------------------------
"""
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
    # Acciones adicionales que decoran
        print('Vamos a realizar un calculo')
        funcion_parametro()
        print('Se ha terminado la ejecución')#Acciones adicionales que decoran
    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(23-10)

suma()

resta()
"""
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------



def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
    # Acciones adicionales que decoran
        print('Vamos a realizar un calculo')
        funcion_parametro(*args)
        print('Se ha terminado la ejecución')#Acciones adicionales que decoran
    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(10, 3, 4)


resta(12,10)


potencia(5,3)