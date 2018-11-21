line = input()
items = line.split(' ')
list = []

for i in items:
    list.append(int(i))

multiply = int(input())
newList = []

for i in list:
    newList.append(i * multiply)


for i in newList:
    print(i, end=' ')

