import random
red_spaces = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black_spaces = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green_spaces = [0,00]
num = random.randint(-1,37)
if num in red_spaces:
    if num < 19 and num > 0:
        if num % 2 == 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Red')
            print('Pay Odd')
            print('Pay 1 to 18')
        elif num % 2 != 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Red')
            print('Pay Even')
            print('Pay 1 to 18')
    elif num < 37 and num > 18:
        if num % 2 == 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Red')
            print('Pay Odd')
            print('Pay 19 to 36')
        elif num % 2 != 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Red')
            print('Pay Even')
            print('Pay 19 to 36')
elif num in black_spaces:
    if num < 19 and num > 0:
        if num % 2 == 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Black')
            print('Pay Odd')
            print('Pay 1 to 18')
        elif num % 2 != 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Black')
            print('Pay Even')
            print('Pay 1 to 18')
    elif num <37 and num > 18:
        if num % 2 == 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Black')
            print('Pay Odd')
            print('Pay 19 to 36')
        elif num % 2 != 1:
            print('The spin resulted in ',num,'...',sep='')
            print('Pay',num)
            print('Pay Black')
            print('Pay Even')
            print('Pay 19 to 36')
elif num in green_spaces:
    if num == 0:
        print('The spin resulted in 0...')
        print('Pay 0')
    elif num == -1:
        print('The spin resulted in 00...')
        print('Pay 00')






