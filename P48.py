#Merge two dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
index = 0

'''
output = dict1.copy()
for key, value in dict2.items():
    output[key] = value
print(output)
'''
merged_dict = dict1.copy()
keys = list(dict2.keys())
values = list(dict2.values())
while index < len(keys):
    merged_dict[keys[index]] = values[index]
    index += 1
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary using while loop:", merged_dict)
