nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Comprenhensions es la forma de crear una lista con un codigo mas corto


#----------------------------------------------------------------------
#I want 'n' for each 'n' in nums

#my_list = []
#for n in nums:
#    my_list.append(n)
#print(my_list)

#my_list = [n for n in nums]
#print(my_list)
#------------------------------------------------------------------------

#I want 'n*n' for each 'n' in nums
#my_list = []
#for n in nums:
#    my_list.append(n*n)
#print(my_list)

#my_list = [n*n for n in nums]
#print(my_list)
#----------------------------------------------------------------------------


#-----------------Maps and lambda---------------------------------------------
#my_list = map(lambda n: n*n, nums)
#print(my_list)
#-------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
#-----I want 'n' for each 'n' in nums if 'n' is even
#my_list = []
#for n in nums:
#    if n%2==0:
#        my_list.append(n)
#print(my_list)


#my_list = [n for n in nums if n%2==0]
#print(my_list)

#FILTER---------------------
#my_list = filter(lambda  n: n%2==0, nums)
#print(list(my_list))
#-----------------------------------------------------------------------------------




#_----------------------------------------------------------------------------------
#I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'--
#my_list = []
#for letter in'abcd':
#    for num in range(4):
#        my_list.append((letter,num))
#print(my_list)


#my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
#print(my_list)
#--------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------
#----------------------------DICCIONARIOS-------------------------------
names = ['Bruce', 'Clarck', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#--------------ZIP-----------
#print(dict(zip(names, heroes)))

#my_dict = {}
#for name, hero in zip(names, heroes):
#    my_dict[name] = hero
#print(my_dict)

#my_dict = {name:hero for name,hero in zip(names, heroes) if name != 'Peter'}
#print(my_dict)
#-------------------------------------------------------------------------------




#---------------------------------------------------------------------------------
#----------------SET---------------------------------
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

#my_set =set()
#for n in nums:
#    my_set.add(n)
#print(my_set)


#my_set = {n for n in nums}
#print(my_set)
#-----------------------------------------------------------------------


#------------------------------------------------------------------------
#--------Generator Expressions--------------
#I want a yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

#def gen_func(nums):
    #for n in nums:
    #    yield n*n

#my_gen = gen_func(nums)


my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)