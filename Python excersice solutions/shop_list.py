
def insertion_sort():
  for j in range(1,len(prices)):
    key = prices[j]
    items_key = items[j]
    i = j - 1
    while (i >= 0 and prices[i] > key):
        prices[i + 1] = prices[i]
        items[i + 1] = items[i]
        i -= 1
        prices[i+1] = key
        items[i+1] = items_key
  return prices,items
  
def lst_items():
    item,price = str(input()) , float(input())
    items.append(item)
    prices.append(price)



items = []
prices = []
count = 5  

while count > 0:
    lst_items()
    count -= 1

insertion_sort()
for i in range(0,len(items)):
    print(items[i] + ' ', end = '')
    print(prices[i])


        
        
        
        
        