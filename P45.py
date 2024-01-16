input = [1,2,3,4,5]
output = []
start_index = 2
end_index = 4
index = start_index

'''
for i in range(start_index,end_index):
    output.append(input[i])
print(output)
'''
while index < end_index :
    output.append(input[index])
    index += 1
print(output)