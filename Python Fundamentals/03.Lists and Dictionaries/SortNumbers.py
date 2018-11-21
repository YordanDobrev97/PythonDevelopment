numbers = map(int, input().split(' '))

list_integers = []

for number in numbers:
    list_integers.append(number)

list_integers.sort()

counter = 0
max_length = len(list_integers) - 1

for item in list_integers:
    if counter != max_length:
        print(item, end=' <= ')
    else:
        print(item)
    counter += 1

