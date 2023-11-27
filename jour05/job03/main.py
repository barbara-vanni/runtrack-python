def draw_triangle(height):
    for i in range(height):

        before_spaces = height - i - 1
        print(' ' * before_spaces, end='')

        if i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print('/' + ' ' * (2 * i) + '\\')

draw_triangle(8)