'''
 *             i =1 , n =5
 * *          i =2 , n =5
 * * *       i =3 , n =5
 * * * *
 * * * * *
'''
space = " "
star = "* "
n = int(input("enter no o f line \n"))
for i in range(1,n+1):
    print(star*i)
    #print(*range(1,i))
