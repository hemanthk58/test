
input = [1, 2, 3, 4, 5]
output = []
end=len(input)-1
'''
while end >= 0:
    output.append(input[end])
    end -=1
print(output)
'''
'''
for each in range(len(input)-1,-1,-1):
    print(input[each])
    '''
for each in input:
    output=[each] + output
print(output)
print(len(output))