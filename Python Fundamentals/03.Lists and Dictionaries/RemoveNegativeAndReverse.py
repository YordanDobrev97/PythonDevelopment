items = list(map(int, input().split(' ')))

list_positive_integers = []

for item in items:
    if item > 0:
        list_positive_integers.append(item)


if len(list_positive_integers) == 0:
    print('empty')
else:
    list_positive_integers.reverse()

    for integer in list_positive_integers:
        print(integer, end=' ')

