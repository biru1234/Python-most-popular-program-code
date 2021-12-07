class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        node = Node(data,self.head)
        self.head=node
        #print(head)
    def print1(self):
        itr=self.head
        while itr:
            print(f"{itr.data}->",end="")
            #print(itr.next)
            itr=itr.next

    def insertatlast(self,data):
        node = Node(data)

        if self.head is None:
            self.head=node
            return
        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next=node
    def insertatnthpos(self,data,pos):
        node = Node(data)
        n=1
        itr=self.head
        if n==pos:
            node.next=self.head
            self.head=node
            return
        while itr:
            n=n+1
            if n==pos:
                node.next=itr.next
                itr.next=node
                return
            itr=itr.next
        print(f"please choose pos value between 1 to {n}")

    def middle1(self,data=None,insert=None):
        if self.head is None:
            print("no data exist in linkedlist")
            return
        slow = self.head
        if slow.next is None:
            print(f"only one data exist{slow.data}")
            return
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        print(f"your middle element is {slow.data}")
        if insert==True:
            node=Node(data)
            node.next=slow.next
            slow.next=node
    def delete1(self,data):
        itr=self.head
        if itr.data==data:
            self.head=itr.next
            return
        while itr.next:
            prev=itr
            itr=itr.next
            if itr.data==data:
                prev.next=itr.next
                itr.next=None
                return
        print("data not  present in linked list")
    def circularlist(self,data):
        node = Node(data,self.head)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node
    def print_circular(self):
        itr=self.head
        start=self.head
        print(f"{itr.data}-->",end="")
        itr=itr.next
        while itr and itr.data != start.data:
            print(f"{itr.data}-->",end="")
            itr = itr.next
        #print(f"{itr.data}-->", end="")
    def check_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next
            fast = fast.next
            if slow==fast:
                print("loop is detected")
                return
        print("loop is not exist")







if __name__ == '__main__':
    link1 = linkedlist()
    '''link1=linkedlist()
    link1.insert_begin(5)
    link1.insert_begin(10)
    link1.insert_begin(6)
    link1.insert_begin(8)
    link1.insert_begin(1)'''

    link1.insertatlast(5)
    link1.insertatlast(10)
    link1.insertatlast(6)
    link1.insertatlast(8)
    link1.insertatlast(1)
    link1.print1()
    print()
    '''link1.middle1()
    link1.insertatnthpos(50,1)
    link1.print1()
    print()
    link1.middle1()
    #link1.insertatnthpos(560,1)
    #link1.print1()
    #print()
    #link1.middle1()
    link1.insertatnthpos(560, 1)
    link1.print1()
    print()
    link1.middle1(77,True)
    link1.print1()
    print()
    link1.delete1(77)'''
    link1.circularlist(69)
    link1.print_circular()
    print()
    link1.check_loop()
