class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


myll=LinkedList(5)
myll.append(10)
myll.append(15)
myll.printList()
myll.printList()

