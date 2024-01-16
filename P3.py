list_a = [1,2,3]
list_b = [4,5,6]
n=0
'''
for each in list_b:
    list_a += [each]
print(list_a)

'''
while n < len(list_b):
    list_a.append(list_b[n])
    n+=1
print(list_a)

