import math

x = int(input())
y = int(input())
c = (math.sqrt((x**2)+(y**2)))/2
d = math.sqrt((c**2)+(y**2)-(2*c*y*math.cos(math.atan(x/y))))
theta = math.asin((c*math.sin(math.atan(x/y)))/(d))
answer = int(round(math.degrees(theta), 0))
print(str(answer) + chr(176)) # chr(176) to add a degree symbol