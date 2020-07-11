count = 0
for i in range (1,101):

    if(i%3) == 0:
        print("Fizz",end = " ")
        count = count + 1
    
    if (i%5) == 0:
        print("Buzz",end = " ")
        count = count + 1

    if count == 0:
        print(i,end = " ")
    
    print(end = ", ")
    count = 0 


