#append two integers into a list
lst = []
lst1 = []
def print_int_list(lst,num1,num2):
    lst.append(num1)
    lst.append(num2)
#swapping the integers in the list
def swap(lst1,num1,num2):
    num1,num2 = num2,num1
    lst1.append(num1) 
    lst1.append(num2)


print_int_list(lst,1, 2)
print (lst)
swap(lst1,lst[0],lst[1])
print (lst1)
    
    
    
