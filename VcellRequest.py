
from math import pi
d=raw_input("Type the diameter of the sphere for which you want to calculate the volume: ")
d=float(d)
r=d/2
V=(4.0/3.0)*pi*(r**3)
round (V)
print ("Volume of the sphere:%f" %(V))
