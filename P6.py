#Remove duplicates from a list
input = [1, 2, 2, 3, 3, 3]
list = []
'''
for each in input:
    if each not in list:
        list.append(each)
print(list)
'''
index = 0
while index < len(input):
    if input[index] not in list:
        list.append(input[index])
    index +=1
print(list)