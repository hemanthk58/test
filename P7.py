#Convert a list to a tuple
input = [1, 2, 3, 4, 5]
output = ()
'''
for each in input:
    output += (each,) 
print(output)
'''
index = 0
while index < len(input):
    output += (input[index],)
    index +=1
    print(output)