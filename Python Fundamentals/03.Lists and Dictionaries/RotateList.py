strings = input().split(' ')

last_element = strings[-1]#get last element

list = []
list.append(last_element)


for i in range(len(strings) - 1):
    list.append(strings[i])

for i in list:
    print(i, end=' ')



