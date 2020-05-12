nums = [1, 2, 3]

#------Esto es iterar-----------
#for num in nums:
#    print(num)


#dir() muestra los diferentes metodos o atributos que tiene el
#objeto que le pasemos

#__iter__()

#print(dir(nums))

#Se aplica el metodo iter para poder aplicar el metodo next a la lista
#i_nums = nums.__iter__()
#i_nums = iter(nums)

#print(i_nums)
#print(dir(i_nums))


#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
#Para evitar que salga un error usando los next 
"""
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
"""

#---------------------------------------------------------------------------------------------------------
#----------------ITERATOR---------------------
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

#nums = MyRange(1, 10)

#for num in nums:
#    print(num)




def my_range(start, end):
    current =start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

for num in nums:
    print(num)

#print(next(nums))
#print(next(nums))
#print(next(nums))

