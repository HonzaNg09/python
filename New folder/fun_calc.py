def add(num1, num2): 
    """ Add two numbers""" 
    print( num1 + num2 )
    
def subtract(num1, num2):
    """ Subtract two numbers"""
    print(  num1 - num2)
    
def multiply(num1, num2):
    """ Multiply two numbers"""
    print(num1 * num2)
    
def divide(num1, num2):
    """Divide two numbers"""
    if num2 == 0 :
        print("Can not divide by 0")
    else:
        print(num1 / num2)
def remainder(num1,num2):
    """ return remainder"""
    if num2 == 0 :
        print("Can not divide by 0")
    else: 
        print(num1 % num2)

    
#promp user for 2 integers
user_num1 = int(input('Enter the first integer: '))
user_num2 = int(input('Enter the second integer: '))

#print operation options
print("Please choose an operation: \n1.Add \n2.Subtract \n3.Multile \n4.Divide \n5.Remainder")
user_choice = int(input('Please enter a number from 1 to 5 to choose an operation: ' ))

if user_choice == 1:
    add(user_num1,user_num2)
elif user_choice == 2:
    subtract(user_num1,user_num2)
elif user_choice == 3:
    multiply(user_num1,user_num2)
elif user_choice == 4:
    divide(user_num1,user_num2)
elif user_choice == 5:
    remainder(user_num1,user_num2)

    

    