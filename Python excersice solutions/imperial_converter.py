num_feet, num_inch = input("Enter your height in feet and inches: ").split()
print("Feet: ", num_feet)
print("Inches: ", num_inch)
num_feet = int(num_feet)
num_inch = int(num_inch)
feet_to_mm  = num_feet * 304.8
inches_to_mm = num_inch * 25.4
total_in_mm = feet_to_mm + inches_to_mm
total_in_cm = total_in_mm / 10
total_in_m = total_in_cm /100
total_in_km = total_in_m / 1000
print('Height in kilometres: ' +  str(total_in_km))
print('Height in metres: ' +  str(total_in_m))
print('Height in centimetres: ' +  str(total_in_cm))
print('Height in millimetres: ' +  str(total_in_mm))
