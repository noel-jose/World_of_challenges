def findlongest(string):
    substring = ""
    count = 0 
    maxcount = 0
    for ch in string:
        if(ch in substring):
            substring = ""
            count = 0
        substring = substring + ch
        count = count + 1
        if(count > maxcount):
                maxcount = count
    print(maxcount)





string = input()
findlongest(string)
