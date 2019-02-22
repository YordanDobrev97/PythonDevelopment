elements = input().split(' ')
element = input()

found = False
for item in elements:
    if item == element:
        found = True
        break

if found:
    print('yes')
else:
    print('no')
