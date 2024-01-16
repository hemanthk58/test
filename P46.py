list = [3,5,7,19,32,45,2,8]
max = list[0]
index = 0
'''
for each in list:
    if each > max:
        max = each
print(max)
'''
while index < len(list):
    if list[index] > max:
        max = list[index]
        index += 1
print(max)