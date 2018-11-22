line = input()
dict = {}


#this function return 1 if have number otherwise return 0
def is_value_number(number):
    try:
        value = int(number)
        return 1
    except ValueError:
        return 0


def change_value_of_key(key_input,value_input):
    for key,value in dict.items():
        if key == key_input:
            dict[key_input] = value_input


def add_items_in_dictionary(key,value):
    #not contains key in dictionary
    if contains_key_in_dictionary(key) == 0:
        dict[key] = value
    else:
        #dict[key] = value
        change_value_of_key(key,value)


def contains_key_in_dictionary(key):
    if key in dict:
        return 1
    return 0


while line != 'end':
    key = line.split(' = ')[0]
    value = line.split(' = ')[1]

    #check if value is number
    if is_value_number(value) == 1:
        add_items_in_dictionary(key,value)
    else:
        get_value_key = dict[value]
        #change_value_of_key(key, value)
        dict[key] = get_value_key

    line = input()

for key,value in dict.items():
    print(f'{key} === {value}')

