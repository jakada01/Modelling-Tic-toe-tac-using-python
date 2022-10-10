buttons = {'up-left':' ', 'up-middle':' ', 'up-right':' ',
           'mid-left':' ', 'mid-mid':' ', 'mid-right':' ',
           'buttom-left':' ', 'buttom-mid':' ', 'buttom-right':' '}
def my_board(board):
    print(board['up-left'] + '|' + board['up-middle'] + '|' + board['up-right'])
    print('-+-+-')
    print(board['mid-left'] + '|' + board['mid-mid'] + '|' + board['mid-right'])
    print('-+-+-')
    print(board['buttom-left'] + '|' + board['buttom-mid'] + '|' + board['buttom-right'])
turn = 'X'
for i in range(9):
    my_board(buttons)
    print('Now turn for ', turn, 'on which box? ')
    move = input('Please make your move')
    buttons[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
my_board(buttons)    

