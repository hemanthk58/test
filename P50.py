#Create a set from a list
input = [1, 2, 2, 3, 3, 3]
output = []
index = 0

'''
for each in input:
    output.append(each)
print(set(output))
'''
while index < len(input):
    output.append(input[index])
    index += 1
print(set(output))