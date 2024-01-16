#Count occurrences of an element in a list
input = [1, 4, 2, 4, 5, 4, 1]
number = 4
count = 0
'''
for each in input:
    if each == number:
        count += 1
print(count)
        '''
index = 0
while index < len(input):
    if input[index] == number:
        count += 1
    index +=1
print(count)