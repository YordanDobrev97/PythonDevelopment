single_string = input()

dictionary = {}

for symbol in single_string:
    if symbol in dictionary:
        dictionary[symbol] += 1
    else:
        dictionary[symbol] = 1

for kvp in dictionary:
    print(kvp,'->', dictionary[kvp])
