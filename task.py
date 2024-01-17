i = [1,2,3,4,5]
reverse_i=[]
#print(reverse_i)
#for values in i:
   # print(values)
    #reverse_i=[values]+reverse_i
    #print(reverse_i)
#print(i[::-1])
#i.reverse()
#print(reverse_i)
#print(len(i))

aa=[1,2,3]
bb=[4,5,6]
#c=aa+bb
#aa += bb
#aa.extend(bb)
#print(aa)
#print(c)

a=[1,2,3]
b=[2,3,4]
#print(a&b)
#c= a.intersection(b)
#12
#a=set(a)
#b=set(b)
#c=a-b
#print(list(c))

total = sum(i)
avg=total/len(i)
#print(avg)

e=[1,2,2,3,3,3]
f=set(e)
g=list(f)
#print(g)
#print(list(set(e)))
#print(tuple(i))

h=5
j=10
#tem=h
#h=j
#j=tem
#h,j=j,h
#print(h,j)

k='A'
value = ord(k)
#print(value)
'''
keys= ['a', 'b', 'c']
values=  [1, 2, 3]
out =dict(zip(keys,values))
print(out)
'''

inpu=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#inpu.remove('Red')
#inpu.remove('Pink')
#inpu.remove('Yellow')
#del inpu[0]
#del inpu[3]
#del inpu[3]
#print(inpu)


#print(a-b)

i=sorted(i)
#print(i[1])

l=[]
#print(not(bool(l)))

#m=list(i)
#m=i.copy()
#print(m)

'''
list1=['hello','world','name','python','programming']
# n is length provided by user
#n=input('enter the required length')
n=4
for i in range(len(list1)):
    temp=list1[i]
    if(len(temp)>n):
        print(list1[i])  
'''
 
#print("Words longer than length", n, "are:", longer)
# Given list of words
#word_list = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'pineapple']

# Specify the length 'n'
#n = 4

# Filter words longer than length 'n'
#longer_than_n = [word for word in word_list if len(word) > n]

#print("Words longer than length", n, "are:", longer_than_n)

shallowlist= [[1, 2, 3], [4, 5], [6]]
flattenedlist = [item for sublist in shallowlist for item in sublist]
#print(flattenedlist)

lista=[1,2,3,4]
listb=[2,1,4,3]
#result=are_circularly_identical(lista, listb)
#if result:
    #print('True')
#else:
    #print('False')

# Function to check if two lists are circularly identical
def are_circularly_identical(list1, list2):
    # Check if the lists have different lengths
    if len(list1) != len(list2):
        return False

    # Concatenate list1 with itself to create a circular version
    circular_list = list1 + list1

    # Check if list2 is a sublist of the circular version of list1
    return any(list2 == circular_list[i:i + len(list2)] for i in range(len(list1)))

# Example lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 1, 2]

# Check if lists are circularly identical
result = are_circularly_identical(list_a, list_b)

if result:
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
