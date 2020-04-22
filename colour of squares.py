position = input('Input the position of a square on the chess board: ')
oddnumber = ['1','3','5','7']
evennumber = ['2','4','6','8']
oddletter = ['a','c','e','g']
evenletter = ['b','d','f','h']
if position[0] in oddletter:
    if position[1] in oddnumber:
        print('black')
    elif position[1] in evennumber:
        print('white')
elif position[0] in evenletter:
    if position[1] in oddnumber:
        print('white')
    elif position[1] in evennumber:
        print('black')


