# Given the radius of a sphere find the diameter, circumference, surface area and volume
import math

radius = float(input("Enter the radius of the sphere: "))

diameter = radius * 2
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * math.pow(radius, 2)
volume = (4/3) * math.pi * math.pow(radius, 3)

print("Radius: " + str(radius))
print("")
print("Diameter: " + str(diameter))
print("Circumference: " + str(circumference))
print("Surface Area: " + str(surfaceArea))
print("Volume: " + str(volume))
