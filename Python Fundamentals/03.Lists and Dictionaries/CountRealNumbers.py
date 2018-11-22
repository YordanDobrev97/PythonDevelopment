from collections import OrderedDict

items = list(map(float, input().split(' ')))

dict = {}

for item in items:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1


for key in sorted(dict.keys()):
    print(f'{key} -> {dict[key]} times')




