#Create a dictionary from a string –
input = "w3resource" 
#Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
output ={}
index = 0
'''
for char in input:
    if char in output:
        output[char] += 1
    else:
        output[char] =1
    print(input)
    print(output)
    '''
while index < len(input):
    char = input[index]
    if char in output:
        output[char] +=1
    else:
        output[char  ] = 1
    index += 1       
    print(input)
    print(output)