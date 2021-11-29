'''
    *       space =4             i =1 , n=5     spcae == n-i    star == i
   * *        space =3          i =2 , n=5
  * * *       space =2          i =3 , n=5
 * * * *
* * * * *
'''
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *     i = 1 n=5
 * * * *      i =2 n=5
  * * *      i =3 n=5
   * * 
    * 
'''
n = int(input("no of line in pyramid \n"))
space = " "
star = "* "
for i in range(1,n+1):
    #print(space*(n-i)+star*(i-1)+"*")
    '''for j in range(1,(n-i+1)):
        print(" ",end="")
    for j in range(1,(i)):
        print("* ",end="")
    print("*")'''
    print(" "*(n-i)+"* "*(i))
    #print(" "*(i-1)+"* "*(n-i+1))
for i in range(2,n+1):
    print(" "*(i-1)+"* "*(n-i+1))