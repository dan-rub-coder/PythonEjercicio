import memory_profiler as mp
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (before): {}Mb'.format(mp.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                     'id':i,
                     'name':random.choice(names),
                     'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id':i,
                    'name':random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

#t1 = time.clock()
#people = people_list(1000000)
#t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (after): {}Mb'.format(mp.memory_usage_resource()))
print('Took {} second'.format(t2-t1))