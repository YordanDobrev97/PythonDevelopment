number = int(input())


def print_triangle(num):
    for first_value in range(1, num + 1):
        for second_value in range(1, first_value + 1):
            print(f'{second_value} ', end='')

        print()

    for first_value in range(num - 1, 0,-1):
        for second_value in range(1, first_value + 1):
            print(f'{second_value} ', end='')
        print()




print_triangle(number)


