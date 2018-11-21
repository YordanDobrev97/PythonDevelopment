items = input().split(' ')
list = []

for i in items:
    list.append(int(i))

smallest_value = 9223372036854775807 #max value of long type, because in python no have max value

for i in list:
    if smallest_value > i:
        smallest_value = i

print(smallest_value)

