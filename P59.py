a = 17
b = 5
quotient = 0
remainder = 0
'''
for i in range (a):
   if a > b:
        a -=b
        quotient +=1
   else:
        remainder = a
        break
print(quotient,remainder)
'''
while a > b:
    a -=b
    quotient +=1
remainder = a
print(remainder,quotient)