# nested lists
list1 = [1, 2, [3, 4]]

# adding and updating list
list1.append(5)
list1[0] = 6
print(list1)
new_list = ['hi', 'bye']
list1.extend(new_list)
print(list1)
# only list gets updated. Original new_list doesn't disappear
print(new_list)

# deleting elements
del list1[0]
list1[1] = 2
# removes first occurrence of the element
list1.remove(2)
print(list1)
list1.pop()
print(list1)
# popping with index
list1.pop(0)
print(list1)

# list operations
print(list1 + new_list)
print(new_list * 3)
print('hi' in new_list)

# list functions
print(max([1, 2, 3, 5, 4]))
print(min([1, 2, 3, 5, 4]))

# tuple into list
tup = (1, 2, 3, 4)
list2 = list(tup)
print(list2)

# list compare
list3 = [11, 12, 131, 4]
# in ascending order
list3.sort()
list2.sort(reverse=True)
if list3 == list2:
    print(True)
else:
    print(False)

# list sum function
print(sum(list2))

# more list functions
print(list2.count(2))
print(list2)
print(list2.index(1))

# list and strings
word = 'hello'
list5 = list(word)
print(list5)
word = 'hello world'
list6 = word.split()
print(list6)
word = 'hello-world'
list7 = word.split('-')
print(list7)
print('=='.join(list7))