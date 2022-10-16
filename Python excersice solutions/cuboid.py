w = int(input("Enter the width of the cuboid: ")) #width
h = int(input("Enter the height of the cuboid: ")) #height
l = int(input("Enter the length of the cuboid: "))#length


surface_area = 2*l*w + 2*l*h + 2*h*w #calculate surface area0
volume_cuboid = w*h*l                #calculate the volume
print("The sureface are of the cuboid is: {}".format(surface_area))
print("The volume of the cuboid is: {}".format(volume_cuboid))