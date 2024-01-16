tuple = (1,2,3,4)
number = 3
check_in = False
'''
for i in tuple:
    if i == number:
        check_in = True
        break
print(check_in)
'''
index = 0
while index < len(tuple):
    if tuple[index] == number:
        check_in = True
        break
    index +=1
print(check_in)