
'''
* * * * *       i =1 , n=5
* * * *         i =2 , n=5       n-1+1
* * *          i =3 , n=5
* *
*
'''

space = " "
star = "* "
n = int(input("no of line \n"))
for i in range(1,n+1):
    print("* "*(n-i+1))