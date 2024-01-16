'''#Find the index of an item in a specified list
input = [10, 20, 30, 40, 50]
value = 40
index_value = None
'''

'''
for index,each in enumerate(input):
    if each == value:
        index_value = index
        break
print(index_value)

'''
'''
my_list = [10, 20, 30, 40, 50]
item_to_find = 40

# Find the index using a for loop
index_found = None
for index, item in enumerate(my_list):
    if item == item_to_find:
        index_found = index
        break

print("List:", my_list)
print("Item to Find:", item_to_find)
print("Index using for loop:", index_found)

'''
'''
index = 0
while index < len(input):
    if input[index] == value:
        index_value == index
        break
    index +=1
print(index_value)
'''
my_list = [10, 20, 30, 40, 50]
item_to_find = 40

# Find the index using a while loop
index_found = None
index = 0
while index < len(my_list):
    if my_list[index] == item_to_find:
        index_found = index
        break
    index += 1

print("List:", my_list)
print("Item to Find:", item_to_find)
print("Index using while loop:", index_found)
