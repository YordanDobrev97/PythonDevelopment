items = input().split(' ')

dict = {}

for i in items:
    lowerCase = i.lower()
    if lowerCase in dict:
        dict[lowerCase] += 1
    else:
        dict[lowerCase] = 1

result = {}

for key,value in dict.items():
    if value % 2 == 1:
        result[key] = value

last_row_index = len(result) - 1
current_row = 0
for key in result.keys():
    if current_row == last_row_index:
        print(f'{key}', end='')
    else:
        print(f'{key}, ', end='')
    current_row += 1
