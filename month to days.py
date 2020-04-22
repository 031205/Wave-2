month = input('Input the full name of a month with capitalized initial: ')
if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print('30 days')
elif month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print('31 days')
elif month == 'February':
    print('28 or 29 days')
