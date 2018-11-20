type = input()
first_value = input()
second_value = input()

def greather_of_two_values(type_input, first_value_input, second_value_input):
    result = None

    if type_input == 'int':
        first_value = int(first_value_input)
        second_value = int(second_value_input)
        result = max(first_value, second_value)
    elif type_input == 'string':
        result = max(first_value_input, second_value_input)
    else:
        result = max(first_value_input, second_value_input)


    return result


result = greather_of_two_values(type, first_value,second_value)
print(result)

