lst = []
rev_lst = []
#creating list from users input
for _ in range(5):
    i = (int(input('Please enter an integer: ' )))
    lst.append(i)   
    
    
for i in range(len(lst)-1,-1,-1):
    rev_lst.append(lst[i])
print(rev_lst)

