sum_pos = 0
sum_neg = 0
for _ in range(10):
    item = int(input("Enter a number: "))
    if item > 0:
        sum_pos += item 
    else:
        sum_neg += item 

print('The sum of all positive integers is: ' + str(sum_pos))
print('The sum of all negative integers is: ' + str(sum_neg))
