number = int(input())

def draw_squre(num):
    def draw_underscore(num):
        print('-'*(num * 2))


    def draw_body(num):
        for i in range(1, num-1):
            print('-' + '\\/'*(int((2 * num - 2) / 2)) + '-')

    draw_underscore(num)
    draw_body(num)
    draw_underscore(num)

draw_squre(number)
