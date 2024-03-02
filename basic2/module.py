from polymorphism import *
from calculation import *


tom = Cat()
d = Dog()
a = Animal()


# print(tom.speak()) # Cat meows

# print(d.speak()) # Dog barks

# print(a.speak()) # Animal speaks

x=10
y =20

add_result = add(x,y)
print('Added result: ',add_result)

print('Subtracted result: ',sub(x,y))

print('Multiplied result: ',mul(x,y))

print('Divided result: ',div(x,y))