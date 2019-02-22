from collections import OrderedDict
line = input().split(', ')

dictionaries = {}

for i in range(len(line)):
    values = line[i]
    name = values.split(' ')[0]
    grade = float(values.split(' ')[1])
    dictionaries[name] = grade


dd = OrderedDict(sorted(dictionaries.items(), key=lambda x: x[0]))

for kvp in dd:
    print(kvp, dd[kvp])

