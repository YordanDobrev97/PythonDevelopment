line = input().split(' ')

list_integers = []

for item in line:
    list_integers.append(int(item))


for i in range(0, len(list_integers)):
    if i % 2 == 1 and list_integers[i] % 2 == 1:
        print(f'Index {i} -> {list_integers[i]}')



