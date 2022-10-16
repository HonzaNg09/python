lst =[['Jack','Queen','Queen','Ace'],['Queen','King','King','Ace'],['Jack','Jack','Queen','Ace'],['Jack','King','Ace','King']]



#position of first card
row1 = int(input('Enter the row of 1st card: '))
column1 = int(input('Enter the column of 1st card: '))

row2 = int(input('Enter the row of 2nd card: '))
column2 = int(input('Enter the column of 2nd card: '))

                   
if lst[row1][column1] == lst[row2][column2]:
    lst[row1][column1] = 'x'
    lst[row2][column2] = 'x'

print(lst)
for i in (lst):
    for j in i:
        if j == 'x':
            print('X' , end = ' ')
        else: 
            print ('*', end = ' ' )
    print(' ')
