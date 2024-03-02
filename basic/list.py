

# list 
list1 =['a','b','c','d','e']
print('printing a list = ', list1);

# list methods


# append
list1.append('new append value')
print('list1 after append = ', list1);

# clear
# list1.clear()
# print('list1 after clear = ', list1);


# copy
newList = list1.copy()
print('newList after copy = ', newList);

# count
countedValueA = list1.count('a')
print('countedValueA = ', countedValueA);

# extend
list1.extend(newList)
print('list1 after extend = ', list1);

# index
indexValue = list1.index('a')
print('indexValue = ', indexValue);

# insert
list1.insert(1, 'inserted value')
print('list1 after insert = ', list1);

# pop
list1.pop(1)
print('list1 after pop from index 1 = ', list1);

# remove
list1.remove('a')
print('list1 after remove first a = ', list1);

# reverse
list1.reverse()
print('list1 after reverse = ', list1);

# sort key
def sortKey (element):
    return len(element)

# sort
list1.sort( key=sortKey)
print('list1 after sort = ', list1);

# more about list sort

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def sortCarsKey(car):
    return car['year']

cars.sort( reverse=True, key=sortCarsKey)
print('cars after sort = ', cars);




print('/n/n')
print('Slice practice')

# slice list
s='hello_world'

# print(s[::-2])
# output: drwolh

# print(s[-1::])
# output: d

print(s[-55:-15:-1])




# x ='atik'

# def reverseString(word):
#     return word[::-1]

# reverse = lambda word: word[::-1]

# print(reverse(x))