sum_pos_num = 0
sum_neg_num = 0 

for i in range(5):
    num = int(input("Enter a number: "))
    if num > 0:
        sum_pos_num += num
    else:
        sum_neg_num += num 


print('Sum of positive integers: '+str(sum_pos_num))
print('Sum of negative integers: '+str(sum_neg_num))