number = input()


def return_multiply_even_odd_sum(number):
    even_sum = 0
    odd_sum = 0

    for value in number:
        if value == '-':
            continue

        convert_to_number = int(value)

        if convert_to_number % 2 == 0:
            even_sum += convert_to_number
        else:
            odd_sum += convert_to_number

    result = even_sum * odd_sum

    return result


result = return_multiply_even_odd_sum(number)
print(result)
