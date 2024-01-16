#Print a specified list after removing the 0th, 4th, and 5th elements
input = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output=[]
index = 0
'''
for i in range(len(input)):
    if i not in (0,4,5):
        output.append(input[i])
print(output)
'''
while index < len(input):
    if index not in (0,4,5):
        output.append(input[index])
    index +=1
print(output)
