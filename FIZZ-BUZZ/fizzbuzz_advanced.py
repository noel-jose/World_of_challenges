num = int(input())
number_list = []
condition = []
count = 0
number_list = input().split()
condition = input().split()

for i in range (1,101):
    for j in range (0,num) :
        number = int(number_list[j])
        if i % number == 0 :
            print(condition[j],end = " ")
            count = count +1

    if count == 0:
        print(i,end =", ")

    else :
        print(end = ", ")

    count = 0    
    

