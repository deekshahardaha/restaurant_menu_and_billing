class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLL:
    def __init__(self):
        self.head=None
        self.counter=0
        self.last=None
    
    def addinempty(self,data):
        nn=Node(data)
        self.head=nn
        self.last=nn
    
    def insertstart(self,data):
        if self.last==None:
            self.addinempty(data)
        else:
            nn=Node(data)
            nn.next=self.head
            self.head=nn
            self.last.next=self.head
            self.counter+=1
    
    def insertafter(self,data,prev):
        if prev==self.last.data:
            print("inside <3 :)")
            insertend(self,data)
        else:
            cur=self.head
            while cur!= prev:
                cur=cur.next
            nn=Node(data)
            nn.next=cur.next
            cur.next=nn
            self.counter+=1
    
    def insertend(self,data):
        cur=self.head
        while cur!=self.last:
            cur=cur.next
        nn=Node(data)
        nn.next=cur.next
        cur.next=nn
        self.last=nn
        self.counter+=1

    def traverselist(self):
        cur=self.head
        while cur.next != self.head:
            print(cur.data,end=" ")
            cur=cur.next
        print(cur.data)


cll=CircularLL()
cll.insertstart(11)
cll.insertstart(22)
cll.insertend(33)
cll.insertafter(44, 22)
cll.traverselist()
