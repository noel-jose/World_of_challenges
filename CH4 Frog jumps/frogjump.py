print("Enter the position and velocity of kid 1")
x1 = int(input())
v1 = int(input())
print("Enter the position and velocity of kid 2")
x2 = int(input())
v2 = int(input())
for t in range (0,1000):
    
    if((x1+(v1*t)) - (x2+(v2*t)) == 0):
        print(t)
    

