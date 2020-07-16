import math
def calclarg(n1,p1,n2,p2):
    if (p1 * math.log(n1))>(p2 * math.log(n2)):
        print(f"{n1}^{p1} is the largest")
    else :
        print(f"{n2}^{p2} is the largest")

num1,pow1,num2,pow2 = map(int,input().split(" "))
calclarg(num1,pow1,num2,pow2)
