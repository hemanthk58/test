#Find the list of words that are longer than n from a given list of words
input = ['hello', 'world', 'name', 'python', 'programming']
n = 4
output = []
index = 0

for i in range(len(input)):
    temp = input[i]
    if n < len(temp):
        output.append(temp)
print(output)
    
        
'''

while index < len(input):
    output = input[index]
    if n < len(output):
        output.append(index)
        print(output)
    index += 1
    '''