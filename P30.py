#Flatten a list without using recursion
input = [[1, 2], [3, 4], [5, 6]]
output = []
index_out= 0

'''
for each in input:
    for i in each:
        output.append(i)
print(output)
'''
while index_out < len(input):
    index_in = 0
    while index_in < len(input[index_out]):
        output.append(input[index_out][index_in])
        index_in +=1
    index_out += 1
print(output)
