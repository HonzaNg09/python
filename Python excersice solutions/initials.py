#get initials from name 

def initials(name):
    #splitting string into a list
    lst = name.split()
    cap_name = ''
    initial = ''
    
    #go through each element in list
    for i in (lst):
        cap_name = (i[0].upper() + '. ')
        initial += cap_name
    print(initial)
   
user_name = input('Enter your full name: ')
initials(user_name)

        
        
    
        
    