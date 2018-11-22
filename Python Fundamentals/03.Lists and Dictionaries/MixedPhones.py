line = input()

dictionary_phones = {}

def only_digits(inputString):
    result = inputString.isdigit()
    return result

while line != 'Over':
    key = line.split(' : ')[0]
    value = line.split(' : ')[1]

    if only_digits(key):
        print('digits')

    line = input()
