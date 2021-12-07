class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left = left
        self.right=right


class doubly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail = None

    def insert_begin(self,data):
        node=Node(data)
        if self.head is None and self.tail is None:
            #node.left = self.head
            #node.right = self.tail
            self.head=node
            self.tail=node
            #node.right = self.tail
            '''print(self.head)
            print(self.tail)'''
            return
        itr=self.head
        node.right = self.head
        self.head = node
        itr.left=node
    def inset_last(self,data):
        node=Node(data)
        if self.head is None and self.tail is None:
            self.head=self.tail=node
            return
        itr=self.head
        while itr.right:
            itr=itr.right
        node.left=itr
        node.right=None
        self.tail=node
        itr.right=node

    def print_forward(self):
        itr=self.head
        while itr:
            print(f"<--{itr.data}-->",end="")
            itr=itr.right
    def print_backward(self):
        itr=self.tail
        while itr:
            print(f"<--{itr.data}-->", end="")
            itr=itr.left

if __name__=='__main__':
    link1=doubly_linkedlist()
    '''link1.insert_begin(6)
    link1.insert_begin(5)
    link1.insert_begin(7)
    link1.insert_begin(9)'''
    link1.inset_last(19)
    link1.inset_last(20)
    link1.inset_last(25)
    print("forward print")
    link1.print_forward()
    print()
    print("backward print")
    link1.print_backward()
