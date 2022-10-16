
rate = 0
rate_lst = ['Very poor','Poor','Neutral','Good','Very good']
count_rates = [0,0,0,0,0]
user_input = 0
total = 0
count = 0 
average = 0
while rate != -1:
    try:
        user_input = int(input('Enter your rate 1-5 or -1 to quit: '))
        if not(0 < user_input < 6 or user_input == -1): raise ValueError
    except ValueError: 
        print('Requires an integer between 1 and 5')
  
    
    if user_input == 1: 
        count_rates[0] += 1
        total += user_input
        count +=1 

    elif user_input == 2:
        count_rates[1] += 1
        total += user_input
        count +=1

    elif user_input == 3:
        count_rates[2] += 1
        total += user_input
        count +=1

    elif user_input == 4: 
        count_rates[3] +=1
        total += user_input
        count +=1

    elif user_input == 5:
        count_rates[4] += 1
        total += user_input
        count +=1
    elif user_input == -1:
        rate = -1 
        
for i in range(len(count_rates)):
    print(rate_lst[i] +': '+  str(count_rates[i])) 
try: 
    total/count
except ZeroDivisionError:
    print('Average = 0')
else:
    print(total/count)


    
        
    
        
    
    

    
    
    