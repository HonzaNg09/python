password = 'password'
quits = 'q'
continues = 'c'
while True:
    user = str(input('Enter your password: '))
    if user == password:
        print('Hello.')
        break
    else: 
        print('Wrong password')
    choice = str(input('Enter q to quit or c to continue: '))
    if choice == quits:
        break
    elif choice == continues: 
        continue
        
        