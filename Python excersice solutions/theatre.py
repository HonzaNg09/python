total_party = int(input('Enter the number of people: '))
num_adult = int(input('Enter the number of adults: '))
num_concession = int(input('Enter the number of concessions: '))
num_child = total_party - num_adult - num_concession
bill = 0
num_discount = 0 
adult_price = 10.50
child_price = 7.30
concessions = 8.40
bill_after_discount = 0


if num_adult + num_concession == 0:
    print('Not allowed to enter theatre')    
else:
    num_discount = num_child //10 
    if num_adult <= num_discount:
        num_adult = 0
    bill = num_concession* concessions + num_child * child_price + num_adult * adult_price
    if bill > 100:
        bill_after_discount = bill * 0.9
    else: 
        bill_after_discount = bill
    a = input('Enter a if tickets to will be collected in person \nEnter b if tickets will be sent through post: \n')
    
    
    print(bill)
    print(' '*16 +'BILL')
    print('Children tickets:         ' + str(num_child),'x', str(child_price),'     ',str(num_child * child_price))
    print('Adult tickets:            ' + str(num_adult),'x', str(adult_price),'     ',str(num_adult * adult_price))
    print('Concession tickets:       ' + str(num_concession),'x', str(concessions),'      ',str(num_concession * concessions))
    print('_' * 50 )
    
    print('Total ticket fees'+ ' '*23 + str(bill))
   
    print('_' * 50 )
    print('Total after discount'+ ' '*20 + str(bill_after_discount))
    if a == 'a':
        
        print('Ticket delivery fee                      0.00')
    elif a == 'b':
        print('Ticket delivery fee                       2.34')
        bill_after_discount += 2.34
    print('Total'+' '* 36 + str(bill_after_discount))
    
    
    
    

    
    


    
    
    
    
    
 
