n = int(input())

items = []

for number in range(n):
    item = int(input())
    items.append(item)


sum = 0

for number in items:
    sum +=number


print(sum)
