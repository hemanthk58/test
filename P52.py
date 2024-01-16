n = 5
output = 1
index =1
'''
for each in range(1,n+1):
    output *= each
    print(output)
'''
while index < n+1:
    output *= index
    index += 1
print(output)