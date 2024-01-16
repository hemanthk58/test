a = 5
b = 10
'''
# Swapping using a for loop
for i in range(1):  
    a, b = b, a

print("After swapping using for loop: a =", a, ", b =", b)
'''
count = 0
while count < 1: 
    a, b = b, a
    count += 1

print("After swapping using while loop: a =", a, ", b =", b)
