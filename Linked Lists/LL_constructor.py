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

my_linkedlist = LinkedList(4)

print('Head = ', my_linkedlist.head.value)
print('Tail = ', my_linkedlist.tail.value)
print('Length = ', my_linkedlist.length)