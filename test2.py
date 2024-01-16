lista=[1,2,3,4,5]
x=0
#index=lista.index(x)
#print(index)
#item =4
#index=None
#for i in range(len(lista)):
    #if lista[i] == item:
        #print(item)
        #index = i
        #break
#if index is not None:
    #print(f"The index of {item} in the list is:", index)
#else:
    #print(f"{item} is not present in the list.")


list_a=[1, 3, 4, 5, 0, 2]
list_a=sorted(list_a)
#print(list_a[-2])

# Given list
given_list = ['p','q']

# Define the value of 'n'
n = 3

# Create a new list by concatenating the given list with a range from 1 to 'n'
new_list = given_list + list(range(1, n + 1))

#print("Concatenated list:", new_list)

from collections import Counter

# Example list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4]

# Get the frequency of elements in the list using Counter
frequency_counter = Counter(my_list)

#print("Frequency of elements:")
#for element, frequency in frequency_counter.items():
    #print(f"{element}: {frequency}")
'''
name = ['P','Y','T','H','O','N']
string_a =''.join(name)
print(string_a)
'''
'''
from itertools import permutations

# Given list
my_list = [1, 2, 3]

# Generate all permutations of the list
all_permutations = list(permutations(my_list))

print("All permutations of the list:", all_permutations)
'''
'''
input=[10, 20, 30, 40, 50]
n=40

index=input.index(n)
print(index)
'''
'''
item =4
index=None
for i in range(len(input)):
    if input[i] == item:
        print(item)
        index = i
        break
if index is not None:
    print(f"The index of {item} in the list is:", index)
else:
    print(f"{item} is not present in the list.")
    '''
'''
my_dict={'a': 10, 'b': 15, 'c': 4, 'd': 25, 'e': 8}
my_dict=sorted(my_dict.values(),reverse=True)
print(my_dict[:3])
'''
'''
# Input dictionary
my_dict = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}

# Print the dictionary in table format
print("ID | Name | Age")

for key, value in my_dict.items():
    print(f"{key}  | {value[0]} | {value[1]}")
    '''
'''
input= {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24} 
input = sorted(input.values(),reverse=True)
print(input[:3])
'''
'''
print("hello world")
'''

'''
a=3
b=5
print(a+b)
'''
'''
a=42
print(type(a))
'''
'''
input = "Python", "Programming"
result = ''.join(input)
print(result)
'''


'''
list_a = [1, 2, 3, 4, 5]
print(list_a[2:4])
'''

'''
input = [3, 1, 4, 1, 5, 9, 2]
input.sort()
print(input[-1])
'''

input = (1, 2, 3, 4)
n=3