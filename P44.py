input = "Python"
input1 = "Programming"
output = ""
'''
for i  in input1:
    input += i
print(input)
'''
index = 0
while index < len(input1):
    input += input1[index]
    index += 1
print(input)