import math

numbers = map(int, input().split(' '))

list_sqrt_numbers = []
for number in numbers:
    if abs(math.sqrt(number)) == abs(int(math.sqrt(number))):
        list_sqrt_numbers.append(number)

list_sqrt_numbers.sort(reverse=True)

for number in list_sqrt_numbers:
    print(number, end=' ')


