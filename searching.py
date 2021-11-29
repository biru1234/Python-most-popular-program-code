def binary_search(list1,start,end,value):
    if start>end:
        return False
    mid = int((start+end)/2)
    if list1[mid]==value:
        return True
    if list1[mid]>value:
        return binary_search(list1,start,mid-1,value)
    else:
        return binary_search(list1,mid+1,end,value)

def binary_serch1(list1,start,end,value):
    found = False
    while start<=end:
        mid = int((start+end)/2)
        if list1[mid]==value:
            found=True
            break
        elif list1[mid]>value:
            end = mid-1
        else:
            start=mid+1
    if found:
        print("data exist")
    else:
        print("not exist")

def linear_serch(list1,value):
    found = "false"
    for x in list1:
        if value == int(x):
            found = "true"
            break
    if found=="true":
        print("found your item")
    else:
        print("data does not found")


for t in range(int(input())):
    data=input("enter your data \n")
    value = int(input("enter search value = "))
    data=data.split(",")
    list1=[]
    for x in data:
        list1.append(int(x))
    binary_serch1(list1,0,len(list1)-1,value)
    '''if z:
        print("found")
    else:
        print("not found")'''