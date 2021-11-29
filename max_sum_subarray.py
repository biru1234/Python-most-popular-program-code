data=input()
data=data.split(",")
list1=[]
for x in data:
    list1.append(int(x))
max_sum=list1[0]
total_sum=0
for x in list1:
    if total_sum<=0:
        total_sum=x
    else :
        total_sum=total_sum+x
    if total_sum>max_sum:
        max_sum=total_sum
print(max_sum)

