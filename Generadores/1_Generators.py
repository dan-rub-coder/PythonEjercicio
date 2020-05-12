
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

#_-----------------Generator---yield---------------------
def square_numbers_g(nums):
    for i in nums:
        yield (i*i)

#print (next(my_nums))
#print (next(my_nums))
#print (next(my_nums))
#print (next(my_nums))
#print (next(my_nums))


#--------------------------------------------------    

#my_nums = square_numbers_g([1,2,3,4,5])

#---------------Otro generador y luego se usa el for para iterar entre el objeto que envia el generador----------------------
#my_nums = (x*x for x in [1,2,3,4,5])
#print (my_nums)
#for num in my_nums:
#    print(num)

#----------------para transformarlo a lista-----------------------------------
#my_nums = (x*x for x in [1,2,3,4,5])
#print(my_nums)
#print (list((my_nums)))




#-------------EJEMPLOS-------------------------
lista = [1,2,3,4,5]
pares = (x for x in lista if x%2==0 )
#print(list(pares))


#for x in lista:
#    if x%2==0:
#        print(x)



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

