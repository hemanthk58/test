#Count the values associated with a key in a dictionary –
input = {'A': [1, 2, 3], 'B': [4, 5], 'C': [6]}
output = {}

'''
for key, values in input.items():
    output[key] = len(values)
    print(output)
'''

index = 0
keys = list(input.keys())
while index < len(input):
    key = keys[index]
    output[key] = len(input[key])
    index += 1







