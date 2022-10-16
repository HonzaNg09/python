q_peaches = int(input("Peaches \n-how many? "))
p_peaches = float(input("-price? "))
q_beans = int(input("Beans \n-how many? "))
p_beans = float(input("-price? "))
q_chicken = int(input("Chicken pieces \n-how many? "))
p_chicken = float(input("-price? "))
q_socks = int(input("Socks \n-how many? "))
p_socks = float(input("-price? "))
q_water = int(input("Bottle of water \n-how many? "))
p_water = float(input("-price? "))


q_total = q_peaches + q_beans + q_chicken + q_socks + q_water #total of quantity

#calculate total of cost: Sum of (price x quantity)
total_cost = q_peaches*p_peaches + q_beans*p_beans + q_chicken*p_chicken + q_socks*p_socks + q_water*p_water  

print("Total number of items purchased: {}".format(q_total))
print("Your weekly shop cost: {}".format(total_cost))