#Sort a list alphabetically in a dictionary –
input = {'n1': ['c', 'b', 'a'], 'n2': ['e', 'd']}
for key in input:
    input[key] = sorted(input[key])
    print(input)
