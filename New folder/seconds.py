s = int(input('Enter the number of seconds: '))

hours = s//60//60
minutes = s//60%60
seconds = s%60%60

print('Input         Hours      Minutes     Seconds')
print(''+str(s)+'           '+str(hours)+'           '+ str(minutes) +'           '+ str(seconds))