import json
            
            
    

try:
    with open('char_classes.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File doesn't exist")


row = data.values() #Retrieve dictionary values
row_list = list(row) #list of rows in dictionary

first_row_dic = row_list[0] #get the first dic in the list 
first_row = first_row_dic.keys() #Retrieve dictionary keys
first_row_list = list(first_row)
first_row_list.insert(0,"Class")

for i in first_row_list:
    print("{:12}".format(i),end = " ")

print('')    
for i in data:
    print("{:12}".format(i), end = " ")
    for j in data[i]:
        print("{:>6}".format(data[i][j]), end = "      ")
         
    print()