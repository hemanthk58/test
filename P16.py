input = [1,2,3,4,5]
output = []
index = 0
'''
for each in input:
    output.append(each)
print(output)
'''
while index < len(input):
    output.append(input[index])
    index += 1
print(output)