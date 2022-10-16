a = 0 
while True:
    a = int(input('Enter an integer of at least 2 digits or -1 to quit: '))
    a = str(a)
    if a == '-1':
        print('Program end')
        break
    elif int(a) <= 10 or int(a) >= 10000000000:
        print("Your input is invalid, please try again")
    else: 
        for i in a[::-1]:
                print(i, end='')
    
    
    