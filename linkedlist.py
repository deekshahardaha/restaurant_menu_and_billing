class Node (object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class Linkedlist(object):
    def __init__(self):
        self.head=None
        self.counter=0

    def traverselist(self):
        actualNode = self.head
        while actualNode != None:
            print(actualNode.data)
            actualNode=actualNode.nextNode

    def insertstart(self,data):
        self.counter+=1
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    
    def size(self):
        return self.counter

    def insertbefore(self,data,next):
        if self.head.data==next:
            nn=Node(data)
            nn.nextNode=self.head
            self.head=nn
            self.counter+=1
        else:
            cur=self.head
            while cur.nextNode and cur.nextNode.data!=next:
                cur=cur.nextNode
            if cur.nextNode:
                nn=Node(data)
                nn.nextNode=cur.nextNode
                cur.nextNode=nn
                self.counter+=1
            else:
                print(f"Node with value {data} not found.")

    def insertafter(self,data,prev):
        if self.head.data==prev:
            nn=Node(data)
            nn.nextNode=self.head.nextNode
            self.head.nextNode=nn
            self.counter+=1
        else:
            preNode=self.head.nextNode
            while preNode and preNode.data!=prev:
                preNode=preNode.nextNode
            if preNode:
                nn=Node(data)
                nn.nextNode=preNode.nextNode
                preNode.nextNode=nn
            else:
                print(f"Node with value {data} not found.")



    def insertend(self,data):

        if self.head==None:
            self.insertstart(data)
            return
        self.counter+=1

        newNode=Node(data)
        actualNode = self.head

        while actualNode.nextNode != None:
            actualNode= actualNode.nextNode

        actualNode.nextNode=newNode


    def remove(self,data):
        if self.head:
            if data== self.head.data:
                self.head=self.head.nextNode
                self.counter-=1
            else:
                prev=self.head
                cur=self.head.nextNode
                while cur and cur.data != data:
                    prev=cur
                    cur=cur.nextNode 
                if cur!=None:
                    prev.nextNode=cur.nextNode
                    self.counter-=1
                else:
                    print(f"Node with value {data} not found.")

    def reverse(self):
        prev=None
        cur=self.head
        while cur:
            next=cur.nextNode
            cur.nextNode=prev
            prev=cur
            cur=next
        self.head=prev


link=Linkedlist()
link.insertend(12)
print(link.head.data)
link.insertend(14)
link.insertend(16)
link.insertend(13)
link.traverselist()
link.remove(15)
link.remove(14)
link.remove(13)
link.traverselist()
print(link.size())
link.insertstart(33)
link.traverselist()
link.insertbefore(44,12)
link.traverselist()
link.insertafter(55, 16)
link.insertafter(66, 44)
link.insertafter(23, 32)
link.traverselist()
link.reverse()
link.traverselist()