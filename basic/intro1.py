# printing hello world
print('hello world')


# using variables
name = 'john'
print('\n')
print('Printing using variables')
print('hello', name)


# using input
# age = float(input('\nWhat is your age? '))
age =23
print('Your age is', age)

# using if else
if age >= 18:
    print('You are an adult now')
elif age < 10:
    print('You are still a kid')
else: 
    print('You are a teenager')



# assigning multiple variables
a, b, c = 1, 2, 3

# assigning same value to multiple variables
e = f = g = 4
print('value before swapping , a = ', a)

# swapping variables
a, b = b, a
print('value after swapping ')
print('a = ', a)
print('b = ', b)

# deleting variables
del e
# print('e = ', e)


# using lists

# creating a list
list1 = [1, 2, 3, 4, 5]
print('\n')
print('Printing a list')
print(list1)

# accessing elements of a list
print('\n')
print('Accessing elements of a list')
print(list1[0])
print(list1[1])


# accessing elements of a list by unpacking
print('\n')
print('Accessing elements of a list by unpacking')
a, b, c, d, e = list1
print(a)
print(b)
print(c)


# insert an element in a list
print('\n')
print('Inserting an element in a list')
list1[0] = 0
print('list1 after inserting at beginning by [] = ', list1)
list1.insert(0, 1)
print('list1 after inserting at beginning by insert() = ', list1)
list1.append(6)
print('list1 after inserting at end by append() = ', list1)



# deleting an element in a list
print('\n')
print('Deleting an element in a list')
del list1[0]
print('list1 after deleting at beginning by del = ', list1)


# using tuples

# creating a tuple
tuple1 = (1, 2, 3, 4, 5)
print('\n')
print('Printing a tuple')
print(tuple1)

# accessing elements of a tuple
print('\n')
print('Accessing elements of a tuple')
print(tuple1[0])

# accessing elements of a tuple by unpacking
print('\n')
print('Accessing elements of a tuple by unpacking')
a, b, c, d, e = tuple1
print(a)
print(b)
print(c)


# using dictionaries

# creating a dictionary
dict1 = {
    'name': 'john',
    'age': 20,
}

print('\n')
print('Printing a dictionary')
print(dict1)

# accessing elements of a dictionary
print('\n')
print('Accessing elements of a dictionary')
print(dict1['name'])
print(dict1['age'])

# adding elements to a dictionary
print('\n')
dict1['gender'] ='male'
dict1[1] = 1

print('Adding elements to a dictionary')
print(dict1)

# deleting elements from a dictionary
print('\n')
del dict1[1]
print('Deleting elements from a dictionary')
print(dict1)


# using sets

# creating a set
set1 = {1, 2, 3, 4, 5, 5}
print('\n')
print('Printing a set')
print(set1)

# adding elements to a set
print('\n')
print('Adding elements to a set')
set1.add(6)
print(set1)

# deleting elements from a set
print('\n')
print('Deleting elements from a set')
set1.remove(6)
print(set1)


# using loops

# using for loop
print('\n')
print('Using for loop')

for i in range(0, 5):
    print(i)

# for loop in dictionary
print('\n')
print('Using for loop in dictionary')

for key, value in dict1.items():
    print(key, value)


# using while loop
print('\n')
print('Using while loop')

i = 0
while i < 5:
    print(i)
    i += 1


# using functions

# defining a function
print('\n')
print('Defining a function')

def func1():
    print('Hello from func1')

# calling a function
func1()

# defining a function with arguments
print('\n')
print('Defining a function with arguments')

def add(a, b):
    return a + b

# calling a function with parameters
print('Calling a function with parameters')
print(add(1, 2))

# defining a function with default arguments
print('\n')
print('Defining a function with default arguments')

def add(a, b = 0):
    return a + b

# calling a function with default parameters
print(add(1))

# what is this f in front of a string

f'hello {name}'


fun =  lambda x: x[::]

print(fun('hello_world'))