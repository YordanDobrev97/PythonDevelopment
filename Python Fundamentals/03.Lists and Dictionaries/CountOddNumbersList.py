line = input().split(' ')

list = []

for i in line:
    list.append(int(i))

count_odd_items = 0

for i in list:
    if i % 2 == 1:
        count_odd_items+=1


print(count_odd_items)