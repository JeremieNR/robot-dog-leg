import math
import random

A=16.6
B=15.4
a=2*(math.pi)*((random.randrange(7500, 10000, 1))/10000)
b=2*(math.pi)*((random.randrange(1300, 3400, 1))/10000)
t=-math.acos(-(2/5))
error=0.1
time_interval=0.1

def fx(a,b):
    return(A*math.cos(a)-B*math.cos(a+b))
def fy(a,b):
    return(A*math.sin(a)-B*math.sin(a+b))
def x(t):
    return (5*math.cos(t))+2
def y(t):
    return (3*math.sin(t))-20


while (t<0):
    while float(abs(fx(a,b) - x(t))+abs(fy(a,b) - y(math.pi))) > float(error):
        a=2*(math.pi)*((random.randrange(7500, 10000, 1))/10000)
        b=2*(math.pi)*((random.randrange(1300, 3400, 1))/10000)
    
    t+=time_interval
#    print("Time: "+str(round(t,2))+",", "at the point: ("+str(round(fx(a,b),10))+", "+str(round(fy(a,b),10))+")")
    print(a,b)

while (0<t<(math.pi)):
    while float(abs(fx(a,b) - x(t))+abs(fy(a,b) - y(t))) > float(error):
        a=2*(math.pi)*((random.randrange(7500, 10000, 1))/10000)
        b=2*(math.pi)*((random.randrange(1300, 3400, 1))/10000)
    
    t+=time_interval
#    print("Time: "+str(round(t,2))+",", "at the point: ("+str(round(fx(a,b),10))+", "+str(round(fy(a,b),10))+")")
    print(a,b)

while ((math.pi)<t<((2*(math.pi))-math.acos(-(2/5)))):
    while float(abs(fx(a,b) - x(t))+abs(fy(a,b) - y(math.pi))) > float(error):
        a=2*(math.pi)*((random.randrange(7500, 10000, 1))/10000)
        b=2*(math.pi)*((random.randrange(1300, 3400, 1))/10000)
    
    t+=time_interval
#    print("Time: "+str(round(t,2))+",", "at the point: ("+str(round(fx(a,b),10))+", "+str(round(fy(a,b),10))+")")
    print(a,b)


print("Done")
