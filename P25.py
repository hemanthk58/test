#Check whether a list contains a sublist
input = [2, 4, 3, 5, 7]
sub = [4, 3]
sublist = False
'''
index = 0
while index <= len(input)-len(sub):
    if input[index:index+len(sub)]==sub:
        sublist = True
        break
    index +=1
print(sublist)
'''

for i in range(len(input)-len(sub)+1):
    if input[i:i+len(sub)] == sub:
        sublist = True
    break
print(sublist)

'''

main_list = [2, 4, 3, 5, 7]
sublist_to_check = [4, 3]

# Checking using a while loop
contains_sublist = False
index = 0
while index <= len(main_list) - len(sublist_to_check):
    if main_list[index:index+len(sublist_to_check)] == sublist_to_check:
        contains_sublist = True
        break
    index += 1

print("Main List:", main_list)
print("Sublist to Check:", sublist_to_check)
print("Contains Sublist using while loop:", contains_sublist)
'''