input = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
print("Id | Name | Age")
print("-"* 15)
for key, value in input.items():
    print(f"{key} | {value[0]:<4} | {value[1]}")

'''
my_dict = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}

# Print dictionary in table format using a for loop
print("ID | Name | Age")
print("-" * 15)
for key, value in my_dict.items():
    print(f"{key}  | {value[0]:<4} | {value[1]}")
    '''
'''
index = 1
while index <= len(input):
    key, value = index, input[index]
    print(f"{key} | {value[0]:<4} | {value[1]}")
    index += 1
    '''
'''
input = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
# Print dictionary in table format using a while loop
print("ID | Name | Age")
print("-" * 15)
index = 1
while index <= len(input):
    key, value = index, input[index]
    print(f"{key}  | {value[0]:<4} | {value[1]}")
    index += 1
    '''