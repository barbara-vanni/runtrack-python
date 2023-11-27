def draw_tapis_diagonale(n):
    for i in range(n + 3):
        if i == 0 or i == (n + 2):
            print('+' + '-' * (n + 1) + '+')
        elif i == 1:
            print('|' + '#' * n + ' ' + '|')
        elif i == n + 1:
            print('|' + ' ' + '#' * (n) + '|')
        else:
            diagonal_spaces = n - i + 1
            after_spaces = i - 1
            print('|' + '#' * diagonal_spaces + ' ' + '#' * after_spaces + '|')



draw_tapis_diagonale(10)
