base = float(input())
height = float(input())


def get_triangle_area(base, heigth):
    return (base * heigth) / 2


print(f'{get_triangle_area(base, height):.12g}')
