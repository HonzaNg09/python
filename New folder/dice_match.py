import random
a = random.randint(1,6)
b = random.randint(1,6)
count = 0 
if a == b:
    print('First dice is: ' + str(a))
    print('Sencond dice is: ' + str(b))   
    count = 1 
while  a != b:
    a = random.randint(1,7)
    b = random.randint(1,7)
    print('First dice is: ' + str(a))
    print('Sencond dice is: ' + str(b))

    count += 1 
print('Number of throws: ' + str(count))

    