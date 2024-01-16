
#Create a dictionary from two lists
keys =['a', 'b', 'c']
values =[1,2,3]
result =  {}
'''
for i in range(len(values)):
    result[keys[i]] =values[i]
    print(result)
    '''
index = 0
while index < len(keys):
    result[keys[index]] = values[index]
    index +=1
    print(result)
