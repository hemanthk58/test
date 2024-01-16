input = [1, 2, 3]
input_a = [4, 5, 6]
index = 0
'''
for each in input_a:
    input.append(each)
print(input)
'''
while index < len(input_a):
    input.append(input_a[index])
    index += 1
print(input)