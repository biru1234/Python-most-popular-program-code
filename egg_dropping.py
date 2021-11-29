import sys
INT_MAX = 32767
def min1(a,b):
    return a if a<b else b

def max1(a,b):
    return a if a>b else b

def egg_drop(n,k):#n = egg no and k = floor
    if n==1:
        return k
    if k==1:
        return 1
    if n==0 or k==0 :
        return 0
    min2 = sys.maxsize
    for x in range(1,k+1):
        res = 1+max1(egg_drop(n-1,x-1),egg_drop(n,k-x))
        #each floor mai break hua and nahi hua dono case ka maximum lenge since we are checking worst case and in worse
        #it will break or not break do not know so max to find worse

        #now each floor ka ans ayega ab humea kis floor se drop karn chaiya pura k mai se woa minum mai ayega na
        #isliye har floor ka max baki sare fllor ke max se compare karega and joa minium hoga  woa harama ans
        if min2>res:
            min2=res
    return min2

def egg_drop_dynamic(n,k):
    dp=[[0 for x in range(n+1)] for y in range(k+1)]
    for i in range(0,k+1):
        for j in range(0,n+1):
            if j==1:
                dp[i][j]=i
            elif i==1 or i==0:
                dp[i][j]=i
            else:
                dp[i][j] = INT_MAX
                for x in range(1,i+1):
                    res=1+max1(dp[x-1][j-1],dp[i-x][j])
                    if res<dp[i][j]:
                        dp[i][j] = res
    return dp[-1][-1]



n = int(input("no of egg "))
k= int(input("no of floor "))
#print(egg_drop(n,k))
print("with dynamic")
print(egg_drop_dynamic(n,k))
