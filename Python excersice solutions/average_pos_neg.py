sum_pos = 0
sum_neg = 0
count_pos = 0
count_neg = 0
average_pos = 0 
average_neg = 0  
for _ in range(10):
    item = int(input("Enter a number: "))
    if item > 0:
        sum_pos += item 
        count_pos += 1 
    elif item < 0: 
        sum_neg += item 
        count_neg +=1    
if count_pos != 0 and count_neg !=0:
    average_neg = sum_neg/count_neg
    average_pos = sum_pos/count_pos
elif count_neg + count_pos == 0 :
    print('The average is of the numbers is 0')
elif count_pos == 0:
    average_neg = sum_neg/count_neg
elif count_neg == 0:
    average_pos = sum_pos/count_pos

if count_pos == 0: 
    print ('No positive number was entered')
print('The average of the positive numbers is: ' + str(average_pos))

if count_neg == 0 :
    print('No negative number was entered')
print('The average of the negative numbers is: ' + str(average_neg))
    







