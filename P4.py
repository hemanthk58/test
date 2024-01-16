#Find the intersection of two sets
input1 = {1,2,3,4,5}
input2 = {2,3,4}
input = []
for each in input1:
    #print(each)
    if each in input2:
       # print(each)
        input.append(each)
print(set(input))