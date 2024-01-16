#Get the difference between two lists
input1 = [1, 2, 3, 4]
input2 = [1, 2]
difference = []
'''
for i in input1:
    if i not in input2:
        difference.append(i)
print(difference)
'''
index = 0
while index < len(input1):
    if input1[index] not in input2:
        difference.append(input1[index])
    index += 1
    print(difference)
