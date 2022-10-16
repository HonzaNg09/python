cost_of_each_item= 20.0
sale_price_per_item = 40.0
fixed_cost = 50000.0

#calculation
profit_per_item = sale_price_per_item - cost_of_each_item
breakeven = fixed_cost/profit_per_item


print ("Cost to produce each item:", cost_of_each_item)
print("Sale price for each item:",sale_price_per_item)
print("Fixed costs:",fixed_cost)
print("Profit per item:",profit_per_item)
print('Breakeven',breakeven,'items')
