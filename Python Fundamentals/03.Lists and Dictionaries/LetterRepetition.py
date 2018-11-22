letters = input()

dict = {}

for letter in letters:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

for key,value in dict.items():
    print(f'{key} -> {value}')

