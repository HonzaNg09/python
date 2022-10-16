import math 
#room measurement
length_floor = float(40)
width_floor = float(30)
height_room = 3.4 

area_paint_cover = 5.1

#can measurement
diameter_can = 0.15
height_can = 0.3

#box measurement
length_box = 0.6
width_box = 0.3
height_box = 0.35


area_to_paint = 2* ( width_floor * height_room + length_floor * height_room)
num_can_to_buy = math.ceil(area_to_paint / area_paint_cover)


numcans_l = math.floor( length_box / diameter_can)  #numbers of cans can be put in the length of the box
numcans_w = math.floor( width_box / diameter_can)   #numbers of cans can be put in the width of the box
numcans_h = math.floor( height_box / height_can)    #numbers of cans can be put in the height of the box

num_can_in_box = (numcans_h * numcans_w * numcans_l)
num_full_box = (num_can_to_buy // num_can_in_box)
remain_cans = (num_can_to_buy % num_can_in_box)

print('Number of cans required:',num_can_to_buy)
print('Number of cans in box:',num_can_in_box)
print('Number of full boxes:',num_full_box)
print('Cans not packed in boxes:', remain_cans)
