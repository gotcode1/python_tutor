import itertools

#Simple itertools functions
#Function count
# counter = itertools.count(start=5, step = -2.5)
# #for loop will start counting by zero, and never stop

# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100,200,300,400]
# daily_data = list(zip(itertools.count(), data))
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# Function cycle - return an iterator 
# counter = itertools.cycle([1,2,3])
counter = itertools.cycle(('On', 'Off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Function repteat - also an infinite iterator

counter = itertools.repeat(2, times= 3)

squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))


# Combinations and permitations
# they don't repeat values (the result)
letters = ['a','b','c','d']
numbers = [0, 1, 2, 3]
names = ['John', 'Mary']

result = itertools.combinations(letters,2) #all different combinations of 2 values
for i in result:
    print(i)
# the print will be 'a','b'... but not 'b','a' - cause they are the same


#if order does matter use permutations
result = itertools.permutations(letters, 2)
for i in result:
    print(i)


#Include repeat values
# result = itertools.product(numbers, repeat= 4)
# for i in result:
#     print(i)

# result = itertools.combinations_with_replacement(numbers, 4)
# for i in result:
#     print(i)

# Function chain
#Loop from 3 lists at the same time
combined = itertools.chain(letters, numbers, names)
for i in combined:
    print(i)

result = itertools.islice(range(10), 1, 5, 2)
for i in result:
    print(i)

with open ('log.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end= '')

# Function compress
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)
for item in result:
    print(item)

def vl_2(n):
    if n < 2:
        return True
    return False

result = itertools.filterfalse(vl_2, numbers)
for i in result:
    print(i)
