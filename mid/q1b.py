list = [1,2,3,4,5]
print(list[-1]) # 5
list.append(6)
print(list) # [1, 2, 3, 4, 5, 6]
list.insert(2,7)
print(list) # [1, 2, 7, 3, 4, 5, 6]
list.pop(2)
print(list) # [1, 2, 3, 4, 5, 6]
list.remove(1)
print(list) # [2, 3, 4, 5, 6]
list = list + [8,9,10]
print(list) # [2, 3, 4, 5, 6, 8, 9, 10]
print(len(list)) # 8
print(list[1:4]) # [3, 4, 5]
print(list[:3]) # [2, 3, 4]
print(list*2) # [2, 3, 4, 5, 6, 8, 9, 10, 2, 3, 4, 5, 6, 8, 9, 10]
