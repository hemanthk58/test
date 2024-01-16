input = [{1: 10}, {2: 20}, {3: 30}]
output = {}
index = 0
'''
for i in input:
        output.update(i)
print(output)
'''
while index < len(input):
    output.update(input[index])
    index +=1
print(output)