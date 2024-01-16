#Get the difference between two lists
'''
input1 = [1, 2, 3, 4]
input2 = [2,3]
list = []
index = 0
'''

'''
for each in input1:
    if each not in input2:
        list.append(each)
    print(list)
'''
'''
while index < len(input1):
    if input1 not in input2:
        list.append(input1[index])
        index +=1
print(list)
'''

input1 = [1, 2, 3, 4]
input2 = [3, 2]

difference = []
i = 0

while i < len(input1):
    if input1[i] not in input2:
        difference.append(input1[i])
    i += 1

print(difference)
