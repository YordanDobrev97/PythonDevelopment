line = input().split('|')

list_items = []

for i in range(len(line) - 1, -1,-1):
    items = line[i].split(' ')

    for current_item in items:
        if current_item != '':
            list_items.append(current_item)



for item in list_items:
    print(item, end=' ')


