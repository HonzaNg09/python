total_candies = 40 #number of candies the teacher has
num_stu = 14 #number of students 


num_candies_splitted = total_candies//num_stu # number of candies are shared equally among children
remain_candies = total_candies % num_stu # number of candies the teacher keeps 

print ('Each child receives',num_candies_splitted,'candies')
print ('The number of candies teacher still has is',remain_candies)
