def sort_alphabets( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp

    return itemsList



#create a list from user's input
lst = []
for _ in range(5):
    i = input('Enter a string: ')
    lst.append(i)
print(sort_alphabets(lst))

        
    
    
 
    