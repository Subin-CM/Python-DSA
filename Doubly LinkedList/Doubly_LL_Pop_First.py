class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def append(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.tail
            temp.next=new_node
            new_node.prev=temp
            new_node.next=None
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.tail
            self.tail=temp.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
    
    def prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=temp.next
            temp.next=None
            self.head.prev=None
        self.length-=1
        return temp


myDLL=DoublyLinkedList(7)
myDLL.append(9)
myDLL.append(8)
myDLL.printList()
myDLL.pop()
myDLL.printList()
myDLL.prepend(10)
myDLL.printList()
