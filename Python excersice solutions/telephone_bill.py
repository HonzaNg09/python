call_rate = 0.15    
num_minute = int(input('Enter number of minutes: '))
charge = call_rate * num_minute
vat = charge * 0.2
total_bill = charge + vat 
print('Number of minutes used: '+ str(num_minute))
print('Basic call charge: £'+ format(charge,'.2f'))
print('VAT due: £' + format(vat,'.2f'))
print('Total bill: £' + format(total_bill,'.2f'))       