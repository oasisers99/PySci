def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))



xs = [3,1,2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop() #remove and return the last element of the list
print(x, xs)


nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2]) 
print(nums[:]) # Get a slice of the whole list
nums[2:4] = [8, 9]
print(nums)


animals = ['cat', 'dog', 'monkey']
for animal in animals:
	print(animal)

for idx, animal in enumerate(animals):
	print('#%d: %s' % (idx + 1, animal))



#list comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
	squares.append(x ** 2)
print(squares)

nums = list(range(5))
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


#dictionaries
d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])
print('cat' in d) #check if a dic has a given key; prints "True"
d['fish'] = 'wet'
print(d['fish'])
print(d.get('monkey', 'N/A')) #Get an element with a default: prints "N/A"
print(d.get('fish', 'N/A')) #Get an element with a default: prints "wet"
del d['fish']
print(d.get('fish', 'N/A'))

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
	legs = d[animal]
	print('A %s has %d legs' % (animal, legs))

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)


#Sets
#a set is an unordered collection of distinct elements. As a simple example, consider the following:
animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)
animals.add('fish')
print('fish' in animals)
print(len(animals))
animals.add('cat') #adding an element that is already in the set does nothing
animals.remove('cat')
print(len(animals))

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
	print('#%d: %s' % (idx + 1, animal))

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)


#Tuples
d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print(type(t))
print(d)
print(d[t])
print(d[(1, 2)])