rb = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']


#prompt user for a number from 1 to 7 or -1
while True:
    n = int(input('Please enter a number from 1 to 7 or -1 to quit: '))
            
    if (n == -1):
        print('Quit')
        break 
    else:
        print(rb[n-1])

