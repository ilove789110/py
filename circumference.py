import math

radiusString = raw_input("Enter the radius of your circle: ")

radiusInt = int(radiusString)

circumference = 2 * math.pi * radiusInt

area = math.pi * (radiusInt ** 2)

print "The circumference is: ", circumference, \
    "The area is :", area

# id
print "The id of area object: ", id(area)

# type
print "The type of area object: ", type(area)
