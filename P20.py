lista=[1,2,3,4,5]
x=0
item =4
index=0
for i in range(len(lista)):
    if lista[i] == item:
        print(item)
        index = i
        break
if index is not None:
    print(f"The index of {item} in the list is:", index)
else:
    print(f"{item} is not present in the list.")