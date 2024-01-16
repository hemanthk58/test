#Get unique values from a list
input = [1, 2, 3, 3, 3, 4, 4]
list=[]
index = 0
'''
for each in input:
    if each not in list:
        list.append(each)
print(list)
'''
while index < len(input):
    if input[index] not in list:
        list.append(input[index])
    index +=1
print(list)