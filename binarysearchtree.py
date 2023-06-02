class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def insert(self,data):
        if data<self.data:
            if self.left ==None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data)

    
    def getMin(self):
        if self.left==None:
            return self.data
        else:
            return self.left.getMin()
        
    def getMax(self):
        if self.right==None:
            return self.right
        else:
            return self.right.getMax()

    
    def inordertraversal(self):
        if self.left!=None:
            self.left.inordertraversal()
        
        print(self.data)

        if self.right!=None:
            self.right.inordertraversal()

        


        

