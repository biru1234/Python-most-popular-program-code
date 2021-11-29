data=input()
data=data.split(",")
list1=[]
for x in data:
    list1.append(int(x))
sum_list=[]
sum_list.append(list1[0])
max_sum=list1[0]
for x in range(1,len(list1)):
    sum_list.append(list1[x])
    for y in range(x):
        if list1[x]>list1[y] and sum_list[y]>0:
            sum_list[x]=list1[x]+sum_list[y]
            if sum_list[x]>max_sum:
                max_sum=sum_list[x]
print(max_sum)
