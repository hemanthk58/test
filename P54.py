input = [1,2,3,4,5]
temp = 0
index = 0
'''
for i in input:
    temp += i
print(temp)
'''
while index < len(input):
    temp += input[index]
    index +=1
print(temp)