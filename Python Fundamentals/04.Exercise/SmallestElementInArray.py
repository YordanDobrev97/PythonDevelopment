elements = input().split(' ')
elements = map(int, elements)

max_value = 9223372036854775807
min_value = max_value

for element in elements:
    if min_value > element:
        min_value = element
print(min_value)
