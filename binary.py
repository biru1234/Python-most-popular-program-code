'''
1              1, 10 =0-----1           n =7 ,
1 0             2,10=1
1 0 1           3,10=2 ---- 1
1 0 1 0         4, 10=2
1 0 1 0 1
1 0 1 0 1 0
1 0 1 0 1 0 1
'''

n = int(input("no of line"))
for i in range(1,n+1):
    '''var = "1"
    for j in range(1,i+1):
        print(var,end=" ")
        if var == "1":
            var ="0"
        else:
            var ="1"
    print()'''
    print("1 0 "*(int(i/2)),end="")
    if (i%2!=0):
        print("1")
    else:
        print()

